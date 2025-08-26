import pygame

print('starting pygame')
game = pygame.init()
window = pygame.display.set_mode(size=(1000, 600))  # Configuração da SCREEN
print('finishing pygame')

print('loop starting')
while True:
    # Ajustando eventos da Screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Fecha janela
            quit()  # finaliza pygame
