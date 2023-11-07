import pygame, sys
from TestLevel import Level
from TestLevelInfo import testLevel1
from Settings import *

#Setup:
pygame.init()

#Screen:
pygame.display.set_caption('Atlas Adventure')
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

#Clock:
clock = pygame.time.Clock()

#Level:
level = Level(testLevel1, screen)
levelScreen = screen.copy()

#Main Game Loop:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            screen.blit(pygame.transform.scale(levelScreen, event.dict['size']), (0, 0))
    
    screen.fill((255, 255, 255)
    level.run()

    pygame.display.update()
    clock.tick(60)
