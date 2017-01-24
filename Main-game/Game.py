import pygame
import sys

width = 1280
heigth = 720
size = (width, heigth)




class Game:
    def __init__(self):
        pygame.init()
        self.turn= Turn()
        pygame.display.set_caption("Shipwars Informatica Editon")
        self.gameExit = False
        self.screen = pygame.display.set_mode((size))
        self.intro_game = IntroGame(self)
        self.game_main = GameMain(self)
        self.pause_menu = PauseMenu(self)
        self.ship1 = Boats(heigth*0.040,width*0.512,30,133,"boat1",3,3,"battleship1.png")
        self.ship2 = Boats(heigth*0.040,width*0.568,20,100,"boat2",3,3,"battleship2.png")
        self.ship3 = Boats(heigth*0.040,width*0.465,20,100,"boat3",3,3,"battleship.png")
        self.ship4 = Boats(heigth * 0.83, width * 0.465, 20, 100, "boat1", 3, 3, "battleship4.png")
        self.ship5 = Boats(heigth * 0.784, width * 0.512, 30, 133, "boat2", 3, 3, "battleship5.png")
        self.ship6 = Boats(heigth * 0.83, width * 0.568, 20, 100, "boat3", 3, 3, "battleship6.png")
        self.state = self.intro_game
        self.events = []

    def set_state(self, state):
        self.state = state

    def update(self):
        self.game_main.update()


    def draw(self):
        if self.state == self.intro_game:
            self.intro_game.draw(self.screen)

        if self.state == self.game_main:
            self.game_main.draw(self.screen)
            if self.turn.turn_number == 0:
                self.ship1.draw(self.screen)
                self.ship2.draw(self.screen)
                self.ship3.draw(self.screen)
            elif self.turn.turn_number >= 1:
                self.ship1.draw(self.screen)
                self.ship2.draw(self.screen)
                self.ship3.draw(self.screen)
                self.ship4.draw(self.screen)
                self.ship5.draw(self.screen)
                self.ship6.draw(self.screen)
            self.turn.draw(self.screen)

        if self.state == self.pause_menu:
            self.pause_menu.draw(self.screen)


        pygame.display.flip()

    # loop voor het laten runnen van het spel
    def loop_of_game(self):
        while not self.gameExit:
            self.events = pygame.event.get()
            self.update()
            self.draw()
            for event in self.events:
                if event.type == pygame.QUIT:
                    quit()

class Boats:
    def __init__(self, lead_x, lead_y, w,h,naam,hp,armor, image):
        self.game = Game
        self.lead_x = lead_y
        self.lead_y = lead_x
        self.hp = hp
        self.armor = armor
        self.block_size = 33.333
        self.block_size_up_down = 33.333
        self.naam = naam
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [w, h])

    def draw(self, screen):
        screen.blit(self.image, [self.lead_x, self.lead_y])

    def rotate(self, degrees):
        self.image = pygame.transform.rotate(self.image, degrees)

    def move_up(self):
        self.lead_y += self.block_size_up_down
        if self.lead_y > heigth * 0.82:
            self.lead_y = heigth * 0.82
        if self.turn.turn_number == 0:
            if self.lead_y > heigth * 0.04:
                self.lead_y = heigth * 0.04

    def move_down(self):
        self.lead_y -= self.block_size_up_down
        if self.lead_y < heigth * 0.04:
            self.lead_y= heigth * 0.04
        if self.turn.turn_number == 1:
            if self.lead_y > heigth*0.630:
                self.lead_y = heigth * 0.82

    def move_left(self):
        self.lead_x -= self.block_size
        if self.lead_x < width * 0.25:
            self.lead_x = width * 0.25

    def move_right(self):
        self.lead_x += self.block_size
        if self.lead_x> width * 0.747:
            self.lead_x = width * 0.747

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
        self.ibuttom = pygame.image.load("button_instructions.png")
        self.ibuttom = pygame.transform.scale(self.ibuttom, [250, 50])
        self.bquit = pygame.image.load("button_quit.png")
        self.bquit = pygame.transform.scale(self.bquit, [250, 50])
        self.title = pygame.image.load("title.png")
        self.title = pygame.transform.scale(self.title, [heigth, 200])
        self.hoover = pygame.image.load("hover.png")
        self.hoover = pygame.transform.scale(self.hoover, [274, 50])
        self.hoover1 = pygame.image.load("hover.png")
        self.hoover1 = pygame.transform.scale(self.hoover, [250, 80])
        self.previeuwgame = pygame.image.load("previeuwgame1.png")
        self.previeuwgame = pygame.transform.scale(self.previeuwgame, [500, 300])

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        screen.blit(self.bg, [0, 0])
        screen.blit(self.title, (width / 5, heigth * 0.1))
        mouse_button_pressed(width/20, heigth/2.0, 250, 70, screen, self.pbuttom, self.game.events,
                                lambda: self.game.set_state(self.game.game_main))
        mouse_button_pressed(width/20, heigth/1.63, 250, 70, screen, self.hbuttom,self.game.events)
        mouse_button_pressed(width/20, heigth/1.38, 250, 70, screen, self.ibuttom,self.game.events)
        mouse_button_pressed(width/20, heigth/1.2, 250, 70, screen, self.bquit,self.game.events,lambda: sys.exit())
        if width/20 + 250 > mouse[0] > width/20 and heigth/2.0 + 50 > mouse[1] > heigth/2.0:
            screen.blit(self.previeuwgame, (width*0.4,heigth*0.5))
            screen.blit (self.hoover, [width/24,heigth/2.0])
        if width/20 + 250 > mouse[0] > width/20 and heigth/1.63 + 50 > mouse[1] > heigth/1.63:
            screen.blit(self.previeuwgame, (width*0.4,heigth*0.5))
            screen.blit (self.hoover, [width/24,heigth/1.63])
        if width/20 + 250 > mouse[0] > width/20 and heigth/1.38 + 50 > mouse[1] > heigth/1.38:
            screen.blit(self.previeuwgame, (width*0.4,heigth*0.5))
            screen.blit (self.hoover, [width/24,heigth/1.38])


class GameMain:
    def __init__(self, game):
        self.pause_menu = PauseMenu
        self.game = game
        self.turn=Turn()
        self.font = pygame.font.Font(None, 25)
        self.sides = pygame.image.load("sides.jpg")
        self.sides = pygame.transform.scale(self.sides, (size))
        self.bggame = pygame.image.load("bggame.jpg")
        self.bggame = pygame.transform.scale(self.bggame, (670, 670))
        self.pbutton = pygame.image.load("menu.png")
        self.pbutton = pygame.transform.scale(self.pbutton, [70, 70])
        self.hoover = pygame.image.load("hoover_image.png")
        self.hoover = pygame.transform.scale(self.hoover, [120, 120])
        self.abutton = pygame.image.load("attack_defence.png")
        self.abutton = pygame.transform.scale(self.abutton, [130 , 50])
        self.movebutton = pygame.image.load("movebutton.png")
        self.movebutton = pygame.transform.scale(self.movebutton, [80,80])
        self.next_turn = pygame.image.load ("next.png")
        self.next_turn = pygame.transform.scale(self.next_turn,[250,70])
        self.emptyimage = pygame.image.load ("empty.png")
        self.emptyimage = pygame.transform.scale(self.emptyimage,[30,30])
        self.redline = pygame.image.load("redline.png")
        self.redline = pygame.transform.scale(self.redline,[670,150])

    def update(self):
        keys = pygame.key.get_pressed()
        if self.game.state == self.game.game_main:
            if keys[pygame.K_ESCAPE]:
                self.game.set_state(self.game.pause_menu)

    def draw(self, screen):
        screen.blit(self.sides, [0, 0])
        screen.blit(self.bggame, [width * 0.25, heigth * 0.04])
        screen.blit(self.movebutton, (width*0.01, heigth*0.11))
        screen.blit(self.movebutton, (width * 0.01, heigth * 0.42))
        screen.blit(self.movebutton, (width * 0.01, heigth * 0.735))
        # menu button---------------------------------------------------------------------------------------------
        mouse_button_pressed(1200, 10, 50, 50, screen, self.pbutton,self.game.events,
                             lambda: self.game.set_state(self.game.pause_menu))

        if self.turn.turn_number == 0:
            # rotate buttons------------------------------------------------------------------------------------------
            mouse_button_pressed(10, 10, 130, 50, screen, self.abutton,self.game.events,
                                 lambda: self.game.ship1.rotate(90))
            mouse_button_pressed(10, 240, 130, 50, screen, self.abutton,self.game.events,
                                 lambda: self.game.ship2.rotate(90))
            mouse_button_pressed(10, 470, 130, 50, screen, self.abutton,self.game.events,
                                 lambda: self.game.ship1.rotate(90))
            # movement buttons ship1-----------------------------------------------------------------------------------
            mouse_button_pressed(width*0.03, heigth*0.115, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.18, 40, 30, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.147, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.147, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_left())

            # movement buttons ship2-----------------------------------------------------------------------------------
            mouse_button_pressed(width * 0.03, heigth * 0.42, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship2.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.49, 40, 30, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship2.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.45, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship2.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.45, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship2.move_left())
            #  ship 3 movement-------------------------------------------------------------------------------------------

            mouse_button_pressed(width * 0.03, heigth * 0.737, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.80, 40, 30, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.763, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.763, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_left())

        if self.turn.turn_number == 1:
            # rotate buttons------------------------------------------------------------------------------------------
            mouse_button_pressed(10, 10, 130, 50, screen, self.abutton,self.game.events,
                                 lambda: self.game.ship4.rotate(90))
            mouse_button_pressed(10, 240, 130, 50, screen, self.abutton,self.game.events,
                                 lambda: self.game.ship5.rotate(90))
            mouse_button_pressed(10, 470, 130, 50, screen, self.abutton,self.game.events,
                                 lambda: self.game.ship6.rotate(90))
            # movement buttons ship1-----------------------------------------------------------------------------------
            mouse_button_pressed(width * 0.03, heigth * 0.115, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship4.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.18, 40, 30, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship4.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.147, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship4.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.147, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship4.move_left())

            # movement buttons ship2-----------------------------------------------------------------------------------
            mouse_button_pressed(width * 0.03, heigth * 0.42, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship5.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.49, 40, 30, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship5.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.45, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship5.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.45, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship5.move_left())
            #  ship 3 movement-------------------------------------------------------------------------------------------

            mouse_button_pressed(width * 0.03, heigth * 0.737, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship6.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.80, 40, 30, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship6.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.763, 40, 20, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship6.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.763, 40, 20, screen, self.emptyimage,
                                 lambda: self.game.ship6.move_left())

        # next turn button-----------------------------------------------------------------------------------------
        mouse_button_pressed(1000, 635, 170, 80, screen, self.next_turn,self.game.events,
                             lambda: self.turn.update)
        # red placing line-----------------------------------------------------------------------------------------
        if self.turn.turn_number == 0:
            screen.blit(self.redline,(width * 0.25,heigth*0.089))
        elif self.turn.turn_number == 1:
            screen.blit(self.redline,(width*0.25,heigth*0.655))

class PauseMenu:
    def __init__(self, game):
        # sprites
        self.game = game
        self.pbuttom = pygame.image.load("button_continue.png")
        self.pbuttom = pygame.transform.scale(self.pbuttom, [250, 50])
        self.ibuttom = pygame.image.load("button_instructions.png")
        self.ibuttom = pygame.transform.scale(self.ibuttom, [250, 50])
        self.qbuttom = pygame.image.load("button_quit.png")
        self.qbuttom = pygame.transform.scale(self.qbuttom, [250, 50])
        self.title = pygame.image.load("title.png")
        self.title = pygame.transform.scale(self.title, [700, 200])
        self.hoover = pygame.image.load("hoover_image.png")
        self.hoover = pygame.transform.scale(self.hoover, [320, 160])
        self.hoover1 = pygame.image.load("hoover_image.png")
        self.hoover1 = pygame.transform.scale(self.hoover, [370, 120])
        self.bmenu = pygame.image.load("button_menu.png")
        self.bmenu = pygame.transform.scale(self.bmenu, [250,50])

    def draw(self, screen):
        mouse= pygame.mouse.get_pos()
        screen.blit(self.title, (width*0.25, heigth*0.15))
        mouse_button_pressed(width*0.4, heigth*0.5, 250, 50, screen, self.pbuttom,self.game.events,
                             lambda: self.game.set_state(self.game.game_main))
        mouse_button_pressed(width*0.4, heigth*0.8, 250, 50, screen, self.qbuttom,self.game.events,
                             lambda: sys.exit())
        mouse_button_pressed(width*0.4, heigth*0.6, 250, 50, screen, self.ibuttom,self.game.events)
        mouse_button_pressed(width * 0.4, heigth * 0.7, 250, 50, screen, self.bmenu,self.game.events,
                             lambda : self.game.set_state(self.game.intro_game))
        # if width*0.4 + 250 > mouse[0] > width*0.4 and heigth*0.5 + 50 > mouse[1] > heigth*0.5:
        #     screen.blit (self.hoover, [width*0.4, heigth*0.5])
        # elif width*0.4 + 250 > mouse[0] > width*0.4 and heigth*0.6 + 50 > mouse[1] > heigth*0.6:
        #     screen.blit (self.hoover, [width*0.4, heigth*0.6])
        # elif width*0.4 + 250 > mouse[0] > width*0.4 and heigth*0.7 + 50 > mouse[1] > heigth*0.7:
        #     screen.blit (self.hoover, [width*0.4, heigth*0.7])

class Turn:
    def __init__(self):
        self.font = pygame.font.Font(None, 25)
        self.turn_number = 0
        self.player = Player

    def update(self):
        self.turn_number += 1

    def draw(self,screen):
        self.turn_text = self.font.render("current Turn: {}".format(self.turn_number),1,(255,255,255))
        if self.turn_number == 0:
            self.turn_text1 = self.font.render("Please place your ships player 1", 1, (255, 255, 255))
            screen.blit(self.turn_text1, (350, 10))
        elif self.turn_number == 1:
            self.turn_text1 = self.font.render("Please place your ships player 2", 1, (255, 255, 255))
            screen.blit(self.turn_text1 ,(350,10))
        screen.blit(self.turn_text, (750,10))

class Player:
    def __init__(self,player1,player2,score,winner):
        self.player1 = player1
        self.player1 = player2
        self.score = score
        self.winner = winner

def mouse_button_pressed(x, y, w, h, screen, image_original, events, action=None):
    screen.blit(image_original, [x, y])
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and action != None:
                action()

def run():
    game = Game()
    game.loop_of_game()


run()



















"""
def text_objects(text,font):
    textSurface = font.render (text,True, (90,90))
    return textSurface, textSurface.get_rect()

def message_to_screen(text):
    largeText = pygame.font.Font("freesansbold.ttf",50)
    textsuf , textrect = text_objects(text,largeText)
    textrect.center = ((width/2),(heigth/2))

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