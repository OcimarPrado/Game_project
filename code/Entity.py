from abc import ABC, abstractmethod
import pygame
import os

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets', name + '.png')).convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
