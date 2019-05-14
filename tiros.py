import pygame

class Shot():

    def __init__(self, position, eixo, vel, grau):
        self.position = position
        self.eixo = eixo
        self.grau = grau
        if eixo == 'x' and grau == 90:
            self.img = pygame.image.load('sprites_player/shotX.png')
        elif eixo == 'x' and grau == 270:
            self.img = pygame.image.load('sprites_player/shotX2.png')
        elif eixo == 'y' and grau == 0:
            self.img = pygame.image.load('sprites_player/shotY.png')
        elif eixo == 'y' and grau == 180:
            self.img = pygame.image.load('sprites_player/shotY2.png')
        
        self.rect = pygame.Rect(position[0], position[1], self.img.get_width(), self.img.get_height())
        self.vel = vel * 30

    def move(self):
        if self.eixo == 'x':
            self.position = (self.position[0]+self.vel, self.position[1])
            self.rect.x += self.vel
        else:
            self.position = (self.position[0], self.position[1]+self.vel)
            self.rect.y += self.vel

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)
