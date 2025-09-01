from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple, speed: int = 0):
        super().__init__(name, position)
        self.speed = speed  # Velocidade do movimento do fundo
        # Coordenadas horizontais para criar efeito de fundo em loop
        self.x1 = position[0]
        self.x2 = self.x1 + self.rect.width

    def move(self):
        # Move o fundo para a esquerda
        self.x1 -= self.speed
        self.x2 -= self.speed

        # Se a primeira imagem sair totalmente da tela, reposiciona ela atrás da segunda
        if self.x1 + self.rect.width <= 0:
            self.x1 = self.x2 + self.rect.width
        # Faz o mesmo para a segunda imagem
        if self.x2 + self.rect.width <= 0:
            self.x2 = self.x1 + self.rect.width

    def draw(self, window):
        # Desenha as duas imagens do fundo para criar o efeito contínuo
        window.blit(self.surf, (self.x1, self.rect.top))
        window.blit(self.surf, (self.x2, self.rect.top))
