import pygame

#Create character
class Character(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        #Testing purposes, will add sprite and animation later
        self.image = pygame.Surface((8, 16))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(topleft = pos)
