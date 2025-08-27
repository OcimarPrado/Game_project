import pygame

from Constantes import WIN_WIDTH, WIN_HEIGTH
from code.Menu import Menu


# !/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        print('starting pygame')
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))  # Configuração da SCREEN


    def run(self):
        menu = Menu(self.window)
        menu.run()
        pass



