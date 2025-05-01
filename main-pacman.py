import pygame
import os
import sys
import random # gera números aleatórios e faz escolhas aleatórias

# incializa o pygame
pygame.init()

# constantes
tile_size = 32
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
FPS = 60

# cores
class colors:
        LIGHT_GREY = (79, 79, 79) # chão
        DARK_GREY = (56, 56, 56) # parede
        DARK_RED = (125, 45, 45) # vermelho escuro
        LIGHT_RED = (149, 56, 56) # vermelho claro
        BEIGE = (203, 194, 135) #bege claro
        DARK_GREEN = (17, 115, 35) # verde escuro
        GREEN = (28, 158, 52) # verde
        LIGHT_GREEN = (37, 173, 62) # verde claro
        LIGHTER_GREEN = (37, 173, 98) # verde mais claro bárbara sua chata
        AQUA_GREEN = (52, 203, 120) # verde água                                         
        DARK_YELLOW = (136, 158, 28) # amarelo escuro 
        LIGHT_YELLOW = (163, 188, 40) # ammarelo claro
        BLACK = (0, 0, 0) # preto
        WHITE = (253, 252, 252) # branco
        LIGHT_BLUE = (172, 188, 233) # azul escuro
        DARK_BLUE = (7, 57, 167) # azul escuro
        LIGHTER_BLUE = (203, 231, 246) # azul mais claro
        RED = (244, 12, 12) # vermelho
        DARK_BLACK = (6, 0, 0) # preto escuro
        DARKER_PURPLE = (43, 3, 36) # roxo escurão
        WHITE_PURPLE = (246, 236, 240) # roxo quase branco
        LIGHT_YELLOW = (232, 233, 144) # amarelo clarinho 
        NEON_PURPLE = (228, 0, 255) # roxo neon 
        DARK_PURPLE = (75, 3, 63) # roxo escuro 
        PURPLE = (188, 18, 160) # roxo
        NEON_PINK = (255, 0, 214) # rosa neon 
        PINK_PINK = (255, 0, 113) # rosa pink
        PINK = (207, 15, 91) # rosa

# tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Melhorado")
clock = pygame.time.Clock()

# carregar imagwns
pacman_img = pygame.image.load("imagens/pacman.png")
pacman_img = pygame.transform.scale(pacman_img, (tile_size, tile_size))

fantasma_img = pygame.image.load("imagens/fantasma.png")
fantasma_img = pygame.transform.scale(fantasma_img, (tile_size, tile_size))

ponto_img = pygame.Surface((8, 8))
ponto_img.fill(colors.LIGHT_YELLOW)

especial_img = pygame.Surface((16, 16))
especial_img.fill(colors.WHITE)

# fonte
font = pygame.font.SysFont("Arial", 24)

# mapas base
mapa_base = [
    "11111111111111111111",
    "10000000001100000001",
    "10111111101111111101",
    "10100000100000000101",
    "10101110111110110101",
    "10100010000010100101",
    "10111111111110111101",
    "10000000000000000001",
    "11111111111111111111"
]

# Gerar mapa aleatório (ainda simples)
def gerar_mapa():
    mapa = []
    for linha in mapa_base:
        nova_linha = ""
        for c in linha:
            if c == "0":
                nova_linha += random.choice(["0", ".", "*"])
            else:
                nova_linha += c
        mapa.append(nova_linha)
    return mapa

# Tela inicial
def tela_inicial():
    esperando = True
    while esperando:
        screen.fill(colors.BLACK)
        titulo = font.render("Pressione ESPAÇO para jogar", True, colors.WHITE)
        screen.blit(titulo, (SCREEN_WIDTH//2 - titulo.get_width()//2, SCREEN_HEIGHT//2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                esperando = False

# Tela de reinício
def tela_reinicio():
    esperando = True
    while esperando:
        screen.fill(colors.BLACK)
        texto = font.render("Pressione ESC para reiniciar", True, colors.RED)
        screen.blit(texto, (SCREEN_WIDTH//2 - texto.get_width()//2, SCREEN_HEIGHT//2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                esperando = False
                main()

# Classe jogador
class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.escudo = False
        self.tempo_escudo = 0

    def mover(self, mapa):
        novo_x = self.x + self.dx
        novo_y = self.y + self.dy
        if mapa[novo_y][novo_x] != "1":
            self.x = novo_x
            self.y = novo_y

    def desenhar(self):
        screen.blit(pacman_img, (self.x * tile_size, self.y * tile_size))

# Classe NPC
class Fantasma:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, pacman, mapa):
        opcoes = [(0,1), (0,-1), (1,0), (-1,0)]
        melhor = (0,0)
        menor_dist = 9999
        for dx, dy in opcoes:
            nx, ny = self.x + dx, self.y + dy
            if mapa[ny][nx] != "1":
                dist = abs(pacman.x - nx) + abs(pacman.y - ny)
                if dist < menor_dist:
                    menor_dist = dist
                    melhor = (dx, dy)
        self.x += melhor[0]
        self.y += melhor[1]

    def desenhar(self):
        screen.blit(fantasma_img, (self.x * tile_size, self.y * tile_size))

# Função principal do jogo
def main():
    global score, vidas
    tela_inicial()
    score = 0
    vidas = 3
    mapa = gerar_mapa()
    pacman = Pacman(1, 1)
    fantasmas = [Fantasma(10, 5), Fantasma(15, 6)]

    running = True
    while running:
        screen.fill(colors.BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.dx, pacman.dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    pacman.dx, pacman.dy = 1, 0
                elif event.key == pygame.K_UP:
                    pacman.dx, pacman.dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    pacman.dx, pacman.dy = 0, 1

        pacman.mover(mapa)

        for fantasma in fantasmas:
            fantasma.mover(pacman, mapa)
            if fantasma.x == pacman.x and fantasma.y == pacman.y:
                if pacman.escudo:
                    fantasmas.remove(fantasma)
                else:
                    vidas -= 1
                    if vidas <= 0:
                        tela_reinicio()
                        return
                    pacman.x, pacman.y = 1, 1

        celula = mapa[pacman.y][pacman.x]
        if celula == ".":
            score += 10
            mapa[pacman.y] = mapa[pacman.y][:pacman.x] + " " + mapa[pacman.y][pacman.x+1:]
        elif celula == "*":
            pacman.escudo = True
            pacman.tempo_escudo = pygame.time.get_ticks()
            score += 50
            mapa[pacman.y] = mapa[pacman.y][:pacman.x] + " " + mapa[pacman.y][pacman.x+1:]

        if pacman.escudo and pygame.time.get_ticks() - pacman.tempo_escudo > 5000:
            pacman.escudo = False

        for y, linha in enumerate(mapa):
            for x, bloco in enumerate(linha):
                if bloco == "1":
                    pygame.draw.rect(screen, colors.LIGHT_BLUE, (x * tile_size, y * tile_size, tile_size, tile_size))
                elif bloco == ".":
                    screen.blit(ponto_img, (x * tile_size + 12, y * tile_size + 12))
                elif bloco == "*":
                    screen.blit(especial_img, (x * tile_size + 8, y * tile_size + 8))

        pacman.desenhar()
        for fantasma in fantasmas:
            fantasma.desenhar()

        texto = font.render(f"Score: {score}  Vidas: {vidas}", True, colors.WHITE)
        screen.blit(texto, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

main()


