import pygame
from Constantes import MENU_OPTION, WIN_WIDTH, WIN_HEIGTH
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGTH))

    def run(self):
        menu = Menu(self.window)
        menu_return = menu.run()

        if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
            level = Level(self.window, 'level1', menu_return)
            level.run()
        elif menu_return == MENU_OPTION[3]:
            pygame.quit()
            quit()
