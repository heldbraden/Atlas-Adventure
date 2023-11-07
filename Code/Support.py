import pygame
from csv import reader
from Settings import tileSize

#Get level information from CSV
def importCSV(path):

    groundMap = []
    with open(path) as map:

        #Get value from file
        level = reader(map, delimiter = ',')

        #Loop through values and add them to map
        for i in level:
            groundMap.append(list(i))

        return groundMap
    
#Get tile graphics from tileset
def importTileGraphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tileX = int(surface.get_size()[0] / tileSize)
    tileY = int(surface.get_size()[1] / tileSize)

    seperatedTiles = []

    for row in range(tileY):
        for col in range(tileX):
            x = col * tileSize
            y = row * tileSize
            newSurface = pygame.Surface((tileSize, tileSize))
            newSurface.blit(surface, (0, 0), pygame.Rect(x, y, tileSize, tileSize))
            seperatedTiles.append(newSurface)

    return seperatedTiles