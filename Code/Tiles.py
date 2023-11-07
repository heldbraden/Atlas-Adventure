import pygame

#Create Tile
class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()

        #Determine size of a tile
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = (x, y))

    #Update camera on nonstatic levels
    def update(self, shift):
        self.rect.x += shift

class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface