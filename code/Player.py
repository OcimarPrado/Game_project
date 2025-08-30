import pygame

from code.Entity import Entity
from Constantes import PLAYER_SPEED, WIN_WIDTH, WIN_HEIGTH
from code.Tiro import Tiro

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = PLAYER_SPEED
        self.tiros = []  # Lista de tiros

    def move(self):
        keys = pygame.key.get_pressed()

        # Movimento horizontal
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Movimento vertical
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Limitar dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIN_HEIGTH:
            self.rect.bottom = WIN_HEIGTH

        # Disparo
        if keys[pygame.K_SPACE]:
            if len(self.tiros) == 0 or self.tiros[-1].rect.x - self.rect.right > 20:
                self.tiros.append(Tiro((self.rect.right, self.rect.centery)))

    def update_tiros(self, window):
        for tiro in self.tiros:
            tiro.move()
            tiro.draw(window)

        # Remover tiros que saíram da tela
        self.tiros = [t for t in self.tiros if t.rect.x < WIN_WIDTH]
