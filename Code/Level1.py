import pygame
from Levels import world1_level1
from Settings import *
from ButtonInfo import Button
#from Main import mainMenu

clock = pygame.time.Clock()
fps = 60

scroll = 0
offsetX = 0

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Atlas Adventure')

#Graphics
background = pygame.image.load('../Graphics/BG_Level1.png')

def playLvl1():

    gameOver = 0

    pygame.init()

    def draw_grid():
        for c in range(14):
            #vertical lines
            pygame.draw.line(screen, (255, 255, 255), (c * tileSize, 0), (c * tileSize, screenHeight))
            #horizontal lines
            pygame.draw.line(screen, (255, 255, 255), (0, c * tileSize), (screenWidth, c * tileSize))

    class Player():
        def __init__(self, x, y):
            self.reset(x, y)
        
        def update(self, gameOver):

            global offsetX

            dx = 0
            dy = 0
            walkSpeed = 5

            if gameOver == 0:
                key = pygame.key.get_pressed()
                if key[pygame.K_LEFT]:
                    dx -= 5
                    self.counter += 1
                    self.direction = -1
                    offsetX -= 10
                if key[pygame.K_RIGHT]:
                    dx += 5
                    self.counter += 1
                    self.direction = 1
                    offsetX += 10

                if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                    self.counter = 0
                    self.index = 0
                    self.image = pygame.image.load('../Graphics/p3_front.png')

                #Can only jump Once
                if key[pygame.K_UP] and self.jumped == False and self.air == False:
                    self.vel = -20
                    self.jumped = True
                    self.image = pygame.image.load('../Graphics/p3_jump.png')
                if key[pygame.K_UP] == False:
                    self.jumped = False

                #Animation
                if self.counter >= walkSpeed:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.imagesRight):
                        self.index = 0
                    if self.direction == 1:
                        self.image = self.imagesRight[self.index]
                    if self.direction == -1:
                        self.image = self.imagesLeft[self.index]

                #Gravity
                self.vel += 1
                if self.vel > 10:
                    self.vel = 10

                #Velocity for upward movement
                dy += self.vel

                self.air = True
                for tile in world1.tileList:
                    #X Collisions
                    if tile[1].colliderect(self.rect.x + dx + offsetX, self.rect.y, self.width, self.height):
                        dx = 0
                    
                    #Y Collisions
                    if tile[1].colliderect(self.rect.x + offsetX, self.rect.y + dy, self.width, self.height):
                        #Jump
                        if self.vel < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel = 0

                        #Falling
                        elif self.vel >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel = 0
                            self.air = False

                if pygame.sprite.spritecollide(self, waterGroup, False):
                    gameOver = -1
                    
                if self.rect.y > screenHeight:
                    gameOver = -1

                #Update Player Posistion
                #self.rect.x += dx
                self.rect.y += dy

            screen.blit(self.image, self.rect)
            #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

            return gameOver
        
        def reset(self, x, y):
            #List of images for walking
            self.imagesRight = []
            self.imagesLeft = []
            self.index = 0
            self.counter = 0
            for num in range (1, 12):
                imgRight = pygame.image.load(f'../Graphics/p3_walk/p3_walk{num}.png')
                imgLeft = pygame.transform.flip(imgRight, True, False)
                self.imagesRight.append(imgRight)
                self.imagesLeft.append(imgLeft)

            self.image = self.imagesRight[self.index]

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y    
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel = 0
            self.jumped = False
            self.direction = 0
            self.air = True

    class WorldCreation():    
        def __init__(self, data):
            self.reset(data)

        def draw(self):
            for tile in self.tileList:
                tile[1].x -= offsetX
                screen.blit(tile[0], tile[1])
                tile[1].x += offsetX
                #pygame.draw.rect(screen, (255, 0, 0), tile[1], 2)

            for waterTile in waterGroup:
                waterTile.rect.x -= offsetX
                screen.blit(waterTile.image, waterTile.rect)
                waterTile.rect.x += offsetX

            for finishTile in finishGroup:
                finishTile.rect.x -= offsetX
                screen.blit(finishTile.image, finishTile.rect)
                finishTile.rect.x += offsetX

            for coinTile in coinGroup:
                coinTile.rect.x -= offsetX
                screen.blit(coinTile.image, coinTile.rect)
                coinTile.rect.x += offsetX

        def reset(self, data):
            self.tileList = []
                
            #Tiles
            grass = pygame.image.load('../Graphics/grassMid.png')
            dirt = pygame.image.load('../Graphics/grassCenter.png')
            hillUp = pygame.image.load('../Graphics/grassHillLeft.png')
            hillDown = pygame.image.load('../Graphics/grassHillRight.png')
            hillUpDirt = pygame.image.load('../Graphics/grassHillLeft2.png')
            hillDownDirt = pygame.image.load('../Graphics/grassHillRight2.png')
            #water = pygame.image.load('../Graphics/liquidWaterTop_mid.png')
            bridge = pygame.image.load('../Graphics/bridgeLogs.png')
            #coins = pygame.image.load('../Graphics/coinGold.png')
            #flag = pygame.image.load('../Graphics/flagRed.png')
            islandLeft = pygame.image.load('../Graphics/grassCliffLeft.png')
            islandRight = pygame.image.load('../Graphics/grassCliffRight.png')


            #Add Tiles to Level
            rowCount = 0
            for row in data:
                colCount = 0
                for tile in row:
                    if tile == 103:
                        img = pygame.transform.scale(grass, (tileSize, tileSize))
                        imgRect = img.get_rect()    
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    if tile == 152:
                        img = pygame.transform.scale(dirt, (tileSize, tileSize))
                        imgRect = img.get_rect()    
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    if tile == 20:
                        img = pygame.transform.scale(hillUpDirt, (tileSize, tileSize))
                        imgRect = img.get_rect()    
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    if tile == 32:
                        img = pygame.transform.scale(hillUp, (tileSize, tileSize))
                        imgRect = img.get_rect()    
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    if tile == 8:
                        img = pygame.transform.scale(hillDown, (tileSize, tileSize))
                        imgRect = img.get_rect()    
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    if tile == 151:
                        img = pygame.transform.scale(hillDownDirt, (tileSize, tileSize))
                        imgRect = img.get_rect()    
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    if tile == 128:
                        img = pygame.transform.scale(islandLeft, (tileSize, tileSize))
                        imgRect = img.get_rect()    
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    if tile == 104:
                        img = pygame.transform.scale(islandRight, (tileSize, tileSize))
                        imgRect = img.get_rect()    
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    if tile == 102:
                        waterTile = Water(colCount * tileSize, rowCount * tileSize)
                        waterGroup.add(waterTile)
                    if tile == 124:
                        img = pygame.transform.scale(bridge, (tileSize, tileSize))
                        imgRect = img.get_rect()
                        imgRect.x = colCount * tileSize
                        imgRect.y = rowCount * tileSize
                        tile = (img, imgRect)
                        self.tileList.append(tile)
                    if tile == 44:
                        coinTile = Coin(colCount * tileSize, rowCount * tileSize)
                        coinGroup.add(coinTile)
                    if tile == 27:
                        finishTile = Finish(colCount * tileSize, rowCount * tileSize)
                        finishGroup.add(finishTile)
                    colCount += 1
                rowCount += 1

    class Water(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('../Graphics/liquidWaterTop_mid.png')
            self.image = pygame.transform.scale(img, (tileSize, tileSize))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Finish(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('../Graphics/flagRed.png')
            self.image = pygame.transform.scale(img, (tileSize, tileSize))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Coin(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('../Graphics/coinGold.png')
            self.image = pygame.transform.scale(img, (tileSize, tileSize))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    #World
    player = Player(350, 200)
    waterGroup = pygame.sprite.Group()
    finishGroup = pygame.sprite.Group()
    coinGroup = pygame.sprite.Group()
    world1 = WorldCreation(world1_level1)

    run = True
    while run:

        mousePos = pygame.mouse.get_pos()

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(background, (0, 0))

        world1.draw()

        waterGroup.draw(screen)

        gameOver = player.update(gameOver)

        if gameOver == -1:

            btnFont = pygame.font.Font('../Graphics/SuperComic-qZg62.ttf', 50)
            gameOverBtn = Button(None, (500, 250), "Game Over", btnFont, (255, 0, 0), (255, 255, 255))

            gameOverBtn.changeColor(mousePos)
            gameOverBtn.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if gameOverBtn.checkForInput(mousePos):
                        #mainMenu()
                        gameOver = 0

        #draw_grid()
        pygame.display.update()

    pygame.quit()