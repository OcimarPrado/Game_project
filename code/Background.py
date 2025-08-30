from code.Entity import Entity
from Constantes import WIN_WIDTH

class Background(Entity):
    def __init__(self, name: str, position: tuple, speed: int = 0):
        super().__init__(name, position)
        self.speed = speed
        self.x1 = position[0]
        self.x2 = self.x1 + self.rect.width

    def move(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.x1 + self.rect.width <= 0:
            self.x1 = self.x2 + self.rect.width
        if self.x2 + self.rect.width <= 0:
            self.x2 = self.x1 + self.rect.width

    def draw(self, window):
        window.blit(self.surf, (self.x1, self.rect.top))
        window.blit(self.surf, (self.x2, self.rect.top))
