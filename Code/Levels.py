world1_level1 = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,40,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,25,44,-1,-1,-1,-1,128,103,104,-1,-1,-1,-1,-1,-1,24,-1,-1,-1,40,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,44,40,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,128,103,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,32,103,103,103,103,103,104,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,40,-1,-1,-1,-1,-1,-1,128,103,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,25,-1,-1,-1,-1,-1,32,20,152,152,152,-1,-1,-1,-1,-1,-1],
    [-1,33,-1,40,-1,32,103,103,103,8,-1,-1,40,-1,-1,24,-1,124,124,124,-1,-1,124,124,124,-1,-1,-1,-1,24,-1,40,132,144,132,44,-1,-1,32,20,152,152,152,152,-1,27,-1,40,-1,-1],
    [103,103,103,103,103,20,152,152,152,151,103,103,103,103,103,103,103,103,102,102,102,102,102,102,103,103,103,103,103,103,103,103,103,103,103,103,103,103,20,152,152,152,152,151,103,103,103,103,103,103],
]

import pygame
from Settings import *
from Game import levels

class Level:
    def __init__(self, currentLevel, surface, createOverworld):
        self.displaySurface = surface
        self.currentLevel = currentLevel
        levelData = levels[currentLevel]
        levelContent = levelData['content']
        self.newMaxLevel = levelData['unlock']
        self.createOverworld = createOverworld

        self.font = pygame.font.Font(None, 40)
        self.textSurface = self.font.render(levelContent, True, (255, 255, 255))
        self.textRect = self.textSurface.get_rect(center = (screenWidth // 2, screenHeight // 2))

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            self.createOverworld(self.currentLevel, self.newMaxLevel)
        if keys[pygame.K_ESCAPE]:
            self.createOverworld(self.currentLevel, 0)

    def run(self):
        self.input()
        self.displaySurface.blit(self.textSurface, self.textRect)