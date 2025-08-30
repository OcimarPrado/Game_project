import pygame
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.Entity import Entity
from Constantes import WIN_WIDTH, WIN_HEIGTH

class Level:
    def __init__(self, window, name, select):
        self.window = window
        self.name = name
        self.select = select
        self.clock = pygame.time.Clock()

        # Carregar fundo
        self.entity_list: list[Entity] = EntityFactory.get_entity('level1bg')

        # Carregar players dependendo da seleção
        if select == 'S E L E C T P1':
            self.entity_list += EntityFactory.get_entity('Player1', (50, 200))
        elif select == 'S E L E C T P2':
            self.entity_list += EntityFactory.get_entity('Player2', (150, 200))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill((0, 0, 0))

            # Loop de atualização e desenho deve estar **dentro do run()**
            for ent in self.entity_list:
                if hasattr(ent, 'move'):
                    ent.move()
                if hasattr(ent, 'draw'):
                    ent.draw(self.window)
                else:
                    self.window.blit(ent.surf, ent.rect)

                # Atualizar tiros se for Player
                if isinstance(ent, Player):
                    ent.update_tiros(self.window)

            pygame.display.flip()
            self.clock.tick(60)
