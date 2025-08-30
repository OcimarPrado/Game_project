import pygame

class Foguete:
    def __init__(self, player):
        self.player = player
        self.surf = pygame.Surface((6, 6), pygame.SRCALPHA)
        self.color = (255, 100, 0)  # Laranja do foguete
        pygame.draw.circle(self.surf, self.color, (3, 3), 3)
        self.rect = self.surf.get_rect()
        self.timer = 10  # Quantos frames vai durar

    def update(self):
        # Posicionar atrás da nave
        self.rect.center = (self.player.rect.left - 3, self.player.rect.centery)
        self.timer -= 1

    def draw(self, window):
        window.blit(self.surf, self.rect)

    def is_alive(self):
        return self.timer > 0
