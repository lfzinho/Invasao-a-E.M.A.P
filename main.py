import pygame
import os
from modulos import classes

pygame.init()

largura_tela = 800
altura_tela = int(largura_tela * 0.8)
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Altera o título e o ícone da aba
pygame.display.set_caption("Sonia's Fury")
icon = pygame.image.load(os.path.join("sprites", "flame_icon.png"))
pygame.display.set_icon(icon)

# Define FPS
clock = pygame.time.Clock()
FPS = 60


# Cria objetos da classe Soldado
jogador = classes.Soldado("jogador", 200, 200, 2, 5)
inimigo = classes.Soldado("inimigo", 400, 200, 2, 5)

movendo_direita = False
movendo_esquerda = False

# Define a cores
fundo = (144, 201, 220)


def desenha_fundo():
    """
    desenha o fundo toda vez que é chamada
    """
    tela.fill(fundo)


rodando = True
while rodando:

    clock.tick(FPS)

    desenha_fundo()

    jogador.update_animation()
    jogador.draw(tela)
    inimigo.draw(tela)

    jogador.move(movendo_esquerda, movendo_direita)


    #atualiza acoes do jogador
    if jogador.vivo:
        if jogador.in_air:
            jogador.update_action(2)#2: Pulo
        elif movendo_direita or movendo_esquerda:
            jogador.update_action(1)#1: Correndo
        else:
            jogador.update_action(0)#0: parado
        jogador.move(movendo_esquerda,movendo_direita)

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
            if event.key == pygame.K_w and jogador.vivo:
                jogador.jump = True
            if event.key == pygame.K_ESCAPE:
                rodando = False

        # Verifica teclas soltas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movendo_esquerda = False
            if event.key == pygame.K_d:
                movendo_direita = False
            if event.key == pygame.K_ESCAPE:
                rodando = False

    pygame.display.update()

pygame.quit()
