#import required modules
import pygame
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
        self.state = self.intro_game

    def set_state(self, state):
        self.state = state

    def draw(self):
        self.state.draw(self.screen)
        pygame.display.flip()


    #loop voor het laten runnen van het spel
    def loop_of_game(self):
        while not Close_game():
            self.draw()
            #self.state = self.state.update(...)




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
        self.game = game
        self.board = pygame.image.load("board.jpg")
        self.board = pygame.transform.scale(self.board, [800,600])
        self.side = pygame.image.load("side.jpg")
        self.side = pygame.transform.scale(self.side, size)
        self.border = pygame.image.load("border.png")
        self.border = pygame.transform.scale(self.border, [900,650])
        self.pbutton = pygame.image.load("menu.png")
        self.pbutton = pygame.transform.scale(self.pbutton, [50, 50])
        self.hoover = pygame.image.load("hoover_image.png")
        self.hoover = pygame.transform.scale(self.hoover, [60, 60])

    def draw(self,screen):
        screen.blit(self.side,[0,0])
        screen.blit(self.board,[width/6,heigth/8])
        screen.blit(self.border,[width/8,heigth/10])
        mouse_button_pressed(10, 10, 50, 50, screen, self.pbutton, self.hoover,lambda: self.game.set_state(self.game.pause_menu))


class Higscorelist:
    def __init__(self):
        # sprites
        pass

class GamerulesList:
    def __init__(self):
        # sprites
        pass

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
