import pygame
from Support import importCSV, importTileGraphics
from Settings import tileSize
from Tiles import StaticTile
from Player import Character

class Level:
    def __init__(self, levelData, surface):
        self.display_surface = surface
        self.camera = 0

        #Get level layout from CSV file
        levelLayout = importCSV(levelData['Ground'])

        #Add level to sprites
        self.groundSprites = self.createLevel(levelLayout, 'ground')

    #Create level
    def createLevel(self, layout, type):
        spriteGroup = pygame.sprite.Group()
        self.character = pygame.sprite.GroupSingle()

        #Go through rows of CSV
        for rowIndex, row in enumerate(layout):

            #Go through cols of CSV and determine its tile value
            for colIndex, val in enumerate(row):

                #Get x and y position based on size of tile
                x = colIndex * tileSize
                y = rowIndex * tileSize

                #-1 value is an empty tile
                if val != '-1':

                    #Check values of CSV and add correct tile from tileset
                    if (type == 'ground'):
                        groundTileList = importTileGraphics('../Graphics/TilesetTest.png')
                        tileSurface = groundTileList[int(val)]
                        tileSprite = StaticTile(tileSize, x, y, tileSurface)
                        spriteGroup.add(tileSprite)

        #Position Character at beginning of level
        characterSprite = Character((16, 152))
        self.character.add(characterSprite)

        return spriteGroup

    #Run entire level
    def run(self):

        #Draw and Update Tiles:
        self.groundSprites.draw(self.display_surface)
        self.groundSprites.update(self.camera)

        #Draw and Update Character:
        self.character.update()
        self.character.draw(self.display_surface)