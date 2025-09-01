import os
import pygame
from code.Background import Background
from code.Player import Player
from code.Enemy import Enemy
from Constantes import ENTITY_SPEED, PLAYER_CONTROLS

# Caminho da pasta de assets (imagens)
ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0), projectile_group=None, controls=None):
        """
        Método para criar entidades do jogo (players, inimigos, background, menu)
        Recebe o nome da entidade, posição, grupo de projéteis (para tiros) e controles
        """
        entity_list = []  # Lista de entidades que serão retornadas
        name = entity_name.lower()  # Trabalhar sempre com nome em minúsculo

        # Background do Level 1
        if name == 'level1bg':
            for i in range(7):  # Criar todas as camadas do parallax
                layer_name = f"Level1Bg{i}"
                file_path = os.path.join(ASSETS_PATH, layer_name + ".png")
                if os.path.exists(file_path):
                    # Velocidade da camada do parallax
                    speed = ENTITY_SPEED.get(layer_name, 0)
                    entity_list.append(Background(layer_name, position, speed))
            return entity_list

        # Background do Level 2
        if name == 'level2bg':
            for i in range(7):
                layer_name = f"Level2Bg{i}"
                file_path = os.path.join(ASSETS_PATH, layer_name + ".png")
                if os.path.exists(file_path):
                    speed = ENTITY_SPEED.get(layer_name, 0)  # velocidade do parallax
                    entity_list.append(Background(layer_name, position, speed))
            return entity_list

        # Menu Background
        if name == 'menubg':
            file_path = os.path.join(ASSETS_PATH, 'MenuBg.png')
            if os.path.exists(file_path):
                # Fundo do menu não se move (velocidade 0)
                entity_list.append(Background('MenuBg', position, 0))
            return entity_list

        # Players
        if name.startswith('player'):
            file_path = os.path.join(ASSETS_PATH, f"{entity_name}.png")
            if os.path.exists(file_path):
                # Cria grupo de projéteis se não existir
                if projectile_group is None:
                    projectile_group = pygame.sprite.Group()
                # Cria o player com controles e grupo de tiros
                entity_list.append(Player(entity_name, position, PLAYER_CONTROLS, projectile_group))
            return entity_list

        # Inimigos
        if name.startswith('enemy'):
            file_path = os.path.join(ASSETS_PATH, f"{entity_name}.png")
            if os.path.exists(file_path):
                if projectile_group is None:
                    projectile_group = pygame.sprite.Group()
                # Cria o inimigo e adiciona ao grupo de projéteis
                entity_list.append(Enemy(entity_name, position, projectile_group))
            return entity_list

        # Retorna lista vazia caso não encontre o tipo
        return []
