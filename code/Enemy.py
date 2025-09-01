import pygame
from code.Entity import Entity
from code.Tiro import Tiro
from Constantes import HEALTH

# Caminho da pasta de assets (imagens)
ASSETS_PATH = "./code/assets"

class Enemy(Entity, pygame.sprite.Sprite):
    def __init__(self, name: str, position: tuple, projectile_group: pygame.sprite.Group):
        # Inicializa as classes-pai
        pygame.sprite.Sprite.__init__(self)
        Entity.__init__(self, name, position)

        self.projectile_group = projectile_group  # Grupo onde os tiros do inimigo serão adicionados
        self.image = pygame.image.load(f"{ASSETS_PATH}/{name}.png").convert_alpha()  # Imagem do inimigo
        self.rect = self.image.get_rect(topleft=position)  # Posição inicial
        self.speed = 3  # Velocidade de movimento
        self.health = HEALTH  # Vida inicial
        self.shoot_timer = 0  # Contador para controlar quando o inimigo atira
        self.shoot_interval = 120  # Intervalo de frames entre os tiros

        # Imagem do tiro do inimigo
        self.shot_image = f"{ASSETS_PATH}/{name}Shot.png"

    def move(self):
        # Move o inimigo para a esquerda
        self.rect.x -= self.speed
        # Se sair da tela, reaparece do lado direito
        if self.rect.right < 0:
            self.rect.left = 800

    def shoot(self):
        """Inimigo dispara tiro em direção ao player"""
        tiro = Tiro(self.rect.centerx, self.rect.centery, self.shot_image, -5)  # -5 para ir para esquerda
        self.projectile_group.add(tiro)

    def update(self):
        self.move()  # Movimento automático
        # Controle do tiro automático
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_interval:
            self.shoot()  # Atira
            self.shoot_timer = 0  # Reinicia o contador

    def draw(self, surface):
        # Desenha o inimigo na tela
        surface.blit(self.image, self.rect)

    def hit(self, damage=1):
        """Reduz a vida do inimigo quando atingido"""
        self.health -= damage
        if self.health <= 0:
            self.kill()  # Remove o inimigo quando morre
