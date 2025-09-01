import os
import pygame
import random
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.Enemy import Enemy
from code.Entity import Entity
from Constantes import WIN_WIDTH, WIN_HEIGTH, PLAYER_SPEED, HEALTH

class Level:
    def __init__(self, window, name, select, bg_image, music, duration=15):
        self.window = window  # janela do jogo
        self.name = name  # nome do nível
        self.select = select  # player selecionado
        self.bg_image_name = bg_image  # background do nível
        self.music_file = music  # música do nível
        self.duration = duration  # duração do nível em segundos
        self.clock = pygame.time.Clock()  # relógio para controlar FPS
        self.start_ticks = pygame.time.get_ticks()  # marca início do nível

        # Grupos de sprites
        self.all_sprites = pygame.sprite.Group()  # todos os sprites
        self.enemy_group = pygame.sprite.Group()  # apenas inimigos
        self.player_shots = pygame.sprite.Group()  # tiros do player
        self.enemy_shots = pygame.sprite.Group()  # tiros dos inimigos

        # Backgrounds com efeito parallax
        self.backgrounds: list[Entity] = EntityFactory.get_entity(self.bg_image_name, (0, 0))

        # Score
        self.score = 0  # pontuação inicial
        self.score_font = pygame.font.SysFont("Lucida Sans Typewriter", 25)  # fonte do score
        self.score_music_file = 'Score.mp3'  # música da tela de score

        # Player selecionado
        if select == 'S E L E C T P1':
            players = EntityFactory.get_entity('Player1', (50, 200), self.player_shots)
        elif select == 'S E L E C T P2':
            players = EntityFactory.get_entity('Player2', (150, 200), self.player_shots)
        else:
            players = []

        self.all_sprites.add(*players)  # adiciona player ao grupo de sprites
        self.players = players  # lista de players

        # Música de fundo
        pygame.mixer.music.load(os.path.join('./code/assets', self.music_file))
        pygame.mixer.music.play(-1)  # toca em loop

        # Fonte para o timer
        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 30)

    def spawn_enemy(self):
        """Cria inimigos aleatórios na tela"""
        if random.randint(0, 100) < 2:  # 2% de chance por frame
            y = random.randint(50, WIN_HEIGTH - 50)  # posição vertical aleatória
            enemy_type = random.choice(['Enemy1', 'Enemy2'])  # tipo de inimigo
            enemies = EntityFactory.get_entity(enemy_type, (WIN_WIDTH, y), self.enemy_shots)
            self.enemy_group.add(*enemies)  # adiciona ao grupo de inimigos
            self.all_sprites.add(*enemies)  # adiciona ao grupo de todos os sprites

    def keep_player_in_screen(self, player: Player):
        """Impede que o player saia da tela"""
        if player.rect.top < 0: player.rect.top = 0
        if player.rect.bottom > WIN_HEIGTH: player.rect.bottom = WIN_HEIGTH
        if player.rect.left < 0: player.rect.left = 0
        if player.rect.right > WIN_WIDTH: player.rect.right = WIN_WIDTH

    def show_level_transition(self):
        """Mostra o nome do nível no início por 3 segundos"""
        transition_font = pygame.font.SysFont("Lucida Sans Typewriter", 60)
        surf = transition_font.render(self.name.upper(), True, (255, 255, 0))
        rect = surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGTH // 2))
        start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start < 3000:
            self.window.fill((0, 0, 0))  # limpa tela
            self.window.blit(surf, rect)  # desenha o nome do nível
            pygame.display.flip()
            self.clock.tick(60)  # mantém 60 FPS

    def show_game_over(self):
        """Mostra a tela de GAME OVER por 3 segundos"""
        font = pygame.font.SysFont("Lucida Sans Typewriter", 60)
        surf = font.render("GAME OVER", True, (255, 0, 0))
        rect = surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGTH // 2))
        start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start < 3000:
            self.window.fill((0, 0, 0))  # fundo preto
            self.window.blit(surf, rect)  # desenha GAME OVER
            pygame.display.flip()
            self.clock.tick(60)

    def draw_player_health(self, player: Player):
        """Desenha a barra de vida do player acima dele"""
        bar_width = 100
        bar_height = 10
        x = player.rect.left
        y = player.rect.top - 15
        health_ratio = player.health / HEALTH
        pygame.draw.rect(self.window, (255, 0, 0), (x, y, bar_width, bar_height))  # fundo vermelho
        pygame.draw.rect(self.window, (0, 255, 0), (x, y, bar_width * health_ratio, bar_height))  # vida verde

    def check_collisions(self):
        """Verifica colisões entre tiros e inimigos ou players"""
        for enemy in self.enemy_group:
            hits = pygame.sprite.spritecollide(enemy, self.player_shots, True)
            if hits:
                if hasattr(enemy, 'hit'):
                    enemy.hit(len(hits))  # reduz vida do inimigo
                else:
                    enemy.kill()
                self.score += len(hits) * 10  # cada inimigo vale 10 pontos

        for player in self.players:
            hits = pygame.sprite.spritecollide(player, self.enemy_shots, True)
            if hits:
                player.hit(len(hits))  # reduz vida do player

    def draw_score(self):
        """Desenha o score no canto superior direito"""
        score_surf = self.score_font.render(f"SCORE: {self.score}", True, (255, 255, 255))
        self.window.blit(score_surf, (WIN_WIDTH - 150, 10))

    def show_score_screen(self):
        """Mostra a tela de score final após game over"""
        pygame.mixer.music.load(os.path.join('./code/assets', self.score_music_file))
        pygame.mixer.music.play(-1)  # toca música do score

        score_bg = pygame.image.load('./code/assets/ScoreBg.png').convert_alpha()
        score_bg = pygame.transform.scale(score_bg, (WIN_WIDTH, WIN_HEIGTH))  # ajusta fundo

        start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start < 3000:
            self.window.fill((0, 0, 0))
            self.window.blit(score_bg, (0, 0))

            font = pygame.font.SysFont("Lucida Sans Typewriter", 60)
            surf = font.render(f"SCORE: {self.score}", True, (255, 255, 255))
            rect = surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGTH // 2))
            self.window.blit(surf, rect)

            pygame.display.flip()
            self.clock.tick(60)

    def run(self):
        """Loop principal do nível"""
        self.show_level_transition()  # mostra nome do nível
        running = True
        game_over = False

        while running:
            events = pygame.event.get()  # captura eventos
            for event in events:
                if event.type == pygame.QUIT:  # fecha o jogo
                    running = False
                    game_over = True

            self.window.fill((0, 0, 0))  # limpa tela
            for bg in self.backgrounds:  # atualiza e desenha backgrounds
                bg.move()
                bg.draw(self.window)

            self.spawn_enemy()  # cria inimigos

            for ent in self.all_sprites:  # atualiza todos os sprites
                if isinstance(ent, Player):
                    ent.update(events)
                    self.keep_player_in_screen(ent)
                    self.draw_player_health(ent)
                elif isinstance(ent, Enemy):
                    ent.update()

            self.player_shots.update()  # atualiza tiros do player
            self.enemy_shots.update()  # atualiza tiros inimigos

            self.all_sprites.draw(self.window)  # desenha todos os sprites
            self.player_shots.draw(self.window)  # desenha tiros do player
            self.enemy_shots.draw(self.window)  # desenha tiros inimigos

            self.draw_score()  # mostra score
            self.check_collisions()  # verifica colisões

            if any(not player.alive for player in self.players):  # checa se player morreu
                game_over = True
                running = False

            # Atualiza timer
            seconds = self.duration - (pygame.time.get_ticks() - self.start_ticks) // 1000
            timer_surf = self.font.render(f"Time: {seconds}", True, (255, 255, 255))
            self.window.blit(timer_surf, (10, 10))

            if seconds <= 0:  # termina nível quando tempo acaba
                running = False

            pygame.display.flip()
            self.clock.tick(60)  # mantém 60 FPS

        # Mostra GAME OVER e tela de score se player morreu
        if game_over:
            self.show_game_over()
            self.show_score_screen()

        return game_over  # retorna se houve game over
