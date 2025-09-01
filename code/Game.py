import os
import pygame
from Constantes import MENU_OPTION, WIN_WIDTH, WIN_HEIGTH, LEVEL_TIMER
from code.Level import Level
from code.Menu import Menu

SCORES_FILE = './code/assets/scores.txt'  # arquivo para armazenar scores

class Game:
    def __init__(self):
        pygame.init()  # inicializa o pygame
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGTH))  # cria a janela do jogo

    def save_score(self, score):
        """Salva o score no arquivo"""
        if not os.path.exists(SCORES_FILE):  # se arquivo não existir, cria
            with open(SCORES_FILE, 'w') as f:
                f.write('')
        with open(SCORES_FILE, 'a') as f:  # adiciona score no final do arquivo
            f.write(f'{score}\n')

    def show_scores(self):
        """Mostra os últimos scores salvos"""
        if not os.path.exists(SCORES_FILE):
            scores = []  # nenhum score salvo
        else:
            with open(SCORES_FILE, 'r') as f:
                scores = [line.strip() for line in f.readlines() if line.strip()]  # lê scores existentes

        self.window.fill((0, 0, 0))  # limpa a tela
        font_title = pygame.font.SysFont("Lucida Sans Typewriter", 50)  # fonte título
        font_score = pygame.font.SysFont("Lucida Sans Typewriter", 30)  # fonte scores

        title_surf = font_title.render("SCORES", True, (255, 255, 0))  # desenha título
        title_rect = title_surf.get_rect(center=(WIN_WIDTH//2, 50))
        self.window.blit(title_surf, title_rect)

        # mostra os últimos 10 scores
        for i, s in enumerate(reversed(scores[-10:])):
            score_surf = font_score.render(f"{i+1}. {s}", True, (255, 255, 255))
            self.window.blit(score_surf, (WIN_WIDTH//2 - 50, 120 + 35*i))

        pygame.display.flip()  # atualiza tela

        waiting = True
        while waiting:  # espera o jogador pressionar qualquer tecla ou fechar a janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    waiting = False  # qualquer tecla fecha a tela de scores

    def run(self):
        menu = Menu(self.window)  # cria menu
        menu_return = menu.run()  # executa menu e recebe opção escolhida

        if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:  # se escolher iniciar jogo
            # Level 1
            level1 = Level(self.window, 'LEVEL 1', menu_return, 'Level1Bg', 'Level1.mp3', duration=LEVEL_TIMER)
            game_over = level1.run()  # executa level 1
            self.save_score(level1.score)  # salva score do level 1
            if game_over:
                level1.show_game_over()  # mostra tela de game over
                pygame.quit()
                return

            # Level 2
            level2 = Level(self.window, 'LEVEL 2', menu_return, 'Level2Bg', 'Level2.mp3', duration=LEVEL_TIMER)
            game_over = level2.run()  # executa level 2
            self.save_score(level2.score)  # salva score do level 2
            if game_over:
                level2.show_game_over()  # mostra tela de game over
                pygame.quit()
                return

        elif menu_return == MENU_OPTION[2]:  # se escolher ver scores
            self.show_scores()  # mostra scores

        elif menu_return == MENU_OPTION[3]:  # se escolher sair
            pygame.quit()
            quit()
