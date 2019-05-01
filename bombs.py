import pygame
import random as rd

class Bomb():

    def __init__(self, position):
        self.img = pygame.transform.scale(pygame.image.load('sprites_player/bomb.png'), (30,30))
        self.position = position
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()
        self.rect = pygame.Rect(position[0] + 5, position[1] + 5, self.img_width - 10, self.img_height - 10)
        self.radius = 300

    def drawBomb(self, screen):
        screen.blit(self.img, self.position)
