
import pygame
from pygame.locals import *
import time
#define colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

width = 1200
heigth = 800
size = (width,heigth)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Shipwars Informatica Editon")
        self.intro_game = IntroGame(self)
        self.game_main= GameMain(self)
        self.pause_menu = PauseMenu(self)
        self.Boats = Boats(width*0.22,heigth*0.2,"boat","battleship.png")
        self.Boats1 = Boats(width*0.22, heigth * 0.4, "boat1", "battleship1.png")
        self.Boats2 = Boats(width*0.22, heigth * 0.6, "boat2", "battleship2.png")
        self.state = self.intro_game

    def set_state(self, state):
        self.state = state

    def update(self):
        self.Boats1.update()
        self.game_main.update()

    def draw(self):
        self.state.draw(self.screen)

        if self.state == self.game_main:
            self.Boats1.draw(self.screen)

        pygame.display.flip()


    #loop voor het laten runnen van het spel
    def loop_of_game(self):
        while not Close_game(self.screen):
            self.update()
            self.draw()

class Boats:
    def __init__(self,x,y,naam,image):
        self.x = x
        self.y = y
        self.block_size = 33.5
        self.block_size_up_down = 39.9
        self.naam = naam
        self.naam = pygame.image.load(image)
        self.naam = pygame.transform.scale(self.naam, [30,100])

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.block_size
        elif keys [pygame.K_RIGHT]:
            self.x += self.block_size

        if keys[pygame.K_UP]:
            self.y -= self.block_size_up_down
        elif keys[pygame.K_DOWN]:
            self.y += self.block_size_up_down

        if self.x < width*0.22:
            self.x = width*0.22
        elif self.y < 0:
            self.y = 0
        if self.x > 905:
            self.x = 905



    def draw(self,screen):
        screen.blit(self.naam,[self.x,self.y])

class IntroGame:
    def __init__(self, game):
        # sprites
        self.game = game
        self.bg = pygame.image.load("bg.jpg")
        self.bg = pygame.transform.scale(self.bg, size)
        self.pbuttom = pygame.image.load("Play.png")
        self.pbuttom = pygame.transform.scale(self.pbuttom, [300, 150])
        self.hbuttom = pygame.image.load("hscore.png")
        self.hbuttom = pygame.transform.scale(self.hbuttom, [350, 100])
        self.rbuttom = pygame.image.load("Instrutions.png")
        self.rbuttom = pygame.transform.scale(self.rbuttom, [350, 150])
        self.title = pygame.image.load("title.png")
        self.title = pygame.transform.scale(self.title,[heigth,200])
        self.hoover = pygame.image.load("hoover_image.png")
        self.hoover = pygame.transform.scale(self.hoover, [320, 160])
        self.hoover1 = pygame.image.load("hoover_image.png")
        self.hoover1 = pygame.transform.scale(self.hoover, [370, 120])


    def draw(self,screen):
        screen.blit(self.bg,[0,0])
        screen.blit(self.title,(width/5,width/8))
        mouse_button_pressed(450, 400, 300, 150, screen, self.pbuttom, self.hoover, lambda: self.game.set_state(self.game.game_main))
        mouse_button_pressed(750, 625, 300, 150, screen, self.hbuttom, self.hoover1)
        mouse_button_pressed(150, 600, 300, 150, screen, self.rbuttom, self.hoover1)

class GameMain:
    def __init__(self, game):
        self.pause_menu = PauseMenu(self)
        self.game = game
        self.board = pygame.image.load("board.jpg")
        self.board = pygame.transform.scale(self.board,(size))
        self.pbutton = pygame.image.load("menu.png")
        self.pbutton = pygame.transform.scale(self.pbutton, [50, 50])
        self.hoover = pygame.image.load("hoover_image.png")
        self.hoover = pygame.transform.scale(self.hoover, [60, 60])


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game.set_state(self.game.pause_menu)

    def draw(self,screen):
        screen.blit(self.board,[0,0])
        mouse_button_pressed(10, 10, 50, 50, screen, self.pbutton, self.hoover,lambda: self.game.set_state(self.game.pause_menu))

class PauseMenu:
    def __init__(self, game):
        # sprites
        self.game = game
        self.bg = pygame.image.load("bg.jpg")
        self.bg = pygame.transform.scale(self.bg, size)
        self.pbuttom = pygame.image.load("Play.png")
        self.pbuttom = pygame.transform.scale(self.pbuttom, [300, 150])
        self.hbuttom = pygame.image.load("hscore.png")
        self.hbuttom = pygame.transform.scale(self.hbuttom, [350, 100])
        self.rbuttom = pygame.image.load("Instrutions.png")
        self.rbuttom = pygame.transform.scale(self.rbuttom, [350, 150])
        self.title = pygame.image.load("title.png")
        self.title = pygame.transform.scale(self.title,[heigth,200])
        self.hoover = pygame.image.load("hoover_image.png")
        self.hoover = pygame.transform.scale(self.hoover, [320, 160])
        self.hoover1 = pygame.image.load("hoover_image.png")
        self.hoover1 = pygame.transform.scale(self.hoover, [370, 120])

    def draw(self,screen):
        screen.blit(self.title,(width/5,width/8))
        mouse_button_pressed(450, 400, 300, 150, screen, self.pbuttom, self.hoover, lambda: self.game.set_state(self.game.game_main))
        mouse_button_pressed(750, 625, 300, 150, screen, self.hbuttom, self.hoover1, lambda :self.game.set_state(self.game.intro_game))
        mouse_button_pressed(150, 600, 300, 150, screen, self.rbuttom, self.hoover1)

class buttons:
    def __init__(self):
        pass



def mouse_button_pressed(x,y,w,h,screen,image_original,image_hover,action=None):
    click=pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        screen.blit(image_original, [x, y])
        screen.blit(image_hover,[x,y])
        if click[0]==1 and action != None:
            action()
    else:
        screen.blit(image_original,[x,y])

def text_objects(text,font):
    textSurface = font.render (text,True, black)
    return textSurface, textSurface.get_rect()

def message_to_screen(text):
    largeText = pygame.font.Font("freesansbold.ttf",50)
    textsuf , textrect = text_objects(text,largeText)
    textrect.center = ((width/2),(heigth/2))

def Close_game(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

def run ():
    game = Game()
    game.loop_of_game()

run()

"""
voor neerzetten van boot (onderste speler)
if self.x > 0:
self.y = heigth * 0.85

(bovenste speler
if self.x > 0:
    self.y = 0
"""