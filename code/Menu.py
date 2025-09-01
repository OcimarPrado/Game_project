import pygame
from Constantes import WIN_WIDTH, COLOR_BLUE, MENU_OPTION, COLOR_R, COLOR_Y, MENU_CONTROLS

class Menu:
    def __init__(self, window):
        self.window = window
        # Carrega a imagem de fundo do menu
        self.surf = pygame.image.load('./code/assets/MenuBg.png')
        self.rect = self.surf.get_rect(topleft=(0,0))  # Define posição do fundo

    def run(self, menu_option=0):
        # Toca música de fundo em loop
        pygame.mixer.music.load('./code/assets/menu.mp3')
        pygame.mixer.music.play(-1)

        while True:
            # Desenha o fundo
            self.window.blit(self.surf, self.rect)
            # Desenha o título do jogo
            self.menu_text(50, "S k y  W a r", COLOR_BLUE, (WIN_WIDTH / 2, 70))

            # Desenha as opções do menu
            for i, option in enumerate(MENU_OPTION):
                # Destaca a opção selecionada em vermelho, as outras em amarelo
                color = COLOR_R if i == menu_option else COLOR_Y
                self.menu_text(25, option, color, (WIN_WIDTH / 2, 150 + 40 * i))

            # Atualiza a tela
            pygame.display.flip()

            # Captura os eventos do teclado e do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # Mover para baixo no menu
                    if event.key == MENU_CONTROLS['down'] or event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    # Mover para cima no menu
                    elif event.key == MENU_CONTROLS['up'] or event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    # Selecionar opção
                    elif event.key == MENU_CONTROLS['select'] or event.key == pygame.K_RETURN:
                        pygame.event.clear()  # Limpa os eventos pendentes
                        return MENU_OPTION[menu_option]  # Retorna a opção escolhida

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):

        font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        surf = font.render(text, True, text_color).convert_alpha()  # Cria superfície com o texto
        rect = surf.get_rect(center=text_center_pos)  # Centraliza o texto
        self.window.blit(surf, rect)  # Desenha na tela
