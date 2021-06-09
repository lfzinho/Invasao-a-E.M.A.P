import pygame
import os


class Soldado(pygame.sprite.Sprite):
    """
    Classe para jogadores e inimigos
    """
    def __init__(self, tipo, x, y, escala, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.velocidade = velocidade
        self.direction = 1
        self.flip = False
        self.tipo = tipo

        img = pygame.image.load(os.path.join("sprites", self.tipo, "idle.png"))
        self.image = pygame.transform.scale(img, (int(img.get_width() * escala), int(img.get_height() * escala)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, movendo_esquerda, movendo_direita):
        """
        verifica se o personagem deveria estar se movendo, e altera sua posição em x e y.
        Também verifica se o sprite necessita ser espelhado.
        :param movendo_esquerda: False ou True
        :param movendo_direita: False ou True
        :return:
        """
        dx = 0
        dy = 0

        if movendo_esquerda:
            dx = -self.velocidade
            self.direction = -1
            self.flip = True
        if movendo_direita:
            dx = self.velocidade
            self.direction = 1
            self.flip = False

        self.rect.x += dx
        self.rect.y += dy

    def draw(self, tela):
        """
        Desenha o personagem na tela
        :param tela: objeto tela
        :return:
        """
        tela.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
