import pygame
import random
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.Enemy import Enemy
from code.Entity import Entity
from Constantes import WIN_WIDTH, WIN_HEIGTH

class Level:
    def __init__(self, window, name, select):
        self.window = window
        self.name = name
        self.select = select
        self.clock = pygame.time.Clock()

        # Grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.player_shots = pygame.sprite.Group()
        self.enemy_shots = pygame.sprite.Group()

        # Carregar fundo
        self.entity_list: list[Entity] = EntityFactory.get_entity('level1bg')

        # Carregar players dependendo da seleção
        if select == 'S E L E C T P1':
            players = EntityFactory.get_entity('Player1', (50, 200), self.player_shots)
        elif select == 'S E L E C T P2':
            players = EntityFactory.get_entity('Player2', (150, 200), self.player_shots)
        else:
            players = []

        # Adicionar players aos grupos
        self.entity_list += players
        self.all_sprites.add(players)

    def spawn_enemy(self):
        if random.randint(0, 100) < 2:  # 2% de chance por frame
            y = random.randint(50, WIN_HEIGTH - 50)
            enemies = EntityFactory.get_entity('Enemy1', (WIN_WIDTH, y), self.enemy_shots)
            self.enemy_group.add(enemies)
            self.all_sprites.add(enemies)

    def run(self):
        running = True
        while running:
            # Captura todos os eventos
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill((0, 0, 0))

            # Atualizar e desenhar fundo
            for ent in self.entity_list:
                if hasattr(ent, 'move'):
                    ent.move()
                if hasattr(ent, 'draw'):
                    ent.draw(self.window)
                else:
                    self.window.blit(ent.image, ent.rect)

            # Spawn inimigos
            self.spawn_enemy()

            # Atualizar e desenhar sprites
            for ent in self.all_sprites:
                if isinstance(ent, Player):
                    ent.update(events)  # passa eventos para o player
                else:
                    ent.update()
            self.all_sprites.draw(self.window)

            # Atualizar a tela e controlar FPS
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS
