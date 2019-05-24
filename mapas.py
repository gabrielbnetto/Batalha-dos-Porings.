import pygame
import time
import math
import random as rd
import Ranking
import time
from monstros import Monster
from players import Player
from imagens import Images
from municao import Bullet
from bombs import Bomb
from ouro import Gold

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000

class Map():

    def __init__(self):
        self.monsters = []
        self.allies = []
        self.bullets = []
        self.bombs = []
        self.pileOfGold = []
        self.level = 1
        self.quant = 1
        self.player = Player((500-70/2, 350-70/2), pygame.image.load('sprites_player/sprite1_player_0.png'))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.images = Images()
        self.bossTime = True
        self.inGame = True
        self.win = False
        self.windowClosed = False
        self.initialScreen = True
        self.intructionsScreen = False
        self.showGuiLevel = True
        self.ranking = []
        self.setRank = True
        self.PauseMusic = False
        self.start_time = time.time()
        self.backgroundIndex = 0
        self.instrucStapoImage = 0
        self.winBackgroundImage = pygame.image.load('background_images/you_win.png')
        self.gameOverBackgroundImage = pygame.image.load('background_images/game_over.jpg')
        self.initialBackgroundImage = pygame.image.load('background_images/initial.jpg')
        self.instructions = pygame.image.load('background_images/instructions.png')
        self.backgrounds = [pygame.image.load('background_images/deserto.png').convert_alpha(), pygame.image.load('background_images/lava.png').convert_alpha(),
                            pygame.image.load('background_images/rocha.png').convert_alpha(), pygame.image.load('background_images/floresta_escura.png').convert_alpha()]
        self.play = pygame.image.load('background_images/play.png')
        self.pause = pygame.image.load('background_images/pause.png')

    def spawnMonsters(self, amount, image, life, isBoss):
        for i in range(amount):
            #monsters spawn at left side
            self.monsters.append(Monster((rd.randint(-(70+(30*amount)), -70), rd.randint(0, 700)), image, life, isBoss))
            #monsters spawn at top side
            self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(-(70+(30*amount)), -70)), image, life, isBoss))
            #monsters spawn at right side
            self.monsters.append(Monster((rd.randint(1070, 1070+(30*amount)), rd.randint(0, 700)), image, life, isBoss))
            #monsters spawn at bot side
            self.monsters.append(Monster((rd.randint(0, 1000), rd.randint(770, 770+(30*amount))), image, life, isBoss))

    def spawnBomb(self):
        self.bombs.append(Bomb((rd.randint(30, 900), rd.randint(30, 600))))

    def spawnGold(self):
        self.pileOfGold.append(Gold((rd.randint(30, 900), rd.randint(30, 600))))

    def spawnBoss(self):
        if self.level <= 5:
            self.spawnMonsters(1, self.images.changeImagesSize(self.images.getRootImages(), (100, 100)), 10, True)
        elif self.level <= 10:
            self.spawnMonsters(1, self.images.changeImagesSize(self.images.getGrizImages(), (100, 100)), 20, True)
        elif self.level <= 15:
            self.spawnMonsters(1, self.images.changeImagesSize(self.images.getAngryPenguinImages(), (100, 100)), 30, True)
        elif self.level <= 20:
            self.spawnMonsters(1, self.images.changeImagesSize(self.images.getStapoImages(), (100, 100)), 40, True)
        
        for i in range(3):
            del self.monsters[rd.randint(0, len(self.monsters)-1)]
        self.monsters[0].changeMonsterVelocity(3)

    def spawnAllies(self, amount, image, life):
        self.allies.append(Monster((rd.randint(0, 1000-30), rd.randint(0,700-30)), image, life, False))

    def spawnBullets(self, amount):
        for i in range(amount):
            self.bullets.append(Bullet())

    def unpauseMusic(self):
        pygame.mixer.music.unpause()
        
    def pauseMusic(self):
        pygame.mixer.music.pause()

    def showPlayerInfos(self):
        #pygame.draw.rect(screen, (0, 0, 0), player1.rect) #debug
        self.screen.blit(self.player.img, self.player.position)
        self.player.showLife(self.screen)
        self.player.showScore(self.screen)
        self.player.showAmmoAmount(self.screen)
        self.player.changeHeartImage()

    def showLevelGUI(self):
        if self.level < 10:
            self.screen.blit(pygame.font.SysFont('arial', 200).render("LEVEL " + str(self.level), True, (0, 0, 0)), (SCREEN_WIDTH/2-(300), SCREEN_HEIGHT/2-150))
        else:
            self.screen.blit(pygame.font.SysFont('arial', 200).render("LEVEL " + str(self.level), True, (0, 0, 0)), (SCREEN_WIDTH/2-(380), SCREEN_HEIGHT/2-150))

    def changeLevel(self):
        self.level += 1
        if self.level <= 5:
            self.backgroundIndex = 0
        elif self.level <= 10:
            self.backgroundIndex = 1
        elif self.level <= 15:
            self.backgroundIndex = 2
        elif self.level <= 20:
            self.backgroundIndex = 3
        else:
            self.inGame = False
            self.win = True
        self.quant += 1
        if (self.quant-1)%5 == 0:
            self.quant = 1
            self.bossTime = True
        #player1.addAmmo(self.level*4+4)
        if self.level <= 5:
            self.spawnMonsters(self.quant, self.images.getStapoImages(), 1, False)
        elif self.level <= 10:
            self.spawnMonsters(self.quant, self.images.getMagmaringImages(), 2, False)
        elif self.level <= 15:
            self.spawnMonsters(self.quant, self.images.getDevelingImages(), 3, False)
        elif self.level <= 20:
            self.spawnMonsters(self.quant, self.images.getPoringImages(), 4, False)
            
        if rd.random() > 0.65:
            self.spawnGold()
            self.spawnAllies(1, self.images.getHeartImages(), 1)
            self.spawnBomb()

        self.showGuiLevel = True
        self.start_time = time.time()


    def blitBackgroundMap(self):
        self.screen.blit(self.backgrounds[self.backgroundIndex], (-13, -30))
        self.screen.blit(self.play, (0, 680))
        self.screen.blit(self.pause, (25, 680))

    def alliesInteractions(self):
        for allie in self.allies:
            allie.drawMonster(self.screen)
            if self.player.is_collided_with(allie):
                if self.PauseMusic == False:
                    allie.healAudio.play()
                self.player.healPlayer(1)
                self.allies.remove(allie)
            else:
                for shot in self.player.shots:
                    if shot.is_collided_with(allie):
                        allie.damageMonster(1)
                        if allie.isDead(self.PauseMusic):
                            self.allies.remove(allie)
                            self.player.addScore(-500)
                        self.player.shots.remove(shot)

    def bombInteractions(self):
        for bomb in self.bombs:
            bomb.drawBomb(self.screen)
            if self.player.is_collided_with(bomb):
                self.bombs.remove(bomb)
                if(self.PauseMusic == False):
                    pygame.mixer.Sound('audio/explosion.wav').play()

    def goldInteractons(self):
        for gold in self.pileOfGold:
            gold.drawGold(self.screen)
            if self.player.is_collided_with(gold):
                self.player.addScore(250)
                self.pileOfGold.remove(gold)
                if(self.PauseMusic == False):
                    pygame.mixer.Sound('audio/gold.wav').play()
            else:
                for shot in self.player.shots:
                    if shot.is_collided_with(gold):
                        self.pileOfGold.remove(gold)
                        self.player.shots.remove(shot)

    def monstersInteractions(self):
        for monster in self.monsters:
            monster.move(self.player)
            monster.drawMonster(self.screen)
            monster.drawLifeBar(monster, self.screen)
            if self.player.is_collided_with(monster):
                if self.PauseMusic == False:
                    monster.damageAudio.play()
                if monster.isBoss:
                    self.player.damagePlayer(5)
                else:
                    self.player.damagePlayer(1)
                self.monsters.remove(monster)
                if(self.player.isPlayerDead()):
                    self.inGame = False
            else:
                for shot in self.player.shots:
                    if shot.is_collided_with(monster):
                        monster.damageMonster(1)
                        if monster.isDead(self.PauseMusic):
                            self.monsters.remove(monster)
                            self.player.addScore(100)
                        self.player.shots.remove(shot)

    def bulletsInteractions(self):
        for bullet in self.bullets:
            self.screen.blit(bullet.img, bullet.position)
            if self.player.is_collided_with(bullet):
                if(self.PauseMusic == False):
                    bullet.reloadAudio.play()
                self.player.addAmmo(5)
                self.bullets.remove(bullet)
                if len(self.bullets) == 0:
                    self.player.canSpawnBullets = True

    def shotsInteractions(self):
        for shot in self.player.shots:
            shot.move()
            self.screen.blit(shot.img, shot.position)
            if shot.position[0] > SCREEN_WIDTH or shot.position[0] < 0:
                self.player.shots.remove(shot)
            elif shot.position[1] > SCREEN_HEIGHT or shot.position[1] < 0:
                self.player.shots.remove(shot)

    def checkEvents(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.grau = 0
            self.player.moveUp()
            self.player.passo += 1
        elif keys[pygame.K_DOWN]:
            self.player.grau = 180
            self.player.moveDown()
            self.player.passo += 1
        elif keys[pygame.K_RIGHT]:
            self.player.grau = 90
            self.player.moveRight()
            self.player.passo += 1
        elif keys[pygame.K_LEFT]:
            self.player.grau = 270
            self.player.moveLeft()
            self.player.passo += 1
        elif keys[pygame.K_q]:
            print('Q PRESSED')
            for m in self.monsters:
                self.monsters.remove(m)
                self.player.addScore(200)
            for a in self.allies:
                self.allies.remove(a)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot(self)
                if event.key == pygame.K_p:
                    self.monsters = []
                    self.allies = []
                    self.level += 3
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0] >= 25 and pos[0] <= 45 and pos[1] >= 680 and pos[1] <= 700):
                    self.pauseMusic()
                    self.PauseMusic = True
                if(pos[0] >= 0 and pos[0] <= 20 and pos[1] >= 680 and pos[1] <= 700):
                    self.PauseMusic = False
                    self.unpauseMusic()

    def checkEndOfLevel(self):
        if len(self.monsters) == 0 and len(self.allies) == 0 and self.inGame:
            if self.level%5 == 0 and self.bossTime:
                self.spawnBoss()
                self.bossTime = False
            else:
                self.changeLevel()

    def showGuiLevelMap(self):
        if self.showGuiLevel:
            if time.time() - self.start_time > 2.2:
                self.showGuiLevel = False
            self.showLevelGUI()

    def endOfGame(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0] >= 25 and pos[0] <= 45 and pos[1] >= 680 and pos[1] <= 700):
                    self.PauseMusic = True
                    self.pauseMusic()
                if(pos[0] >= 0 and pos[0] <= 20 and pos[1] >= 680 and pos[1] <= 700):
                    self.PauseMusic = False
                    self.unpauseMusic()
                    
        if self.win:
            self.screen.blit(self.winBackgroundImage, (0, 0))
            self.screen.blit(self.play, (0, 680))
            self.screen.blit(self.pause, (25, 680))
            self.screen.blit(pygame.font.SysFont('arial', 45).render("Parabéns " + Ranking.GetUsername(), True, (255, 255, 255)), (50, 600))
        else: 
            self.screen.blit(self.gameOverBackgroundImage, (0, 0))
            self.screen.blit(self.play, (0, 680))
            self.screen.blit(self.pause, (25, 680))
            count = 1
            for score in self.ranking:
                self.screen.blit(pygame.font.SysFont('arial', 45).render(str(count) + " Lugar - " + score[1] + " - Level: " + score[2] + " - Score: " + score[3] , True, (255, 255, 255)), (150, 170 + (70*count)))
                count += 1
                if count > 5: break
        if self.setRank:    
            Ranking.SetRank(self.player.score, self.level, Ranking.GetUsername())
            Ranking.LoadRanking()
            self.ranking = Ranking.GetRanking()
            self.setRank = False

        pygame.display.update()

    def initalScreen(self):
        self.screen.blit(self.initialBackgroundImage, (0, 0))
        self.screen.blit(self.play, (0, 680))
        self.screen.blit(self.pause, (25, 680))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0] >= 250 and pos[0] <= 440 and pos[1] >= 650 and pos[1] <= 695):
                    self.initialScreen = False
                if(pos[0] >= 485 and pos[0] <= 735 and pos[1] >= 650 and pos[1] <= 695):
                    self.initialScreen = False
                    self.intructionsScreen = True
                if(pos[0] >= 25 and pos[0] <= 45 and pos[1] >= 650 and pos[1] <= 700):
                    self.PauseMusic = True
                    self.pauseMusic()
                if(pos[0] >= 0 and pos[0] <= 20 and pos[1] >= 680 and pos[1] <= 700):
                    self.PauseMusic = False
                    self.unpauseMusic()

    def instructionScreen(self):
        self.screen.blit(self.instructions, (0, 0))
        if(self.instrucStapoImage == 13):
            self.instrucStapoImage = 0
        stapos = [pygame.transform.scale(pygame.image.load('sprites_monsters/stapo/right/frame_' + str(i) + '_delay-0.1s.png'), (60, 60)) for i in range(13)]
        self.screen.blit(stapos[self.instrucStapoImage],(450,350))
        self.instrucStapoImage+=1
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inGame = False
                self.windowClosed = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0] >= 410 and pos[0] <= 540 and pos[1] >= 630 and pos[1] <= 690):
                    self.intructionsScreen = False
                if(pos[0] >= 25 and pos[0] <= 45 and pos[1] >= 650 and pos[1] <= 700):
                    self.pauseMusic()
                    self.PauseMusic = True
                if(pos[0] >= 0 and pos[0] <= 20 and pos[1] >= 680 and pos[1] <= 700):
                    self.unpauseMusic()
                    self.PauseMusic = False
