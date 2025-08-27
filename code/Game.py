import pygame
from code.Menu import Menu


# !/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        print('starting pygame')
        game = pygame.init()
        self.window = pygame.display.set_mode(size=(1000, 600))  # Configuração da SCREEN


    def run(self):
        menu = Menu(self.window)
        menu.run()

        while True:
            # Ajustando eventos da Screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting')
                    pygame.quit()  # Fecha janela
                    quit()  # finaliza pygame
