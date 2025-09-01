import pygame
from Constantes import WIN_WIDTH, COLOR_BLUE, MENU_OPTION, COLOR_R, COLOR_Y, MENU_CONTROLS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./code/assets/MenuBg.png')
        self.rect = self.surf.get_rect(topleft=(0,0))

    def run(self, menu_option=0):
        pygame.mixer_music.load('./code/assets/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(50, "S k y  W a r", COLOR_BLUE, ((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION)):
                color = COLOR_R if i == menu_option else COLOR_Y
                self.menu_text(25, MENU_OPTION[i], color, ((WIN_WIDTH / 2), 150 + 40 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == MENU_CONTROLS['down']:
                            menu_option = (menu_option + 1) % len(MENU_OPTION)
                        elif event.key == MENU_CONTROLS['up']:
                            menu_option = (menu_option - 1) % len(MENU_OPTION)
                        elif event.key == MENU_CONTROLS['select']:
                            pygame.event.clear()  # limpa eventos pendentes
                            return MENU_OPTION[menu_option]
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        pygame.event.clear()  # limpa todos os eventos pendentes
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect(center=text_center_pos)
        self.window.blit(surf, rect)
