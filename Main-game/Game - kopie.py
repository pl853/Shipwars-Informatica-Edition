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
        self.cards= Cards (self,self.turn)
        self.screen = pygame.display.set_mode((size))
        self.intro_game = IntroGame(self)
        self.game_main = GameMain(self,self.turn)
        self.pause_menu = PauseMenu(self)
        self.ship1 = Boats(heigth*0.1, width*0.16,30,133,"boat1",3,3,"battleship1.png",self.turn)
        self.ship2 = Boats(heigth*0.43,width*0.16,20,100,"boat2",3,3,"battleship2.png",self.turn)
        self.ship3 = Boats(heigth * 0.75,width*0.16,20,100,"boat3",3,3,"battleship.png",self.turn)
        self.ship4 = Boats(heigth * 0.1, width * 0.16, 30, 130, "boat1", 3, 3, "battleship5.png",self.turn)
        self.ship5 = Boats(heigth * 0.43, width * 0.16, 20, 100, "boat2", 3, 3, "battleship6.png",self.turn)
        self.ship6 = Boats(heigth * 0.75, width * 0.16, 20, 100, "boat3", 3, 3, "battleship4.png",self.turn)
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
            self.draw()
            for event in self.events:
                if event.type == pygame.QUIT:
                    quit()

class Boats:
    def __init__(self, lead_x, lead_y, width,height,naam,hp,armor, image,turn):
        self.game = Game
        self.turn = turn
        self.width = width
        self.height = height
        self.lead_x = lead_y
        self.lead_y = lead_x
        self.hp = hp
        self.armor = armor
        self.block_size = 32.8
        self.block_size_up_down = 33.333
        self.naam = naam
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [width, height])


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
    def __init__(self, game , turn):
        self.button_test = False
        self.cards_shown = False
        self.pause_menu = PauseMenu
        self.game = game
        self.turn= turn
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
        self.greenline = pygame.image.load("redline.png")
        self.greenline = pygame.transform.scale(self.greenline, [320, 200])
        self.ihealth = pygame.image.load("healthon.png")
        self.ihealth = pygame.transform.scale(self.ihealth, [30, 30])
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

    def update(self):
        drag = 0
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if self.game.state == self.game.game_main:
            if keys[pygame.K_ESCAPE]:
                self.game.set_state(self.game.pause_menu)

            elif click[0] == 1 and self.game.ship1.lead_x + (self.game.ship1.width+10) > mouse[0] > self.game.ship1.lead_x and self.game.ship1.lead_y + (self.game.ship1.height+10) > mouse[1] > self.game.ship1.lead_y: # asking if i am within the boundaries of the image
                drag = 1  # and if the left button is pressed
            elif click[0] == 1 and self.game.ship2.lead_x + (self.game.ship2.width+10) > mouse[0] > self.game.ship2.lead_x and self.game.ship2.lead_y + (self.game.ship2.height+10) > mouse[1] > self.game.ship2.lead_y: # asking if i am within the boundaries of the image
                drag = 2  # and if the left button is pressed
            elif click[0] == 1 and self.game.ship3.lead_x + (self.game.ship3.width+10) > mouse[0] > self.game.ship3.lead_x and self.game.ship3.lead_y + (self.game.ship3.height+10) > mouse[1] > self.game.ship3.lead_y: # asking if i am within the boundaries of the image
                drag = 3  # and if the left button is pressed
            elif click[0] == 1 and self.game.ship4.lead_x + (self.game.ship1.width+10) > mouse[0] > self.game.ship4.lead_x and self.game.ship4.lead_y + (self.game.ship4.height+10) > mouse[1] > self.game.ship4.lead_y: # asking if i am within the boundaries of the image
                drag = 4  # and if the left button is pressed
            elif click[0] == 1 and self.game.ship5.lead_x + (self.game.ship2.width+10) > mouse[0] > self.game.ship5.lead_x and self.game.ship5.lead_y + (self.game.ship5.height+10) > mouse[1] > self.game.ship5.lead_y: # asking if i am within the boundaries of the image
                drag = 5  # and if the left button is pressed
            elif click[0] == 1 and self.game.ship6.lead_x + (self.game.ship3.width+10) > mouse[0] > self.game.ship6.lead_x and self.game.ship6.lead_y + (self.game.ship6.height+10) > mouse[1] > self.game.ship6.lead_y: # asking if i am within the boundaries of the image
                drag = 6  # and if the left button is pressed

            if click[0] == 0:  # asking if the left button is pressed
                drag = 0
            elif drag == 1:  # moving the image
                self.game.ship1.lead_x = mouse[0] - (self.game.ship1.width/2)
                self.game.ship1.lead_y = mouse[1] - (self.game.ship1.height/2)
            elif drag == 2:
                self.game.ship2.lead_x = mouse[0] - (self.game.ship2.width / 2)
                self.game.ship2.lead_y = mouse[1] - (self.game.ship2.height / 2)
            elif drag == 3:  # moving the image
                self.game.ship3.lead_x = mouse[0] - (self.game.ship3.width/2)
                self.game.ship3.lead_y = mouse[1] - (self.game.ship3.height/2)
            elif drag == 4:
                self.game.ship4.lead_x = mouse[0] - (self.game.ship4.width / 2)
                self.game.ship4.lead_y = mouse[1] - (self.game.ship4.height / 2)
            elif drag == 5:  # moving the image
                self.game.ship5.lead_x = mouse[0] - (self.game.ship5.width/2)
                self.game.ship5.lead_y = mouse[1] - (self.game.ship5.height/2)
            elif drag == 6:
                self.game.ship6.lead_x = mouse[0] - (self.game.ship6.width / 2)
                self.game.ship6.lead_y = mouse[1] - (self.game.ship6.height / 2)

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
        # screen.blit(self.greenline,(0,heigth*0.28))
        # screen.blit(self.greenline, (0, heigth * 0.60))
        # menu button---------------------------------------------------------------------------------------------
        mouse_button_pressed(width*0.96,heigth*0.01, 50, 50, screen, self.pbutton,self.game.events,
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

        mouse_button_pressed(width * 0.8, heigth * 0.85,250,70,screen,self.next_turn,self.game.events,lambda: next_turn_conf_true())
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

        # placing health button------------------------------------------------------------------------------------
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
        # if self.turn.turn_number % 2 == 0:
        #     mouse_button_pressed(width * 0.82, heigth * 0.19, 170, 90, screen, self.game.events,self.turn.update())

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
        self.turn_number = 0
        self.player = Player
        self.flag_a=pygame.image.load("flag_a.png")
        self.flag_a=pygame.transform.scale(self.flag_a,[80,60])
        self.flag_r=pygame.image.load("flag_r.png")
        self.flag_r = pygame.transform.scale(self.flag_r, [80,60])

    def update(self):
        self.turn_number += 1

    def draw(self,screen):
        message_to_screen("current Turn:",screen,width*0.85,heigth*0.76,20)
        if self.turn_number == 0:
            screen.blit(self.flag_a,(width*0.7,heigth*0.435))
            message_to_screen("Move your ships in position America!",screen,width/2.15,heigth/2.1,30)
        elif self.turn_number == 1:
            message_to_screen("Move your ships in position Russia!",screen,width/2.15,heigth/2.1,30)
            screen.blit(self.flag_r, (width * 0.7, heigth *0.435))
        elif self.turn_number %2 == 0:
            screen.blit(self.flag_a, (width * 0.92, heigth *0.72))
        elif self.turn_number %2 == 1:
            screen.blit(self.flag_r, (width * 0.92, heigth *0.72))

class Player:
    def __init__(self,player1,player2,score,winner):
        self.player1 = player1
        self.player1 = player2
        self.score = score
        self.winner = winner

class Cards:
    def __init__(self,turn,game):
        self.game = game
        self.turn = turn
        self.carda = pygame.image.load("carda.jpg")
        self.carda = pygame.transform.scale(self.carda, [170, 90])
        self.cardd = pygame.image.load("carda.jpg")
        self.cardd = pygame.transform.scale(self.cardd, [70, 70])
        self.cards = pygame.image.load("carda.jpg")
        self.cards = pygame.transform.scale(self.cards, [70, 70])
        self.cardh = pygame.image.load("carda.jpg")
        self.cardh = pygame.transform.scale(self.cardh, [70, 70])

    def draw (self,screen):
        screen.blit(self.carda,(width*0.82,heigth*0.04))
        screen.blit(self.carda, (width * 0.82, heigth * 0.19))
        screen.blit(self.carda, (width * 0.82, heigth * 0.34))
        screen.blit(self.carda, (width * 0.82, heigth * 0.49))


    def showcards(self,screen):
        if self.turn.turn_number%2 ==0:
            screen.blit(self.carda, (width * 0.3, heigth * 0.5))
            screen.blit(self.carda, (width * 0.45, heigth * 0.5))
            screen.blit(self.carda, (width * 0.6, heigth * 0.5))

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






