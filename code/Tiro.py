import pygame

class Tiro:
    def __init__(self, position: tuple):
        self.surf = pygame.Surface((8, 4))  # Tamanho do tiro
        self.surf.fill((255, 255, 0))       # Cor amarela
        self.rect = self.surf.get_rect(center=position)
        self.speed = 3

    def move(self):
        self.rect.x += self.speed  # Vai para a direita

    def draw(self, window):
        window.blit(self.surf, self.rect)
