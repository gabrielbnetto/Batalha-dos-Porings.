import pygame
import random as rd

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000

class Bullet():

    def __init__(self):
        self.position = (rd.randint(0, SCREEN_WIDTH-30), rd.randint(0, SCREEN_HEIGHT-30))
        self.img = pygame.image.load('sprites_player/bullets.png')
        self.rect = pygame.Rect(self.position[0], self.position[1], self.img.get_width(), self.img.get_height())
        self.reloadAudio = pygame.mixer.Sound('audio/reload.wav')
