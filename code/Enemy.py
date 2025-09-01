# #!/usr/bin/python
# # -*- coding: utf-8 -*-
#
#
#
#
# class Enemy(Entity1):
#     def __init__(self):
#         pass
#
#     def move(self, ):
#         pass

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random
import os
from code.Tiro import Tiro

ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name: str, position: tuple, projectile_group):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(os.path.join(ASSETS_PATH, name + ".png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.speed = 3
        self.projectile_group = projectile_group
        self.shoot_delay = random.randint(60, 120)

        # Definir sprite do tiro
        self.shot_image = os.path.join(ASSETS_PATH, f"{name}Shot.png")

    def update(self):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()

        self.shoot_delay -= 1
        if self.shoot_delay <= 0:
            self.shoot()
            self.shoot_delay = random.randint(60, 120)

    def shoot(self):
        tiro = Tiro(self.rect.centerx, self.rect.centery, self.shot_image, -7)
        self.projectile_group.add(tiro)
