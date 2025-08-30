import os
from code.Background import Background
from code.Player import Player
from Constantes import ENTITY_SPEED

ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        entity_list = []

        name = entity_name.lower()

        # Background Level1
        if name == 'level1bg':
            for i in range(7):
                layer_name = f"Level1Bg{i}"
                file_path = os.path.join(ASSETS_PATH, layer_name + ".png")
                if os.path.exists(file_path):
                    speed = ENTITY_SPEED.get(layer_name, 0)
                    entity_list.append(Background(layer_name, position, speed))
                else:
                    print(f"Arquivo não encontrado: {file_path}")
            return entity_list

        # Menu
        if name == 'menubg':
            file_path = os.path.join(ASSETS_PATH, 'MenuBg.png')
            if os.path.exists(file_path):
                entity_list.append(Background('MenuBg', position, 0))
            else:
                print(f"Arquivo não encontrado: {file_path}")
            return entity_list

        # Players
        if name.startswith('player'):
            player_index = entity_name[-1]  # 'Player1' ou 'Player2'
            file_path = os.path.join(ASSETS_PATH, f'Player{player_index}.png')
            if os.path.exists(file_path):
                entity_list.append(Player(f'Player{player_index}', position))
            else:
                print(f"Arquivo não encontrado: {file_path}")
            return entity_list

        return []
