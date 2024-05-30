import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
# Música de fundo do jogo e controle de volume
pygame.mixer.music.set_volume(0.3)
musica_de_fundo = pygame.mixer.music.load('audio/Mind-Bender.mp3')
pygame.mixer.music.play(-1)

# Som de colisao
barulho_colisao = pygame.mixer.Sound('audio/smw_coin.wav')
# Som de game over
derrota = pygame.mixer.Sound('audio/defeat.mp3')

# Dimensões do display da tela
largura = 640
altura = 480

velocidade = 10
x_controle = velocidade
y_controle = 0

#Tamanho da cobra
x_cobra = int(largura/2) 
y_cobra = int(altura/2)

#Tamanho da maça
x_maca = randint(40, 600)
y_maca = randint(50, 430)

# Pontuação inicial, e a fonte e tamanho da letra marcando a pontuação
pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

# Codigos para aumentar o tamanho da cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
       

        pygame.draw.rect(tela, (147,103,191), (XeY[0], XeY[1], 20, 20))

# Codigos para reiniciar o jogo e zerar as variaveis cobra e pontuação
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2)
    y_cobra = int(largura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40,600)
    y_maca = randint(50,430)
    morreu = False

while True:
    relogio.tick(30)
    tela.fill((124,217,17))
    
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        # codigos para movimentar a cobra com as teclas WASD
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
        

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (147,103,191), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            derrota.play()
            for event in pygame.event.get():
                if event.type ==QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()   

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450,40))

    
    pygame.display.flip()