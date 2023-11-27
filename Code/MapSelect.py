import pygame
from Settings import *
from ButtonInfo import Button
from Level1 import playLvl1
from Level2 import playLvl2
from Level3 import playLvl3

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Atlas Adventure')

#Graphics
background = pygame.image.load('../Graphics/BG_Level1.png')

def levelSelect():

    pygame.init()
    
    screen.blit(background, (0, 0))
    btnFont = pygame.font.Font('../Graphics/SuperComic-qZg62.ttf', 50)
    title = btnFont.render('Level Select', True, (255, 255, 255))
    screen.blit(title, (280, 100))

    lvl1 = pygame.image.load('../Graphics/bush.png')
    scale1 = pygame.transform.scale(lvl1, (100, 100))
    lvl2 = pygame.image.load('../Graphics/caneRedSmall.png')
    scale2 = pygame.transform.scale(lvl2, (100, 100))
    lvl3 = pygame.image.load('../Graphics/snowBallBig.png')
    scale3 = pygame.transform.scale(lvl3, (100, 100))

    while True:

        mousePos = pygame.mouse.get_pos()

        lvl1Btn = Button(scale1, (295, screenHeight // 2), "", btnFont, (255, 0, 0), (255, 255, 255))
        lvl2Btn = Button(scale2, (490, screenHeight // 2), "", btnFont, (255, 0, 0), (255, 255, 255))
        lvl3Btn = Button(scale3, (685, screenHeight // 2), "", btnFont, (255, 0, 0), (255, 255, 255))

        for btns in [lvl1Btn, lvl2Btn, lvl3Btn]:
            btns.changeColor(mousePos)
            btns.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1Btn.checkForInput(mousePos):
                    playLvl1()
                if lvl2Btn.checkForInput(mousePos):
                    playLvl2()
                if lvl3Btn.checkForInput(mousePos):
                    playLvl3()

        pygame.display.update()