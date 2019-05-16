import pygame
import random as rd

class Gold():

    def __init__(self, position):
        self.imgIndex = 0
        self.img = pygame.transform.scale(pygame.image.load('sprites_player/gold.png'), (65,30)) 
        self.position = position
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()
        self.rect = pygame.Rect(position[0] + 5, position[1] + 5, self.img_width - 10, self.img_height - 10)
        self.radius = 300

    def drawGold(self, screen):
        screen.blit(self.img, self.position)
        
 
