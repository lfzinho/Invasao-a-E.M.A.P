import pygame
import os
from modulos import classes

pygame.init()

# Variáveis Globais
LARGURA_TELA = 800
ALTURA_TELA = int(LARGURA_TELA * 0.8)
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
tempo_da_animacao = 100

# Altera o Título e o Ícone da Aba
pygame.display.set_caption("Sonia's Fury")
icone = pygame.image.load(os.path.join("sprites", "flame_icon.png"))
pygame.display.set_icon(icone)

# Define FPS
clock = pygame.time.Clock()
FPS = 60

movendo_direita = False
movendo_esquerda = False
atirando = False

# Define a cores
fundo = (144, 201, 220)


def desenha_fundo():
    """
    desenha o fundo toda vez que é chamada
    """
    TELA.fill(fundo)


rodando = True
while rodando:

    clock.tick(FPS)

    desenha_fundo()

    classes.jogador.update_animation()
    classes.jogador.update()
    classes.jogador.draw(TELA)
    classes.inimigo.update()
    classes.inimigo.draw(TELA)



    classes.jogador.move(movendo_esquerda, movendo_direita)


    # Atualiza ações do jogador
    if classes.jogador.vivo:
        if atirando:
            classes.jogador.shooting() # Atirando
        if classes.jogador.no_ar:
            classes.jogador.update_action(2) #2: Pulo
        elif movendo_direita or movendo_esquerda:
            classes.jogador.update_action(1) #1: Correndo
        else:
            classes.jogador.update_action(0) #0: parado
        classes.jogador.move(movendo_esquerda, movendo_direita)

    # Atualiza e desenha grupos
    classes.grupo_de_balas.update()
    classes.grupo_de_balas.draw(TELA)

    pygame.display.update()



    for event in pygame.event.get():
        # Sai do jogo quando a aba for fechada
        if event.type == pygame.QUIT:
            rodando = False

        # Verifica teclas apertadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movendo_esquerda = True
            if event.key == pygame.K_d:
                movendo_direita = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_w and classes.jogador.vivo:
                classes.jogador.pular = True
            if event.key == pygame.K_ESCAPE:
                rodando = False

        # Verifica teclas soltas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movendo_esquerda = False
            if event.key == pygame.K_d:
                movendo_direita = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_ESCAPE:
                rodando = False

    pygame.display.update()

pygame.quit()
