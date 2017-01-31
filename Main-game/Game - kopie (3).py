import pygame
import sys
import random
import time



width = 1280
heigth = 720
size = (width, heigth)

class Game:
    def __init__(self):
        pygame.init()
        self.turn= Turn()
        self.player = Player
        self.player1 = Player(3)
        self.player2 = Player(3)
        self.boats = Boats
        pygame.display.set_caption("Shipwars Informatica Editon")
        self.gameExit = False
        self.cards= Cards (self,self.turn)
        self.screen = pygame.display.set_mode((size))
        self.intro_game = IntroGame(self)
        self.game_main = GameMain(self,self.turn,self.cards)
        self.pause_menu = PauseMenu(self)
        self.ship1 = Boats(heigth*0.040, width*0.4583,30,133,"boat1",4,2,1,"battleship1.png",self.turn)
        self.ship2 = Boats(heigth*0.040,width*0.511,20,100,"boat2",3,3,1,"battleship2.png",self.turn)
        self.ship3 = Boats(heigth * 0.040,width*0.562,20,100,"boat3",2,3,1,"battleship.png",self.turn)
        self.ship4 = Boats(heigth * 0.79, width * 0.46, 30, 130, "boat1", 4, 2, 1,"battleship5.png",self.turn)
        self.ship5 = Boats(heigth * 0.83, width * 0.512, 20, 100, "boat2", 3, 3,1, "battleship6.png",self.turn)
        self.ship6 = Boats(heigth * 0.83, width * 0.564, 20, 100, "boat3", 2, 3,1, "battleship4.png",self.turn)
        self.state = self.intro_game
        self.events = []

    def set_state(self, state):
        self.state = state

    def update(self):
        self.game_main.update()

    def draw(self,screen):
        if self.state == self.intro_game:
            self.intro_game.draw(self.screen)

        if self.state == self.game_main:
            self.game_main.draw(self.screen)
            self.cards.draw(self.screen)
            if self.turn.turn_number == 0:
                self.ship3.draw(self.screen)
                self.ship2.draw(self.screen)
                self.ship1.draw(self.screen)
            elif self.turn.turn_number == 1:
                self.ship6.draw(self.screen)
                self.ship5.draw(self.screen)
                self.ship4.draw(self.screen)
            elif self.turn.turn_number > 1:
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
            self.draw(self.screen)
            for event in self.events:
                if event.type == pygame.QUIT:
                    quit()

class Boats:
    def __init__(self, lead_x, lead_y, width,height,naam,hp,feul,attack_p, image,turn):
        self.game = Game
        self.turn = turn
        self.width = width
        self.height = height
        self.lead_x = lead_y
        self.lead_y = lead_x
        self.attack_p = attack_p
        self.hp = hp
        self.feul = feul
        self.block_size = 32.8
        self.block_size_up_down = 33.333
        self.naam = naam
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [width, height])


    def draw(self, screen):
        screen.blit(self.image, [self.lead_x, self.lead_y])

    def resetfeul(self):
        self.feul = 3

    def rotate(self, degrees):
        if self.hp>0:
            self.image = pygame.transform.rotate(self.image, degrees)

    def move_up(self):
        if self.feul >0:
            self.lead_y += self.block_size_up_down
            self.feul -= 1
            if self.lead_y > heigth * 0.82:
                self.lead_y = heigth * 0.82
            if self.turn.turn_number == 0:
                if self.lead_y > heigth * 0.04:
                    self.lead_y = heigth * 0.04


    def move_down(self):
        if self.feul > 0 and self.hp>0:
            self.lead_y -= self.block_size_up_down
            self.feul -= 1
            if self.lead_y < heigth * 0.04:
                self.lead_y= heigth * 0.04
            if self.turn.turn_number == 1:
                if self.lead_y > heigth*0.630:
                    self.lead_y = heigth * 0.82

    def move_left(self):
        if self.feul > 0 and self.hp>0:
            self.lead_x -= self.block_size
            self.feul -= 1
            if self.lead_x < width * 0.25:
                self.lead_x = width * 0.25

    def move_right(self):
        if self.feul > 0 and self.hp>0:
            self.lead_x += self.block_size
            self.feul -= 1
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

    def draw(self,screen):
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
        if width/20 + 250 > mouse[0] > width/20 and heigth/1.2 + 50 > mouse[1] > heigth/1.2:
            screen.blit (self.hoover, [width/24,heigth/1.2])

class GameMain:
    def __init__(self, game , turn , cards):
        self.button_test = False
        self.cards_shown = False
        self.cards_draw = False
        self.min_health = False
        self.block_size = 32.8
        self.block_size_up_down = 33.333
        self.pause_menu = PauseMenu
        self.game = game
        self.turn= turn
        self.cards = cards
        self.font = pygame.font.Font(None,25)
        self.sides = pygame.image.load("sides.jpg")
        self.sides = pygame.transform.scale(self.sides, (size))
        self.bggame = pygame.image.load("bord.png")
        self.bggame = pygame.transform.scale(self.bggame, (725, 725))
        self.pbutton = pygame.image.load("menu.png")
        self.pbutton = pygame.transform.scale(self.pbutton, [50, 50])
        self.hoover = pygame.image.load("hoover_image.png")
        self.hoover = pygame.transform.scale(self.hoover, [120, 120])
        self.abutton = pygame.image.load("attack_defence.png")
        self.abutton = pygame.transform.scale(self.abutton, [130 , 50])
        self.movebutton = pygame.image.load("movebutton.png")
        self.movebutton = pygame.transform.scale(self.movebutton, [80,80])
        self.next_turn = pygame.image.load ("next.png")
        self.next_turn = pygame.transform.scale(self.next_turn,[250,70])
        self.emptyimage = pygame.image.load ("empty.png")
        self.emptyimage = pygame.transform.scale(self.emptyimage,[60,50])
        self.redline = pygame.image.load("redline.png")
        self.redline = pygame.transform.scale(self.redline,[670,150])
        self.ihealth = pygame.image.load("healthon.png")
        self.ihealth = pygame.transform.scale(self.ihealth, [30, 30])
        self.ohealth = pygame.image.load("healthoff.png")
        self.ohealth = pygame.transform.scale(self.ohealth, [30, 30])
        self.yes = pygame.image.load("yes.png")
        self.yes = pygame.transform.scale(self.yes, [70,70])
        self.no = pygame.image.load("no.png")
        self.no = pygame.transform.scale(self.no, [70, 70])
        self.boat1= pygame.image.load("battleship1.png")
        self.boat1 = pygame.transform.scale(self.boat1,[30,133])
        self.boat2 = pygame.image.load("battleship2.png")
        self.boat2 = pygame.transform.scale(self.boat2, [20, 100])
        self.boat3 = pygame.image.load("battleship.png")
        self.boat3 = pygame.transform.scale(self.boat3, [20, 100])
        self.carda = pygame.image.load("carda.jpg")
        self.carda = pygame.transform.scale(self.carda, [170, 90])
        self.carda1 = pygame.image.load("carda1.jpg")
        self.carda1 = pygame.transform.scale(self.carda, [90, 160])
        self.attack_button = pygame.image.load("attack_button.png")
        self.attack_button = pygame.transform.scale(self.attack_button,[50,50])



    def update(self):
        keys = pygame.key.get_pressed()
        if self.game.state == self.game.game_main:
            if keys[pygame.K_ESCAPE]:
                self.game.set_state(self.game.pause_menu)

            if self.button_test:
                self.game.ship1.feul = 99
                self.game.ship2.feul = 99
                self.game.ship3.feul = 99
                self.game.ship4.feul = 99
                self.game.ship5.feul = 99
                self.game.ship6.feul = 99
                self.game.ship1.attack_p = 1
                self.game.ship2.attack_p = 1
                self.game.ship3.attack_p = 1
                self.game.ship4.attack_p = 1
                self.game.ship5.attack_p = 1
                self.game.ship6.attack_p = 1






    def draw(self, screen):
        #standaard images----------------------------------------------------------------------------------------
        screen.blit(self.sides, [0, 0])
        screen.blit(self.bggame, [width * 0.225,0])
        screen.blit(self.movebutton, (width*0.01, heigth*0.11))
        screen.blit(self.movebutton, (width * 0.01, heigth * 0.42))
        screen.blit(self.movebutton, (width * 0.01, heigth * 0.735))
        screen.blit(self.boat1, (width*0.16, heigth*0.1))
        screen.blit(self.boat2, (width * 0.16, heigth * 0.43))
        screen.blit(self.boat3, (width * 0.16, heigth * 0.75))
        screen.blit(self.abutton, (width * 0.01, heigth*0.02))
        screen.blit(self.abutton, (width * 0.01, heigth * 0.335))
        screen.blit(self.abutton, (width * 0.01, heigth * 0.653))
        message_to_screen("scorep1 : {}".format(self.game.player1.boats), screen, width * 0.06, heigth * 0.3, 18)
        message_to_screen("attack1 : {}".format(self.game.ship1.attack_p), screen, width * 0.06, heigth * 0.35, 18)

        # menu button---------------------------------------------------------------------------------------------
        mouse_button_pressed(width*0.77,heigth*0.01, 50, 50, screen, self.pbutton,self.game.events,
                             lambda: self.game.set_state(self.game.pause_menu))

        if self.turn.turn_number%2 == 0:
            # rotate buttons------------------------------------------------------------------------------------------
            mouse_button_pressed(width*0.01,heigth*0.02, 60, 50, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.rotate(90))
            mouse_button_pressed(width*0.065,heigth*0.02, 60, 50, screen, self.emptyimage, self.game.events,
                                 lambda: self.game.ship1.rotate(-90))
            mouse_button_pressed(width*0.01, heigth * 0.335, 60, 50, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship2.rotate(90))
            mouse_button_pressed(width*0.065, heigth * 0.335, 60, 50, screen, self.emptyimage, self.game.events,
                                 lambda: self.game.ship2.rotate(-90))
            mouse_button_pressed(width*0.01, heigth * 0.653, 60, 50, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship3.rotate(90))
            mouse_button_pressed(width*0.065, heigth * 0.653, 60, 50, screen, self.emptyimage, self.game.events,
                                 lambda: self.game.ship3.rotate(-90))
            # movement buttons ship1-----------------------------------------------------------------------------------
            mouse_button_pressed(width*0.03, heigth*0.115, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.18, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.147, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.147, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship1.move_left())

            # movement buttons ship2-----------------------------------------------------------------------------------
            mouse_button_pressed(width * 0.03, heigth * 0.42, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship2.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.49, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship2.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.45, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship2.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.45, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship2.move_left())
            #  ship 3 movement-------------------------------------------------------------------------------------------

            mouse_button_pressed(width * 0.03, heigth * 0.737, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship3.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.80, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship3.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.763, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship3.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.763, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship3.move_left())

        elif self.turn.turn_number%2 == 1:

            # rotate buttons------------------------------------------------------------------------------------------
            mouse_button_pressed(width * 0.01, heigth * 0.02, 60, 50, screen, self.emptyimage, self.game.events,
                                 lambda: self.game.ship4.rotate(90))
            mouse_button_pressed(width * 0.065, heigth * 0.02, 60, 50, screen, self.emptyimage, self.game.events,
                                 lambda: self.game.ship4.rotate(-90))
            mouse_button_pressed(width * 0.01, heigth * 0.335, 60, 50, screen, self.emptyimage, self.game.events,
                                 lambda: self.game.ship5.rotate(90))
            mouse_button_pressed(width * 0.065, heigth * 0.335, 60, 50, screen, self.emptyimage, self.game.events,
                                 lambda: self.game.ship5.rotate(-90))
            mouse_button_pressed(width * 0.01, heigth * 0.653, 60, 50, screen, self.emptyimage, self.game.events,
                                 lambda: self.game.ship6.rotate(90))
            mouse_button_pressed(width * 0.065, heigth * 0.653, 60, 50, screen, self.emptyimage, self.game.events,
                                 lambda: self.game.ship6.rotate(-90))
            # movement buttons ship1-----------------------------------------------------------------------------------
            mouse_button_pressed(width * 0.03, heigth * 0.115, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship4.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.18, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship4.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.147, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship4.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.147, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship4.move_left())

            # movement buttons ship2-----------------------------------------------------------------------------------
            mouse_button_pressed(width * 0.03, heigth * 0.42, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship5.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.49, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship5.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.45, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship5.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.45, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship5.move_left())
            #  ship 3 movement-------------------------------------------------------------------------------------------

            mouse_button_pressed(width * 0.03, heigth * 0.737, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship6.move_down())
            mouse_button_pressed(width * 0.03, heigth * 0.80, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship6.move_up())
            mouse_button_pressed(width * 0.05, heigth * 0.763, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship6.move_right())
            mouse_button_pressed(width * 0.01, heigth * 0.763, 35, 35, screen, self.emptyimage,self.game.events,
                                 lambda: self.game.ship6.move_left())

        # next turn button-----------------------------------------------------------------------------------------
        def next_turn_conf_true():
            self.button_test = True
        def next_turn_conf_false():
            self.button_test = False

        mouse_button_pressed(width * 0.8, heigth * 0.9,250,70,screen,self.next_turn,self.game.events,lambda: next_turn_conf_true())
        if self.button_test and self.turn.turn_number < 2:
            message_to_screen("are you sure you want to end your turn", screen, width * 0.5, heigth * 0.62, 30)
            mouse_button_pressed(width * 0.425, heigth * 0.65, 70, 70, screen, self.yes, self.game.events,
                             lambda: self.turn.update())
            mouse_button_pressed(width * 0.425, heigth * 0.65, 70, 70, screen, self.yes, self.game.events,
                             lambda: next_turn_conf_false())
            mouse_button_pressed(width * 0.525, heigth * 0.65, 70, 70, screen, self.no, self.game.events,
                             lambda: self.game.set_state(self.game.game_main))
            mouse_button_pressed(width * 0.525, heigth * 0.65, 70, 70, screen, self.no, self.game.events,
                             lambda: next_turn_conf_false())
        elif self.button_test and self.turn.turn_number > 1:
            message_to_screen("are you sure you want to end your turn", screen, width * 0.5, heigth * 0.48, 30)
            mouse_button_pressed(width * 0.425, heigth * 0.5, 70, 70, screen, self.yes, self.game.events,
                                     lambda: self.turn.update())
            mouse_button_pressed(width * 0.425, heigth * 0.5, 70, 70, screen, self.yes, self.game.events,
                                     lambda: next_turn_conf_false())
            mouse_button_pressed(width * 0.525, heigth * 0.5, 70, 70, screen, self.no, self.game.events,
                                     lambda: self.game.set_state(self.game.game_main))
            mouse_button_pressed(width * 0.525, heigth * 0.5, 70, 70, screen, self.no, self.game.events,
                                     lambda: next_turn_conf_false())


        # red placing line-----------------------------------------------------------------------------------------
        if self.turn.turn_number == 0:
            screen.blit(self.redline,(width * 0.25,heigth*0.089))
        elif self.turn.turn_number == 1:
            screen.blit(self.redline,(width*0.25,heigth*0.655))

        if self.game.ship1.hp<= 0 and self.game.ship2.hp <= 0 and self.game.ship3.hp <= 0:
            self.game.state = self.game.pause_menu




        # placing health button------------------------------------------------------------------------------------
        def healthoff(self):
            self.min_health = True

        screen.blit(self.ihealth,(width*0.13,heigth*0.03))
        screen.blit(self.ihealth, (width * 0.155, heigth * 0.03))
        screen.blit(self.ihealth, (width * 0.18, heigth * 0.03))
        screen.blit(self.ihealth, (width * 0.205, heigth * 0.03))
        #--------------------------------------------------------
        screen.blit(self.ihealth, (width * 0.13, heigth * 0.35))
        screen.blit(self.ihealth, (width * 0.155, heigth * 0.35))
        screen.blit(self.ihealth, (width * 0.18, heigth * 0.35))
        #--------------------------------------------------------
        screen.blit(self.ihealth, (width * 0.13, heigth * 0.67))
        screen.blit(self.ihealth, (width * 0.155, heigth * 0.67))

        if self.min_health:
            if self.turn.turn_number % 2 == 0:
                if self.game.ship1.hp == 3:
                    screen.blit(self.ohealth, (width * 0.205, heigth * 0.03))
                elif self.game.ship1.hp ==2:
                    screen.blit(self.ohealth, (width * 0.205, heigth * 0.03))
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.03))
                elif self.game.ship1.hp == 1:
                    screen.blit(self.ohealth, (width * 0.205, heigth * 0.03))
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.03))
                    screen.blit(self.ohealth, (width * 0.155, heigth * 0.03))
                elif self.game.ship1.hp <= 0:
                    screen.blit(self.ohealth, (width * 0.205, heigth * 0.03))
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.03))
                    screen.blit(self.ohealth, (width * 0.155, heigth * 0.03))
                    screen.blit(self.ohealth, (width*0.13,heigth*0.03))



                if self.game.ship2.hp ==2:
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.35))
                elif self.game.ship2.hp == 1:
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.35))
                    screen.blit(self.ohealth, (width * 0.155, heigth * 0.35))
                elif self.game.ship2.hp <= 0:
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.35))
                    screen.blit(self.ohealth, (width * 0.155, heigth * 0.35))
                    screen.blit(self.ohealth, (width*0.13,heigth*0.35))


                if self.game.ship3.hp == 1:
                    screen.blit(self.ohealth, (width * 0.155, heigth * 0.67))
                elif self.game.ship3.hp <= 0:
                    screen.blit(self.ohealth, (width * 0.155, heigth *0.67))
                    screen.blit(self.ohealth, (width*0.13,heigth*0.67))

            elif self.turn.turn_number %2 ==1 :
                if self.game.ship4.hp == 3:
                    screen.blit(self.ohealth, (width * 0.205, heigth * 0.03))
                elif self.game.ship4.hp ==2:
                    screen.blit(self.ohealth, (width * 0.205, heigth * 0.03))
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.03))
                elif self.game.ship4.hp == 1:
                    screen.blit(self.ohealth, (width * 0.205, heigth * 0.03))
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.03))
                    screen.blit(self.ohealth, (width * 0.155, heigth * 0.03))
                elif self.game.ship4.hp <= 0:
                    screen.blit(self.ohealth, (width * 0.205, heigth * 0.03))
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.03))
                    screen.blit(self.ohealth, (width * 0.155, heigth * 0.03))
                    screen.blit(self.ohealth, (width*0.13,heigth*0.03))



                if self.game.ship5.hp ==2:
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.35))
                elif self.game.ship5.hp == 1:
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.35))
                    screen.blit(self.ohealth, (width * 0.155, heigth * 0.35))
                elif self.game.ship5.hp <= 0:
                    screen.blit(self.ohealth, (width * 0.18, heigth * 0.35))
                    screen.blit(self.ohealth, (width * 0.155, heigth * 0.35))
                    screen.blit(self.ohealth, (width*0.13,heigth*0.35))



                if self.game.ship6.hp==1:
                    screen.blit(self.ohealth, (width * 0.155, heigth * 0.67))
                elif self.game.ship6.hp <= 0:
                    screen.blit(self.ohealth, (width * 0.155, heigth *0.67))
                    screen.blit(self.ohealth, (width*0.13,heigth*0.67))


        #werking van showing cards--------------------------------------------------------

        def show_cards_true():
            self.cards_shown = True
        def show_cards_false():
            self.cards_shown = False
        mouse_button_pressed(width * 0.92, heigth * 0.72, 80, 60, screen, self.emptyimage, self.game.events,lambda: show_cards_true())
        if self.cards_shown:
            screen.blit(self.carda1, (width * 0.275, heigth * 0.32))
            screen.blit(self.carda1, (width * 0.355, heigth * 0.32))
            screen.blit(self.carda1, (width * 0.435, heigth * 0.32))
            screen.blit(self.carda1, (width * 0.515, heigth * 0.32))
            screen.blit(self.carda1, (width * 0.595, heigth * 0.32))
            screen.blit(self.carda1, (width * 0.675, heigth * 0.32))

        #het krijgen van de kaarten
        def draw_a_card():
            self.cards.attack_cards()
        mouse_button_pressed(width * 0.82, heigth * 0.04, 170, 90, screen, self.emptyimage,self.game.events , draw_a_card) # draw_cards_true)
        if self.turn.turn_number % 2 == 0 and self.cards_draw :
            self.cards.attack_cards(screen)
        if self.turn.turn_number % 2 == 1 and self.cards_draw :
            self.cards.attack_cards(screen)

        if self.cards.attack_cards_choice != None:
            screen.blit(self.cards.attack_cards_choice, (width * 0.87, heigth * 0.53))

        #het draw van feul:
        if self.turn.turn_number%2 == 0:
            message_to_screen("Fuel available: {}".format(self.game.ship1.feul), screen, width*0.06, heigth*0.25, 18)
            message_to_screen("Fuel available: {}".format(self.game.ship2.feul), screen, width*0.06, heigth*0.56, 18)
            message_to_screen("Fuel available: {}".format(self.game.ship3.feul), screen, width*0.06, heigth*0.88, 18)
        if self.turn.turn_number % 2 == 1:
            message_to_screen("Fuel available: {}".format(self.game.ship4.feul), screen, width*0.06, heigth*0.25, 18)
            message_to_screen("Fuel available: {}".format(self.game.ship5.feul), screen, width*0.06, heigth*0.56, 18)
            message_to_screen("Fuel available: {}".format(self.game.ship6.feul), screen, width*0.06, heigth*0.88, 18)



        #aanval van de schepen
        mouse_button_pressed(self.game.ship1.lead_x,self.game.ship1.lead_y,30,133,screen,self.emptyimage,self.game.events)
        mouse_button_pressed(self.game.ship2.lead_x, self.game.ship2.lead_y, 20, 100, screen, self.emptyimage,
                             self.game.events)
        mouse_button_pressed(self.game.ship3.lead_x, self.game.ship3.lead_y, 20, 100, screen, self.emptyimage,
                             self.game.events)
        mouse_button_pressed(self.game.ship4.lead_x, self.game.ship4.lead_y, 30, 133, screen, self.emptyimage,
                             self.game.events)
        mouse_button_pressed(self.game.ship5.lead_x, self.game.ship5.lead_y, 20, 100, screen, self.emptyimage,
                             self.game.events)
        mouse_button_pressed(self.game.ship6.lead_x, self.game.ship6.lead_y, 20, 100, screen, self.emptyimage,
                             self.game.events)

        #amount of attacks

        #attack of boats --------------------------------------------------------------------------------------------------


        def subtract_health_1(self,screen):
            self.game.ship1.hp -= 1
            healthoff(self)

        def subtract_health_2(self,screen):
            self.game.ship2.hp -= 1
            healthoff(self)

        def subtract_health_3(self,screen):
            self.game.ship3.hp -= 1
            healthoff(self)

        def subtract_health_4(self,screen):
            self.game.ship4.hp -= 1
            healthoff(self)

        def subtract_health_5(self,screen):
            self.game.ship5.hp -= 1
            healthoff(self)

        def subtract_health_6(self,screen):
            self.game.ship6.hp -= 1
            healthoff(self)

        if self.turn.turn_number%2 == 1:
            if self.game.ship4.lead_y - self.game.ship4.height - (self.block_size_up_down*3)<self.game.ship1.lead_y and self.game.ship4.lead_x >= self.game.ship1.lead_x and self.game.ship4.lead_x < self.game.ship1.lead_x + self.game.ship1.width and self.game.ship4.lead_y-10+self.game.ship4.height>self.game.ship1.lead_y or self.game.ship4.lead_x + self.game.ship4.width + (self.block_size*3)>self.game.ship1.lead_x and self.game.ship4.lead_x < self.game.ship1.lead_x + self.game.ship1.width and self.game.ship4.lead_y <= self.game.ship1.lead_y+self.game.ship1.height and self.game.ship4.lead_y-10+self.game.ship4.height>self.game.ship1.lead_y or self.game.ship4.lead_x - (self.block_size*3) < self.game.ship1.lead_x+self.game.ship1.width and self.game.ship4.lead_x+-5>self.game.ship1.lead_x and self.game.ship4.lead_y <= self.game.ship1.lead_y + self.game.ship1.height and self.game.ship4.lead_y-10+self.game.ship4.height>self.game.ship1.lead_y:
                if self.game.ship4.attack_p >= 1 and self.game.ship4.hp>0:
                    mouse_button_pressed(width * 0.09, heigth * 0.13, 170, 90, screen, self.attack_button, self.game.events,lambda:subtract_health_1(self,screen))

            if self.game.ship4.lead_y - self.game.ship4.height - (self.block_size_up_down*2)<self.game.ship2.lead_y and self.game.ship4.lead_x >= self.game.ship2.lead_x and self.game.ship4.lead_x < self.game.ship2.lead_x + self.game.ship2.width and self.game.ship4.lead_y-30+self.game.ship4.height>self.game.ship2.lead_y or self.game.ship4.lead_x + self.game.ship4.width + (self.block_size*3)>self.game.ship2.lead_x and self.game.ship4.lead_x < self.game.ship2.lead_x + self.game.ship2.width and self.game.ship4.lead_y <= self.game.ship2.lead_y+self.game.ship2.height  and self.game.ship4.lead_y-10+self.game.ship4.height>self.game.ship2.lead_y or self.game.ship4.lead_x - (self.block_size*3) < self.game.ship2.lead_x+self.game.ship2.width and self.game.ship4.lead_x+-5>self.game.ship2.lead_x and self.game.ship4.lead_y <= self.game.ship2.lead_y + self.game.ship2.height and self.game.ship4.lead_y-10+self.game.ship4.height>self.game.ship2.lead_y:
                if self.game.ship4.attack_p >= 1 and self.game.ship4.hp>0:
                    mouse_button_pressed(width * 0.09, heigth * 0.13, 170, 90, screen, self.attack_button, self.game.events,lambda: subtract_health_2(self, screen))

            if self.game.ship4.lead_y - self.game.ship4.height - (self.block_size_up_down*2)<self.game.ship3.lead_y and self.game.ship4.lead_x >= self.game.ship3.lead_x and self.game.ship4.lead_x < self.game.ship3.lead_x + self.game.ship3.width and self.game.ship4.lead_y-10+self.game.ship4.height>self.game.ship3.lead_y or self.game.ship4.lead_x + self.game.ship4.width + (self.block_size*3)>self.game.ship3.lead_x and self.game.ship4.lead_x < self.game.ship3.lead_x + self.game.ship3.width and self.game.ship4.lead_y <= self.game.ship3.lead_y+self.game.ship3.height and self.game.ship4.lead_y-10+self.game.ship4.height>self.game.ship3.lead_y or self.game.ship4.lead_x - (self.block_size*3) < self.game.ship3.lead_x+self.game.ship3.width and self.game.ship4.lead_x+-5>self.game.ship3.lead_x and self.game.ship4.lead_y <= self.game.ship3.lead_y + self.game.ship3.height and self.game.ship4.lead_y-10+self.game.ship4.height>self.game.ship3.lead_y:
                if self.game.ship4.attack_p >= 1 and self.game.ship4.hp>0:
                    mouse_button_pressed(width * 0.09, heigth * 0.13, 170, 90, screen, self.attack_button, self.game.events,lambda:subtract_health_3(self,screen))


            if self.game.ship5.lead_y - self.game.ship5.height - (self.block_size_up_down*3)<self.game.ship1.lead_y and self.game.ship5.lead_x >= self.game.ship1.lead_x and self.game.ship5.lead_x < self.game.ship1.lead_x + self.game.ship1.width and self.game.ship5.lead_y-10+self.game.ship5.height>self.game.ship1.lead_y or self.game.ship5.lead_x + self.game.ship5.width + (self.block_size*2)>self.game.ship1.lead_x and self.game.ship5.lead_x < self.game.ship1.lead_x + self.game.ship1.width and self.game.ship5.lead_y <= self.game.ship1.lead_y+self.game.ship1.height and self.game.ship5.lead_y-10+self.game.ship5.height>self.game.ship1.lead_y or self.game.ship5.lead_x - (self.block_size*2) < self.game.ship1.lead_x+self.game.ship1.width and self.game.ship5.lead_x+-5>self.game.ship1.lead_x and self.game.ship5.lead_y <= self.game.ship1.lead_y + self.game.ship1.height and self.game.ship5.lead_y-10+self.game.ship5.height>self.game.ship1.lead_y:
                if self.game.ship5.attack_p >= 1 and self.game.ship5.hp>0:
                 mouse_button_pressed(width * 0.09, heigth * 0.435, 170, 90, screen, self.attack_button, self.game.events,lambda:subtract_health_1(self,screen))

            if self.game.ship5.lead_y - self.game.ship5.height - (self.block_size_up_down * 2) < self.game.ship2.lead_y and self.game.ship5.lead_x >= self.game.ship2.lead_x and self.game.ship5.lead_x < self.game.ship2.lead_x + self.game.ship2.width and self.game.ship5.lead_y - 10 + self.game.ship5.height > self.game.ship2.lead_y or self.game.ship5.lead_x + self.game.ship5.width + (self.block_size * 2) > self.game.ship2.lead_x and self.game.ship5.lead_x < self.game.ship2.lead_x + self.game.ship2.width and self.game.ship5.lead_y <= self.game.ship2.lead_y + self.game.ship2.height and self.game.ship5.lead_y - 10 + self.game.ship5.height > self.game.ship2.lead_y or self.game.ship5.lead_x - (self.block_size * 2) < self.game.ship2.lead_x + self.game.ship2.width and self.game.ship5.lead_x + -5 > self.game.ship2.lead_x and self.game.ship5.lead_y <= self.game.ship2.lead_y + self.game.ship2.height and self.game.ship5.lead_y - 10 + self.game.ship5.height > self.game.ship2.lead_y:
                if self.game.ship5.attack_p >= 1 and self.game.ship5.hp>0:
                 mouse_button_pressed(width * 0.09, heigth * 0.435, 170, 90, screen, self.attack_button,self.game.events, lambda: subtract_health_1(self, screen))

            if self.game.ship5.lead_y - self.game.ship5.height - (self.block_size_up_down * 2) < self.game.ship3.lead_y and self.game.ship5.lead_x >= self.game.ship3.lead_x and self.game.ship5.lead_x < self.game.ship3.lead_x + self.game.ship3.width and self.game.ship5.lead_y - 10 + self.game.ship5.height > self.game.ship3.lead_y or self.game.ship5.lead_x + self.game.ship5.width + (self.block_size * 2) > self.game.ship3.lead_x and self.game.ship5.lead_x < self.game.ship3.lead_x + self.game.ship3.width and self.game.ship5.lead_y <= self.game.ship3.lead_y + self.game.ship3.height and self.game.ship5.lead_y - 10 + self.game.ship5.height > self.game.ship3.lead_y or self.game.ship5.lead_x - (self.block_size * 2) < self.game.ship3.lead_x + self.game.ship3.width and self.game.ship5.lead_x + -5 > self.game.ship3.lead_x and self.game.ship5.lead_y <= self.game.ship3.lead_y + self.game.ship3.height and self.game.ship5.lead_y - 10 + self.game.ship5.height > self.game.ship3.lead_y:
                if self.game.ship5.attack_p >= 1 and self.game.ship5.hp>0:
                 mouse_button_pressed(width * 0.09, heigth * 0.435, 170, 90, screen, self.attack_button,self.game.events, lambda: subtract_health_1(self, screen))


            if self.game.ship6.lead_y - self.game.ship6.height - (self.block_size_up_down * 3) < self.game.ship1.lead_y and self.game.ship6.lead_x >= self.game.ship1.lead_x and self.game.ship6.lead_x < self.game.ship1.lead_x + self.game.ship1.width and self.game.ship6.lead_y - 10 + self.game.ship6.height > self.game.ship1.lead_y or self.game.ship6.lead_x + self.game.ship6.width + (self.block_size * 2) > self.game.ship1.lead_x and self.game.ship6.lead_x < self.game.ship1.lead_x + self.game.ship1.width and self.game.ship6.lead_y <= self.game.ship1.lead_y + self.game.ship1.height and self.game.ship6.lead_y - 10 + self.game.ship6.height > self.game.ship1.lead_y or self.game.ship6.lead_x - (self.block_size * 2) < self.game.ship1.lead_x + self.game.ship1.width and self.game.ship6.lead_x + -5 > self.game.ship1.lead_x and self.game.ship6.lead_y <= self.game.ship1.lead_y + self.game.ship1.height and self.game.ship6.lead_y - 10 + self.game.ship6.height > self.game.ship1.lead_y:
                if self.game.ship6.attack_p >= 1 and self.game.ship6.hp>0:
                 mouse_button_pressed(width * 0.09, heigth * 0.744, 170, 90, screen, self.attack_button,self.game.events, lambda: subtract_health_1(self, screen))

            if self.game.ship6.lead_y - self.game.ship6.height - (self.block_size_up_down * 2) < self.game.ship2.lead_y and self.game.ship6.lead_x >= self.game.ship2.lead_x and self.game.ship6.lead_x < self.game.ship2.lead_x + self.game.ship2.width and self.game.ship6.lead_y - 10 + self.game.ship6.height > self.game.ship2.lead_y or self.game.ship6.lead_x + self.game.ship6.width + (self.block_size * 2) > self.game.ship2.lead_x and self.game.ship6.lead_x < self.game.ship2.lead_x + self.game.ship2.width and self.game.ship6.lead_y <= self.game.ship2.lead_y + self.game.ship2.height and self.game.ship6.lead_y - 10 + self.game.ship6.height > self.game.ship2.lead_y or self.game.ship6.lead_x - (self.block_size * 2) < self.game.ship2.lead_x + self.game.ship2.width and self.game.ship6.lead_x + -5 > self.game.ship2.lead_x and self.game.ship6.lead_y <= self.game.ship2.lead_y + self.game.ship2.height and self.game.ship6.lead_y - 10 + self.game.ship6.height > self.game.ship2.lead_y:
                if self.game.ship6.attack_p >= 1 and self.game.ship6.hp>0:
                 mouse_button_pressed(width * 0.09, heigth * 0.744, 170, 90, screen, self.attack_button,self.game.events, lambda: subtract_health_1(self, screen))

            if self.game.ship6.lead_y - self.game.ship6.height - (self.block_size_up_down * 2) < self.game.ship3.lead_y and self.game.ship6.lead_x >= self.game.ship3.lead_x and self.game.ship6.lead_x < self.game.ship3.lead_x + self.game.ship3.width and self.game.ship6.lead_y - 10 + self.game.ship6.height > self.game.ship3.lead_y or self.game.ship6.lead_x + self.game.ship6.width + (self.block_size * 2) > self.game.ship3.lead_x and self.game.ship6.lead_x < self.game.ship3.lead_x + self.game.ship3.width and self.game.ship6.lead_y <= self.game.ship3.lead_y + self.game.ship3.height and self.game.ship6.lead_y - 10 + self.game.ship6.height > self.game.ship3.lead_y or self.game.ship6.lead_x - (self.block_size * 2) < self.game.ship3.lead_x + self.game.ship3.width and self.game.ship6.lead_x + -5 > self.game.ship3.lead_x and self.game.ship6.lead_y <= self.game.ship3.lead_y + self.game.ship3.height and self.game.ship6.lead_y - 10 + self.game.ship6.height > self.game.ship3.lead_y:
                if self.game.ship6.attack_p >= 1 and self.game.ship6.hp>0:
                 mouse_button_pressed(width * 0.09, heigth * 0.744, 170, 90, screen, self.attack_button,self.game.events, lambda: subtract_health_1(self, screen))





        elif self.turn.turn_number %2 == 0:
            if self.game.ship1.lead_y + self.game.ship1.height + (self.block_size_up_down*3)> self.game.ship4.lead_y and self.game.ship1.lead_x+10 >= self.game.ship4.lead_x and self.game.ship1.lead_x < self.game.ship4.lead_x + self.game.ship4.width and self.game.ship1.lead_y  +self.game.ship1.height<=self.game.ship4.lead_y or self.game.ship1.lead_x+self.game.ship1.width+(self.block_size*3)>self.game.ship4.lead_x and self.game.ship1.lead_x+self.game.ship1.width<self.game.ship4.lead_x and self.game.ship1.lead_y+self.game.ship1.height>= self.game.ship4.lead_y and self.game.ship1.lead_y-self.game.ship1.height <=self.game.ship4.lead_y-10 or self.game.ship1.lead_x - (self.block_size*3)<self.game.ship4.lead_x and self.game.ship1.lead_x>self.game.ship4.lead_x and self.game.ship1.lead_y+self.game.ship1.height>self.game.ship4.lead_y and self.game.ship1.lead_y<self.game.ship4.lead_y+self.game.ship4.height-10:
                 if self.game.ship1.attack_p >= 1 and self.game.ship1.hp>0:
                    mouse_button_pressed(width * 0.09, heigth * 0.13, 170, 90, screen, self.attack_button, self.game.events,
                                      lambda: subtract_health_4(self, screen))
            if self.game.ship1.lead_y + self.game.ship1.height + (self.block_size_up_down * 3) > self.game.ship5.lead_y and self.game.ship1.lead_x + 10 >= self.game.ship5.lead_x and self.game.ship1.lead_x < self.game.ship5.lead_x + self.game.ship5.width and self.game.ship1.lead_y   + self.game.ship1.height <= self.game.ship5.lead_y or self.game.ship1.lead_x + self.game.ship1.width + (self.block_size * 3) > self.game.ship5.lead_x and self.game.ship1.lead_x + self.game.ship1.width < self.game.ship5.lead_x  and self.game.ship1.lead_y+self.game.ship1.height>= self.game.ship5.lead_y and self.game.ship1.lead_y-self.game.ship1.height < self.game.ship5.lead_y -40  or self.game.ship1.lead_x - (self.block_size * 3) < self.game.ship5.lead_x and self.game.ship1.lead_x > self.game.ship5.lead_x and self.game.ship1.lead_y + self.game.ship1.height > self.game.ship5.lead_y and self.game.ship1.lead_y < self.game.ship5.lead_y + self.game.ship5.height -10:
                if self.game.ship1.attack_p >= 1 and self.game.ship1.hp>0:
                     mouse_button_pressed(width * 0.09, heigth * 0.13, 170, 90, screen, self.attack_button,
                                          self.game.events,
                                          lambda: subtract_health_5(self, screen))
            if self.game.ship1.lead_y + self.game.ship1.height + (self.block_size_up_down * 3) > self.game.ship6.lead_y and self.game.ship1.lead_x + 10 >= self.game.ship6.lead_x and self.game.ship1.lead_x < self.game.ship6.lead_x + self.game.ship6.width and self.game.ship1.lead_y + self.game.ship1.height <= self.game.ship6.lead_y or self.game.ship1.lead_x + self.game.ship1.width + (self.block_size * 3) > self.game.ship6.lead_x and self.game.ship1.lead_x + self.game.ship1.width < self.game.ship6.lead_x and self.game.ship1.lead_y + self.game.ship1.height >= self.game.ship6.lead_y and self.game.ship1.lead_y - self.game.ship1.height < self.game.ship6.lead_y - 40 or self.game.ship1.lead_x - (self.block_size * 3) < self.game.ship6.lead_x and self.game.ship1.lead_x > self.game.ship6.lead_x and self.game.ship1.lead_y + self.game.ship1.height > self.game.ship6.lead_y and self.game.ship1.lead_y < self.game.ship6.lead_y + self.game.ship6.height - 10:
                if self.game.ship1.attack_p >= 1 and self.game.ship1.hp>0:
                     mouse_button_pressed(width * 0.09, heigth * 0.13, 170, 90, screen, self.attack_button,self.game.events,lambda: subtract_health_6(self, screen))


            if self.game.ship2.lead_y + self.game.ship2.height + (self.block_size_up_down * 2) > self.game.ship6.lead_y and self.game.ship2.lead_x + 10 >= self.game.ship6.lead_x and self.game.ship2.lead_x < self.game.ship6.lead_x + self.game.ship6.width and self.game.ship2.lead_y + self.game.ship2.height <= self.game.ship6.lead_y or self.game.ship2.lead_x + self.game.ship2.width + (self.block_size * 2) > self.game.ship6.lead_x and self.game.ship2.lead_x + self.game.ship2.width < self.game.ship6.lead_x and self.game.ship2.lead_y + self.game.ship2.height >= self.game.ship6.lead_y and self.game.ship2.lead_y - self.game.ship2.height < self.game.ship6.lead_y -20or self.game.ship2.lead_x - (self.block_size * 2) < self.game.ship6.lead_x and self.game.ship2.lead_x > self.game.ship6.lead_x and self.game.ship2.lead_y + self.game.ship2.height > self.game.ship6.lead_y and self.game.ship2.lead_y < self.game.ship6.lead_y + self.game.ship6.height - 10:
                if self.game.ship2.attack_p >= 1 and self.game.ship2.hp>0:
                    mouse_button_pressed(width * 0.09, heigth * 0.435, 170, 90, screen, self.attack_button,
                                              self.game.events, lambda: subtract_health_6(self, screen))

            if self.game.ship2.lead_y + self.game.ship2.height + (self.block_size_up_down * 2) > self.game.ship5.lead_y and self.game.ship2.lead_x + 10 >= self.game.ship5.lead_x and self.game.ship2.lead_x < self.game.ship5.lead_x + self.game.ship5.width and self.game.ship2.lead_y + self.game.ship2.height <= self.game.ship5.lead_y or self.game.ship2.lead_x + self.game.ship2.width + (self.block_size * 2) > self.game.ship5.lead_x and self.game.ship2.lead_x + self.game.ship2.width < self.game.ship5.lead_x and self.game.ship2.lead_y + self.game.ship2.height >= self.game.ship5.lead_y and self.game.ship2.lead_y - self.game.ship2.height < self.game.ship5.lead_y - 20 or self.game.ship2.lead_x - (self.block_size * 2) < self.game.ship5.lead_x and self.game.ship2.lead_x > self.game.ship5.lead_x and self.game.ship2.lead_y + self.game.ship2.height > self.game.ship5.lead_y and self.game.ship2.lead_y < self.game.ship5.lead_y + self.game.ship5.height - 10:
                if self.game.ship2.attack_p >= 1 and self.game.ship2.hp>0 :
                    mouse_button_pressed(width * 0.09, heigth * 0.435, 170, 90, screen, self.attack_button,
                                             self.game.events, lambda: subtract_health_5(self, screen))

            if self.game.ship2.lead_y + self.game.ship2.height + (self.block_size_up_down * 2) > self.game.ship4.lead_y and self.game.ship2.lead_x + 10 >= self.game.ship4.lead_x and self.game.ship2.lead_x < self.game.ship4.lead_x + self.game.ship4.width and self.game.ship2.lead_y + self.game.ship2.height  <= self.game.ship4.lead_y  or self.game.ship2.lead_x + self.game.ship2.width + (self.block_size * 2) > self.game.ship4.lead_x and self.game.ship2.lead_x + self.game.ship2.width < self.game.ship4.lead_x and self.game.ship2.lead_y + self.game.ship2.height  >= self.game.ship4.lead_y and self.game.ship2.lead_y - self.game.ship2.height - 30 < self.game.ship4.lead_y - 20 or self.game.ship2.lead_x - (self.block_size * 2) < self.game.ship4.lead_x and self.game.ship2.lead_x > self.game.ship4.lead_x and self.game.ship2.lead_y + self.game.ship2.height > self.game.ship4.lead_y and self.game.ship2.lead_y < self.game.ship4.lead_y + self.game.ship4.height - 10:
                if self.game.ship2.attack_p >= 1 and self.game.ship2.hp>0:
                    mouse_button_pressed(width * 0.09, heigth * 0.435, 170, 90, screen, self.attack_button,
                                                 self.game.events, lambda: subtract_health_4(self, screen))

            if self.game.ship3.lead_y + self.game.ship3.height + (self.block_size_up_down * 2) > self.game.ship4.lead_y and self.game.ship3.lead_x + 10 >= self.game.ship4.lead_x and self.game.ship3.lead_x < self.game.ship4.lead_x + self.game.ship4.width and self.game.ship3.lead_y + self.game.ship3.height <= self.game.ship4.lead_y or self.game.ship3.lead_x + self.game.ship3.width + (self.block_size * 2) > self.game.ship4.lead_x and self.game.ship3.lead_x + self.game.ship3.width < self.game.ship4.lead_x and self.game.ship3.lead_y + self.game.ship3.height >= self.game.ship4.lead_y and self.game.ship3.lead_y - self.game.ship3.height < self.game.ship4.lead_y  or self.game.ship3.lead_x - (self.block_size * 2) < self.game.ship4.lead_x and self.game.ship3.lead_x > self.game.ship4.lead_x and self.game.ship3.lead_y + self.game.ship3.height > self.game.ship4.lead_y and self.game.ship3.lead_y < self.game.ship4.lead_y + self.game.ship4.height - 10:
                if self.game.ship3.attack_p >= 1 and self.game.ship3.hp>0:
                    mouse_button_pressed(width * 0.09, heigth * 0.744, 170, 90, screen, self.attack_button,
                                             self.game.events, lambda: subtract_health_4(self, screen))

            if self.game.ship3.lead_y + self.game.ship3.height + (self.block_size_up_down * 2) > self.game.ship5.lead_y and self.game.ship3.lead_x + 10 >= self.game.ship5.lead_x and self.game.ship3.lead_x < self.game.ship5.lead_x + self.game.ship5.width and self.game.ship3.lead_y + self.game.ship3.height <= self.game.ship5.lead_y or self.game.ship3.lead_x + self.game.ship3.width + (self.block_size * 2) > self.game.ship5.lead_x and self.game.ship3.lead_x + self.game.ship3.width < self.game.ship5.lead_x and self.game.ship3.lead_y + self.game.ship3.height >= self.game.ship5.lead_y and self.game.ship3.lead_y - self.game.ship3.height < self.game.ship5.lead_y -20 or self.game.ship3.lead_x - (self.block_size * 2) < self.game.ship5.lead_x and self.game.ship3.lead_x > self.game.ship5.lead_x and self.game.ship3.lead_y + self.game.ship3.height > self.game.ship5.lead_y and self.game.ship3.lead_y < self.game.ship5.lead_y + self.game.ship5.height - 10:
                if self.game.ship3.attack_p >= 1 and self.game.ship3.hp>0:
                    mouse_button_pressed(width * 0.09, heigth * 0.744, 170, 90, screen, self.attack_button,
                                                 self.game.events, lambda: subtract_health_5(self, screen))

            if self.game.ship3.lead_y + self.game.ship3.height + (self.block_size_up_down * 2) > self.game.ship6.lead_y and self.game.ship3.lead_x + 10 >= self.game.ship6.lead_x and self.game.ship3.lead_x < self.game.ship6.lead_x + self.game.ship6.width and self.game.ship3.lead_y + self.game.ship3.height <= self.game.ship6.lead_y or self.game.ship3.lead_x + self.game.ship3.width + (self.block_size * 2) > self.game.ship6.lead_x and self.game.ship3.lead_x + self.game.ship3.width < self.game.ship6.lead_x and self.game.ship3.lead_y + self.game.ship3.height >= self.game.ship6.lead_y and self.game.ship3.lead_y - self.game.ship3.height < self.game.ship6.lead_y - 20 or self.game.ship3.lead_x - (self.block_size * 2) < self.game.ship6.lead_x and self.game.ship3.lead_x > self.game.ship6.lead_x and self.game.ship3.lead_y + self.game.ship3.height > self.game.ship6.lead_y and self.game.ship3.lead_y < self.game.ship6.lead_y + self.game.ship6.height - 10:
                if self.game.ship3.attack_p >= 1 and self.game.ship3.hp>0:
                    mouse_button_pressed(width * 0.09, heigth * 0.744, 170, 90, screen, self.attack_button,
                                                     self.game.events, lambda: subtract_health_6(self, screen))



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
        screen.blit(self.title, (width*0.25, heigth*0.15))
        mouse_button_pressed(width*0.4, heigth*0.5, 250, 50, screen, self.pbuttom,self.game.events,
                             lambda: self.game.set_state(self.game.game_main))
        mouse_button_pressed(width*0.4, heigth*0.8, 250, 50, screen, self.qbuttom,self.game.events,
                             lambda: sys.exit())
        mouse_button_pressed(width*0.4, heigth*0.6, 250, 50, screen, self.ibuttom,self.game.events)
        mouse_button_pressed(width * 0.4, heigth * 0.7, 250, 50, screen, self.bmenu,self.game.events,
                             lambda : self.game.set_state(self.game.intro_game))

class Turn:
    def __init__(self):
        self.turn_number = 0
        self.boats = Boats
        self.flag_a=pygame.image.load("flag_a.png")
        self.flag_a=pygame.transform.scale(self.flag_a,[80,60])
        self.flag_r=pygame.image.load("flag_r.png")
        self.flag_r = pygame.transform.scale(self.flag_r, [80,60])
        self.range = pygame.image.load("range.png")
        self.range = pygame.transform.scale(self.range,[100,100])

    def update(self):
        self.turn_number += 1

    def draw(self,screen):
        message_to_screen("current Turn:",screen,width*0.85,heigth*0.85,20)
        if self.turn_number == 0:
            screen.blit(self.flag_a,(width*0.7,heigth*0.435))
            message_to_screen("Move your ships in position America!",screen,width/2.15,heigth/2.1,30)
        elif self.turn_number == 1:
            message_to_screen("Move your ships in position Russia!",screen,width/2.15,heigth/2.1,30)
            screen.blit(self.flag_r, (width * 0.7, heigth *0.435))
        elif self.turn_number %2 == 0:
            screen.blit(self.flag_a, (width * 0.92, heigth *0.79))
        elif self.turn_number %2 == 1:
            screen.blit(self.flag_r, (width * 0.92, heigth *0.79))

class Player:
    def __init__(self,boats):
        self.game = Game
        self.boats = boats
        self.player = Player

class Cards:
    def __init__(self,turn,game):
        self.game = game
        self.turn = turn
        self.cardat = pygame.image.load("offensive_back.png")
        self.cardat = pygame.transform.scale(self.cardat, [90,150])
        self.carda1 = pygame.image.load("Attack.png")
        self.carda1 = pygame.transform.scale(self.carda1, [90, 150])
        self.cardd = pygame.image.load("defensive_back.png")
        self.cardd = pygame.transform.scale(self.cardd, [90, 150])
        self.cardsp = pygame.image.load("special_back.png")
        self.cardsp = pygame.transform.scale(self.cardsp, [90, 150])
        self.cardh = pygame.image.load("help_back.png")
        self.cardh = pygame.transform.scale(self.cardh, [90, 150])
        self.attack_cards_choice = None

    def draw (self,screen):
        if self.game.turn_number >=2:
            screen.blit(self.cardat,(width*0.82,heigth*0.04))
            screen.blit(self.cardd, (width * 0.92, heigth * 0.04))
            screen.blit(self.cardh, (width * 0.82, heigth * 0.28))
            screen.blit(self.cardsp, (width * 0.92, heigth * 0.28))

    def attack_cards(self):
        attackcards = [self.carda1]
        self.attack_cards_choice = random.choice(attackcards)

def mouse_button_pressed(x, y, w, h, screen, image_original, events, action=None):
    screen.blit(image_original, [x, y])
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and action != None:
                action()

def text_objects(text,font):
    textSurface = font.render (text,True, (250,0,0))
    return textSurface, textSurface.get_rect()

def message_to_screen(text,screen,x,y,size):
    largeText = pygame.font.Font("freesansbold.ttf",size)
    textsuf , textrect = text_objects(text,largeText)
    textrect.center = ((x),(y))
    screen.blit(textsuf,textrect)

def run():
    game = Game()
    game.loop_of_game()
run()




