# import pygame
#
# class Tiro:
#     def __init__(self, position: tuple):
#         self.surf = pygame.Surface((8, 4))  # Tamanho do tiro
#         self.surf.fill((255, 255, 0))       # Cor amarela
#         self.rect = self.surf.get_rect(center=position)
#         self.speed = 3
#
#     def move(self):
#         self.rect.x += self.speed  # Vai para a direita
#
#     def draw(self, window):
#         window.blit(self.surf, self.rect)
import pygame

class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, speed):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
