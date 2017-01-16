#import required modules
import pygame

class Game():
    def __init__(self):
        #define colors
        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        black = (0,0,0)

        #hoogte en breedte van het scherm
        width = 800
        heigth = 600
        size = (width,heigth)

        #standard initialisation of pygame
        pygame.init()

        #Weergaven van het scherm
        self.screen = pygame.display.set_mode(size)

    def visual_display(self):
        self.screen.fill((0,0,0))


        pygame.display.flip()

    #loop voor het laten runnen van het spel
    def loop_of_game(self):
        while not Close_game():
            self.visual_display()

#sluiten van game via kruisje
def Close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

def program():
    game=Game()
    game.loop_of_game()


#run the program
program()