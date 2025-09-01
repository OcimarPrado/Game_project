import pygame
import os
from code.Tiro import Tiro
from Constantes import PLAYER_CONTROLS, WIN_HEIGTH, WIN_WIDTH, HEALTH

# Caminho da pasta onde estão as imagens do jogo
ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')

class Player(pygame.sprite.Sprite):
    def __init__(self, name: str, position: tuple, controls, projectile_group):
        super().__init__()
        self.name = name
        # Carrega a imagem do player
        self.image = pygame.image.load(os.path.join(ASSETS_PATH, f"{name}.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)  # Define a posição inicial
        self.speed = 5  # Velocidade de movimento
        self.controls = controls  # Controles do player
        self.projectile_group = projectile_group  # Grupo para armazenar os tiros
        self.health = HEALTH  # Vida inicial
        self.alive = True  # Player está vivo no início

        # Imagem do tiro do player
        self.shot_image = os.path.join(ASSETS_PATH, f"{name}Shot.png")

    def update(self, events):
        keys = pygame.key.get_pressed()
        # Movimento contínuo baseado nas teclas pressionadas
        if keys[self.controls['up']]:
            self.rect.y -= self.speed
        if keys[self.controls['down']]:
            self.rect.y += self.speed
        if keys[self.controls['left']]:
            self.rect.x -= self.speed
        if keys[self.controls['right']]:
            self.rect.x += self.speed

        # Impede que o player saia da tela
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, WIN_HEIGTH)
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIN_WIDTH)

        # Verifica se apertou a tecla de atirar
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == self.controls['shoot']:
                self.shoot()  # Cria um tiro

    def shoot(self):
        # Cria o tiro e adiciona ao grupo de projéteis
        tiro = Tiro(self.rect.centerx, self.rect.centery, self.shot_image, 7)
        self.projectile_group.add(tiro)

    def hit(self, damage=1):
        """Reduz a vida do player quando ele é atingido"""
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.kill()  # Remove o player do jogo

    def draw_health_bar(self, surface):
        """Desenha a barra de vida acima do player"""
        bar_width = 50
        bar_height = 6
        fill = int((self.health / HEALTH) * bar_width)  # Vida proporcional

        # Posição da barra de vida
        x = self.rect.centerx - bar_width // 2
        y = self.rect.top - 10

        # Fundo vermelho representa a vida que foi perdida
        pygame.draw.rect(surface, (255, 0, 0), (x, y, bar_width, bar_height))
        # Parte verde mostra a vida atual
        pygame.draw.rect(surface, (0, 255, 0), (x, y, fill, bar_height))
