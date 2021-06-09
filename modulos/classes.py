import pygame
import os


class Soldado(pygame.sprite.Sprite):

    def __init__(self, x, y, escala):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(os.path.join("sprites", "idle.png"))
        self.image = pygame.transform.scale(img, (int(img.get_width() * escala), int(img.get_height() * escala)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
