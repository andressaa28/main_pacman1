import pygame
import os
import sys

# incializa o pygame
pygame.init()

# tamanho da tela
TILE_SIZE = 32
SCREEN_WIDTH = 448
SCREEN_HEIGHT = 496
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Simples")

# tela inicial
def tela_inicial():
     fonte_titulo = pygame.font.pygame.font.SysFont("Arial", 48, bold=False, italic=False)

#imagem do mapa

# imagem do pac-man

# função para carregar imagem de fantasma
def carregar_imagem():
    imagens = []
    for i in range(1, 4):  # 1 até 3
        caminho = os.path.join('imagens', f'fantasma{i}.png')
        imagem = pygame.image.load(caminho).convert_alpha()
        imagens.append(imagem)
    return imagens

# carregar imagem do fantasma verde
fantasma_img = pygame.image.load("fantasma_verde.png")
fantasma_img = pygame.transform.scale(fantasma_img, (32, 32))

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

# função para carregar um nível de um arquivo .txt
def load_level(level_num):
    try:
        with open(f"levels/level{level_num}.txt") as f:
            map_data = [line.strip() for line in f.readlines()]
        return map_data
    except FileNotFoundError:
        print(f"Erro: levels/level{level_num}.txt não encontrado.")
        sys.exit()

# exemplo de nível hardcoded (como dicionário python)
level1 = {
     "matrix": [
        "1111111111",
        "1000000001",
        "1011111101",
        "1000000001",
        "1111111111"
     ],
     "pacman_start": [1, 1],
     "ghost_den": [],
     "extra_voids": [],
     "num_rows": 5,
     "num_cols": 10,
     "cell_width": TILE_SIZE,
     "cell_height": TILE_SIZE
}

# carregando o mapa do nível
level_matrix = level1["matrix"]
ROWS = len(level_matrix)
COLS = len(level_matrix[0])

# posição inicial do pac-man
pacman_x = level1["pacman_start"][0] * TILE_SIZE
pacman_y = level1["pacman_start"][1] * TILE_SIZE
direction = (0, 0)

# ex: FPS = 60 -> o jogo tenta rodar as 60 atualizações por segundo, o que é considerado suave e padrão em jogos
# FPS (quadros por segundo) 
clock = pygame.time.Clock()
FPS = 60

# loop principl do jogo 
running = True
while running:
     screen.fill(colors.LIGHT_GREY)

     # eventos
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False

     # atualiza a tela
     pygame.pygame.flip()
     clock.tick(FPS)

pygame.quit()
sys.exit()


