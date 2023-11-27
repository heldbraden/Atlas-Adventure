import pygame
from Settings import *
from ButtonInfo import Button
from MapSelect import levelSelect

clock = pygame.time.Clock()
fps = 60

scroll = 0
offsetX = 0

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Atlas Adventure')

#Graphics
background = pygame.image.load('../Graphics/BG_Level1.png')
restart1 = pygame.image.load('../Graphics/hud_p3Alt.png')
restart = pygame.transform.scale(restart1, (100, 100))
start = pygame.image.load('../Graphics/hud_p3Alt.png')

pygame.init()

def mainMenu():

    titleFont = pygame.font.Font('../Graphics/SuperComic-qZg62.ttf', 70)
    btnFont = pygame.font.Font('../Graphics/SuperComic-qZg62.ttf', 50)

    while True:
        screen.blit(background, (0, 0))

        mousePos = pygame.mouse.get_pos()

        title = titleFont.render('Atlas Adventure', True, (255, 255, 255))

        playBtn = Button(None, (500, 250), "Play", btnFont, (255, 0, 0), (255, 255, 255))
        quitBtn = Button(None, (500, 310), "Quit", btnFont, (255, 0, 0), (255, 255, 255))

        screen.blit(title, (70, 100))

        for btns in [playBtn, quitBtn]:
            btns.changeColor(mousePos)
            btns.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playBtn.checkForInput(mousePos):
                    levelSelect()
                if quitBtn.checkForInput(mousePos):
                    pygame.quit()

        pygame.display.update()

mainMenu()