#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Constantes import WIN_WIDTH, COLOR_BLUE, MENU_OPTION, COLOR_W


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, MENU_PTION=None):
        pygame.mixer_music.load('./assets/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "S k y  W a r", COLOR_BLUE, ((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION)):
                self.menu_text(25, MENU_OPTION[i], COLOR_W, ((WIN_WIDTH / 2), 150 + 40 * i))

            pygame.display.flip()

            # Ajustando eventos da Screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting')
                    pygame.quit()  # Fecha janela
                    quit()  # finaliza pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
