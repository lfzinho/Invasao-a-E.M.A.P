import pygame
import os
import classes

pygame.init()

largura_tela = 800
altura_tela = int(largura_tela * 0.8)
tela = pygame.display.set_mode((largura_tela, altura_tela))

pygame.display.set_caption("Sonia's Fury")
icon = pygame.image.load(os.path.join("sprites", "flame_icon.png"))
pygame.display.set_icon(icon)

jogador = classes.Soldado(200, 200, 2)

rodando = True
while rodando:

    tela.blit(jogador.image, jogador.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    pygame.display.update()

pygame.quit()
