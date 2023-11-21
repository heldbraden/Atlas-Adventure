import pygame
from Game import levels

class Node(pygame.sprite.Sprite):
    def __init__(self, pos, status):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        if status == 'available':
            self.image.fill((0, 255, 0))
        else:
            self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center = pos)

class Icon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center = pos)


class Overworld:
    def __init__(self, startLevel, maxLevel, surface, createLevel):
        self.displaySurface = surface
        self.maxLevel = maxLevel
        self.currentLevel = startLevel
        self.createLevel = createLevel

        self.moved = False

        self.setupNodes()
        self.setupIcon()

    def setupNodes(self):
        self.nodes = pygame.sprite.Group()

        for index, nodeData in enumerate(levels.values()):
            if index <= self.maxLevel:
                nodeSprite = Node(nodeData['nodePos'], 'available')
                self.nodes.add(nodeSprite)
            else:
                nodeSprite = Node(nodeData['nodePos'], 'locked')
                self.nodes.add(nodeSprite)

    def drawPaths(self):
        points = [node['nodePos'] for node in levels.values()]
        pygame.draw.lines(self.displaySurface, (0, 255, 0), False, points, 6)

    def setupIcon(self):
        self.icon = pygame.sprite.GroupSingle()
        iconSprite = Icon(self.nodes.sprites()[self.currentLevel].rect.center)
        self.icon.add(iconSprite)

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.moved:
            if keys[pygame.K_RIGHT]and self.currentLevel < self.maxLevel:
                self.currentLevel += 1
                self.moved = True
            elif keys[pygame.K_LEFT] and self.currentLevel > 0:
                self.currentLevel -= 1
                self.moved = True
            elif keys[pygame.K_UP]:
                self.createLevel(self.currentLevel)

    def updateIconPos(self):
        self.icon.sprite.rect.center = self.nodes.sprites()[self.currentLevel].rect.center
        self.moved = False

    def run(self):
        self.input()
        self.drawPaths()
        self.updateIconPos()
        self.nodes.draw(self.displaySurface)
        self.icon.draw(self.displaySurface)