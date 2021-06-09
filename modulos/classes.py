
import pygame
import os

# Define as variaveis do jogo
GRAVITY = 0.6



class Soldado(pygame.sprite.Sprite):
    """
    Classe para jogadores e inimigos
    """
    def __init__(self, tipo, x, y, escala, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.vivo = True
        self.tipo = tipo
        self.velocidade = velocidade
        self.direction = 1
        self.vel_y = 0
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.in_air = True
        self.jump = False

    

        self.update_time = pygame.time.get_ticks()

        tipos_de_animacao = ["Idle","Run","Jump"]
        for animation in tipos_de_animacao:
            lista_temporaria = []
            #conta quantos arquivos tem na pasta (ou seja, quantos frames tem a animação)
            num_of_frames = len(os.listdir(os.path.join("sprites", self.tipo,animation)))
            print(num_of_frames," em ",animation)
            for i in range(num_of_frames):
                img = pygame.image.load(os.path.join("sprites",self.tipo,animation,(str(i)+".png")))
                img = pygame.transform.scale(img, (int(img.get_width() * escala), int(img.get_height() * escala)))
                lista_temporaria.append(img)
            self.animation_list.append(lista_temporaria)

        self.image = self.animation_list[self.action][self.frame_index]
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

        #pular
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True
        
        #aplica gravidade
        self.vel_y += GRAVITY
        #coloca uma velocidade terminal
        if self.vel_y > 10:
            self.vel_y = 10
        
        dy += self.vel_y

        #Checha colisão com o solo
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        #Atualiza a posição do retangulo
        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        # Aqui é o onde é mudado entre os frames da animação do personagem

        # Tempo entre as trocas de imagens
        ANIMATION_COOLDOWN = 100
        #atualiza a imagem dependendo do frame atual
        self.image = self.animation_list[self.action][self.frame_index]
        #checa se passou um tempo suficiente desde a ultima atualização
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            # Volta para o primeiro frame da animação quando passa do ultimo
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0

    def update_action(self, new_action):
        #checa se a nova ação é diferente da antiga
        if new_action != self.action:
            self.action = new_action
            #atualiza as variáveis da atualização
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, tela):
        """
        Desenha o personagem na tela
        :param tela: objeto tela
        :return:
        """
        tela.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
