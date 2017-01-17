#import required modules
import pygame
import time
#define colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

#dimensies van het scherm
width = 800
heigth = 600
size = (width,heigth)

#laden en invoegen van achtergrond sprite
class Game():
    def __init__(self):
        #standard initialisation of pygame
        pygame.init()

        #Weergaven van het scherm
        self.screen = pygame.display.set_mode(size)

        #initialize intro_menu
        self.intro_game = IntroGame()

    def visual_display(self):
        #aangeven van naam van het spel
        pygame.display.set_caption("Shipwars: Informatica Editon")

        #visuals van intro screen
        self.intro_game.visual_display(self.screen)

        #updaten van visueele aspecten
        pygame.display.flip()


    #loop voor het laten runnen van het spel
    def loop_of_game(self):
        while not Close_game():
            self.visual_display()


class IntroGame:
    def __init__(self):
        # sprites
        self.bg = pygame.image.load("bg.jpg")
        self.bg = pygame.transform.scale(self.bg, size)
        self.pbuttom = pygame.image.load("play-buttom1.png")
        self.pbuttom = pygame.transform.scale(self.pbuttom, [300, 250])
        self.hbuttom = pygame.image.load("high-buttom1.png")
        self.hbuttom = pygame.transform.scale(self.hbuttom, [300, 250])
        self.title = pygame.image.load("title.png")
        self.title = pygame.transform.scale(self.title,[heigth,200])

    def visual_display(self,screen):

        screen.blit(self.bg,[0,0])
        screen.blit(self.title,(heigth/5,100))
        screen.blit(self.pbuttom,(heigth/6,width/2))
        screen.blit(self.hbuttom,(heigth/2+150,width/2))
        pygame.display.flip()


class GameMain:
    def __init__(self):
        # sprites
        pass

class Higscorelist:
    def __init__(self):
        # sprites
        pass
class GamerulesList:
    def __init__(self):
        # sprites
        pass

class PauseMenu:
    def __init__(self):
        # sprites
        pass

def text_objects(text,font):
    textSurface = font.render (text,True, black)
    return textSurface, textSurface.get_rect()


def message_to_screen(text):
    largeText = pygame.font.Font("freesansbold.ttf",50)
    textsuf , textrect = text_objects(text,largeText)
    textrect.center = ((width/2),(heigth/2))


#sluiten van game via kruisje
def Close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def run ():
    game = Game()
    game.loop_of_game()

run()
