import pygame
import sys

width = 1280
heigth = 720
size = (width, heigth)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Shipwars Informatica Editon")
        self.gameExit = False
        self.screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
        self.intro_game = IntroGame(self)
        self.game_main = GameMain(self)
        self.pause_menu = PauseMenu(self)
        self.ship1 = Boats(heigth*0.045,width*0.695, "boat1", "battleship1.png")
        self.state = self.intro_game

    def set_state(self, state):
        self.state = state

    def update(self):
        self.ship1.update()
        self.game_main.update()

    def draw(self):
        self.state.draw(self.screen)

        if self.state == self.game_main:
            self.game_main.draw(self.screen)
            self.ship1.draw(self.screen)

        pygame.display.flip()

    # loop voor het laten runnen van het spel
    def loop_of_game(self):
        while not self.gameExit:
            self.update()
            self.draw()

class Boats:
    def __init__(self, lead_x, lead_y, naam, image):
        self.lead_x = lead_y
        self.lead_y = lead_x
        self.block_size = 33.333
        self.block_size_up_down = 33.333
        self.naam = naam
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [30, 100])

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.lead_x -= self.block_size
                elif event.key == pygame.K_RIGHT:
                    self.lead_x += self.block_size
                elif event.key == pygame.K_UP:
                    self.lead_y -= self.block_size_up_down
                elif event.key == pygame.K_DOWN:
                    self.lead_y += self.block_size_up_down


    def draw(self, screen):
        screen.blit(self.image, [self.lead_x, self.lead_y])


    def rotate(self, degrees):
        self.image = pygame.transform.rotate(self.image, degrees)

class IntroGame:
    def __init__(self, game):
        # sprites
        self.game = game
        self.bg = pygame.image.load("bg2.jpg")
        self.bg = pygame.transform.scale(self.bg, (size))
        self.pbuttom = pygame.image.load("button_play.png")
        self.pbuttom = pygame.transform.scale(self.pbuttom, [250, 50])
        self.hbuttom = pygame.image.load("button_high-scores.png")
        self.hbuttom = pygame.transform.scale(self.hbuttom, [250, 50])
        self.rbuttom = pygame.image.load("button_instructions.png")
        self.rbuttom = pygame.transform.scale(self.rbuttom, [250, 50])
        self.bquit = pygame.image.load("button_quit.png")
        self.bquit = pygame.transform.scale(self.bquit, [250, 50])
        self.title = pygame.image.load("title.png")
        self.title = pygame.transform.scale(self.title, [heigth, 200])
        self.hoover = pygame.image.load("hover.png")
        self.hoover = pygame.transform.scale(self.hoover, [275, 50])
        self.hoover1 = pygame.image.load("hover.png")
        self.hoover1 = pygame.transform.scale(self.hoover, [250, 80])
        self.previeuwgame = pygame.image.load("previeuwgame.png")
        self.previeuwgame = pygame.transform.scale(self.previeuwgame, [300, 300])

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        screen.blit(self.bg, [0, 0])
        screen.blit(self.title, (width / 5, heigth * 0.1))
        mouse_button_pressed(width/20, heigth/2.0, 250, 70, screen, self.pbuttom, self.hoover,
                                lambda: self.game.set_state(self.game.game_main))
        mouse_button_pressed(width/20, heigth/1.63, 250, 70, screen, self.hbuttom, self.hoover)
        mouse_button_pressed(width/20, heigth/1.38, 250, 70, screen, self.rbuttom, self.hoover)
        mouse_button_pressed(width/20, heigth/1.2, 250, 70, screen, self.bquit, self.hoover, lambda: sys.exit())
        if width/20 + 250 > mouse[0] > width/20 and heigth/2.0 + 80 > mouse[1] > heigth/2.0:
            screen.blit(self.previeuwgame, (width*0.5,heigth*0.5))

class GameMain:
    def __init__(self, game):
        self.pause_menu = PauseMenu(self)
        self.game = game
        self.sides = pygame.image.load("sides.jpg")
        self.sides = pygame.transform.scale(self.sides, (size))
        self.bggame = pygame.image.load("bggame.jpg")
        self.bggame = pygame.transform.scale(self.bggame, (670, 670))
        self.pbutton = pygame.image.load("menu.png")
        self.pbutton = pygame.transform.scale(self.pbutton, [50, 50])
        self.hoover = pygame.image.load("hoover_image.png")
        self.hoover = pygame.transform.scale(self.hoover, [120, 120])
        self.abutton = pygame.image.load("attack_defence.png")
        self.abutton = pygame.transform.scale(self.abutton, [130 , 50])


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game.set_state(self.game.pause_menu)

    def draw(self, screen):
        screen.blit(self.sides, [0, 0])
        screen.blit(self.bggame, [width * 0.25, heigth * 0.04])
        mouse_button_pressed(1000, 10, 50, 50, screen, self.pbutton, self.hoover,
                             lambda: self.game.set_state(self.game.pause_menu))
        mouse_button_pressed(10, 10, 120, 120, screen, self.abutton, self.hoover,
                             lambda: self.game.ship1.rotate(90))
        mouse_button_pressed(10, 240, 120, 120, screen, self.abutton, self.hoover,
                             lambda: self.game.ship1.rotate(90))
        mouse_button_pressed(10, 470, 120, 120, screen, self.abutton, self.hoover,
                             lambda: self.game.ship1.rotate(90))


class PauseMenu:
    def __init__(self, game):
        # sprites
        self.game = game
        self.pbuttom = pygame.image.load("Play.png")
        self.pbuttom = pygame.transform.scale(self.pbuttom, [300, 150])
        self.hbuttom = pygame.image.load("hscore.png")
        self.hbuttom = pygame.transform.scale(self.hbuttom, [350, 100])
        self.rbuttom = pygame.image.load("Instrutions.png")
        self.rbuttom = pygame.transform.scale(self.rbuttom, [350, 150])
        self.title = pygame.image.load("title.png")
        self.title = pygame.transform.scale(self.title, [heigth, 200])
        self.hoover = pygame.image.load("hoover_image.png")
        self.hoover = pygame.transform.scale(self.hoover, [320, 160])
        self.hoover1 = pygame.image.load("hoover_image.png")
        self.hoover1 = pygame.transform.scale(self.hoover, [370, 120])

    def draw(self, screen):
        screen.blit(self.title, (width / 5, width / 8))
        mouse_button_pressed(450, 400, 300, 150, screen, self.pbuttom, self.hoover,
                             lambda: self.game.set_state(self.game.game_main))
        mouse_button_pressed(750, 625, 300, 150, screen, self.hbuttom, self.hoover1,
                             lambda: self.game.set_state(self.game.intro_game))
        mouse_button_pressed(150, 600, 300, 150, screen, self.rbuttom, self.hoover1)

def mouse_button_pressed(x, y, w, h, screen, image_original, image_hover, action=None):
    screen.blit(image_original, [x, y])
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        screen.blit(image_hover, [x, y])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                screen.blit(image_hover, [x, y])
                if action != None:
                     action()

def run():
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

def text_objects(text,font):
    textSurface = font.render (text,True, black)
    return textSurface, textSurface.get_rect()

def message_to_screen(text):
    largeText = pygame.font.Font("freesansbold.ttf",50)
    textsuf , textrect = text_objects(text,largeText)
    textrect.center = ((width/2),(heigth/2))



        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.block_size
        elif keys [pygame.K_RIGHT]:
            self.x += self.block_size

        if keys[pygame.K_UP]:
            self.y -= self.block_size_up_down
        elif keys[pygame.K_DOWN]:
            self.y += self.block_size_up_down

        if self.x < width*0.21:
            self.x = width*0.21
        elif self.y < heigth*0.06:
            self.y = heigth*0.06
        if self.x > width*0.765:
            self.x = width*0.765
        elif self.y > heigth*0.815:
            self.y = heigth*0.815




"""

"""


"""