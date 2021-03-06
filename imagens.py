import pygame

class Images():

    def __init__(self):
        self.poring = [[pygame.image.load('sprites_monsters/poring/right/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)],
                       [pygame.image.load('sprites_monsters/poring/left/frame_' + str(i) + '_delay-0.1s.png') for i in range(10)]]

        self.heart = [[pygame.transform.scale(pygame.image.load('sprites_player/heart.png'), (30,30))], [pygame.transform.scale(pygame.image.load('sprites_player/heart.png'), (30,30))]]

        self.stapo = [[pygame.transform.scale(pygame.image.load('sprites_monsters/stapo/right/frame_' + str(i) + '_delay-0.1s.png'), (60, 60)) for i in range(13)],
                      [pygame.transform.scale(pygame.image.load('sprites_monsters/stapo/left/frame_' + str(i) + '_delay-0.1s.png'), (60, 60)) for i in range(13)]]

        self.magmaring = [[pygame.transform.scale(pygame.image.load('sprites_monsters/magmaring/right/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(4)],
                         [pygame.transform.scale(pygame.image.load('sprites_monsters/magmaring/left/frame_' + str(i) + '_delay-0.1s.png'),(80, 80)) for i in range(4)]]

        self.develing = [[pygame.transform.scale(pygame.image.load('sprites_monsters/develing/right/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(7)],
                         [pygame.transform.scale(pygame.image.load('sprites_monsters/develing/left/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(7)]]

        self.root = [[pygame.transform.scale(pygame.image.load('sprites_monsters/root_of_corruption/right/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(4)],
                     [pygame.transform.scale(pygame.image.load('sprites_monsters/root_of_corruption/left/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(4)]]

        self.griz = [[pygame.transform.scale(pygame.image.load('sprites_monsters/griz/right/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(6)],
                     [pygame.transform.scale(pygame.image.load('sprites_monsters/griz/left/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(6)]]

        self.angry_penguin = [[pygame.transform.scale(pygame.image.load('sprites_monsters/angry_penguin/right/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(9)],
                     [pygame.transform.scale(pygame.image.load('sprites_monsters/angry_penguin/left/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(9)]]

        self.king_poring = [[pygame.transform.scale(pygame.image.load('sprites_monsters/king_poring/right/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(7)],
                     [pygame.transform.scale(pygame.image.load('sprites_monsters/king_poring/left/frame_' + str(i) + '_delay-0.1s.png'), (80, 80)) for i in range(7)]]


    def getPoringImages(self):
        return self.poring

    def getHeartImages(self):
        return self.heart

    def getAquaringImages(self):
        return self.aquaring

    def getPoporingImages(self):
        return self.poporing

    def getStapoImages(self):
        return self.stapo

    def getMetallingImages(self):
        return self.metalling

    def getMagmaringImages(self):
        return self.magmaring

    def getDevelingImages(self):
        return self.develing

    def getRootImages(self):
        return self.root

    def getGrizImages(self):
        return self.griz

    def getAngryPenguinImages(self):
        return self.angry_penguin

    def getKingPoringImages(self):
        return self.king_poring

    def changeImagesSize(self, images, size):
        return [[pygame.transform.scale(images[0][i], size) for i in range(len(images[0]))], [pygame.transform.scale(images[1][i], size) for i in range(len(images[1]))]]
