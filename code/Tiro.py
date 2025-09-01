import pygame

class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, speed):
        super().__init__()
        # Carrega a imagem do tiro
        self.image = pygame.image.load(image_path).convert_alpha()
        # Define o retângulo do tiro, centralizando na posição inicial (x, y)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed  # Velocidade do tiro

    def update(self):
        # Move o tiro horizontalmente de acordo com a velocidade
        self.rect.x += self.speed
        # Remove o tiro se ele sair da tela (lado esquerdo ou direito)
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
