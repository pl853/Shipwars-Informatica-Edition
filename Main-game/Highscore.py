import pygame
import mysql.connector

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
display_width = 1280
display_height = 720

gameDisplay = pygame.display.set_mode((display_width, display_height))


pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



bg = pygame.image.load("/Users/mitchellneels/Documents/git/Shipwars-Informatica-Edition/Main-game/bg2.jpg").convert()
pygame.draw.rect(bg, black, [427,100,427,500])
pygame.display.set_caption("Highscores")

def draw(self,screen):
    screen.blit(self.bg,(100,100))
    pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_highscore(text):
    largeText = pygame.font.Font('freesansbold.ttf', 10)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width - 437),(display_height-150))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

def highscore():
    message_highscore('Highscores:')

def interact_database(command):
    db = mysql.connector.connect("highscore_database")
    cursor = db.cursor()
    cursor.execute(command)
    db.commit()
    results = None
    try:
        results=cursor.fetchall()
    except mysql.Programming.Error:
        pass
    cursor.close()
    db.close()
    return results

def Upload_Score (name, score):
    return interact_database("UPDATE score SET score = {} WHERE name = '{}' ". format(score, name))

def Download_Score():
   return interact_database("SELECT * FROM score")

def Top_Score():
    result = interact_database("SELECT * FROM score ORDER BY score")[0][1]
    return result




# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    gameDisplay.blit(bg, [0,0])

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


pygame.quit()


class Highscore:
    def __init__(self):
        pygame.init()
        self.bg = pygame.image.load("/Users/mitchellneels/Documents/git/Shipwars-Informatica-Edition/Main-game/bg2.jpg")
        self.bg = pygame.transform.scale(self.bg , [100,100])

    def draw(self,screen):
        screen.blit(self.bg,(100,100))
        pygame.display.update()


    def interact_database(command):
        db = mysql.connector.connect("highscore_database")
        cursor = db.cursor()
        cursor.execute(command)
        db.commit()
        results = None
        try:
            results=cursor.fetchall()
        except mysql.Programming.Error:
            pass
        cursor.close()
        db.close()
        return results

    def Upload_Score (name, score):
        return interact_database("UPDATE score SET score = {} WHERE name = '{}' ". format(score, name))

    def Download_Score():
        return interact_database("SELECT * FROM score")

    def Top_Score():
        result = interact_database("SELECT * FROM score ORDER BY score")[0][1]
        return result









