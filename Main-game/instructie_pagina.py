import pygame
pygame.init()

width = 1280
heigth = 720
size = (width, heigth)

gameDisplay = pygame.display.set_mode(size)


def instructionPage():
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    font = pygame.font.Font(None, 25)
    nextb = pygame.image.load("C:/Users/gebruiker/Downloads/21828-200.png")
    backb = pygame.image.load("C:/Users/gebruiker/Downloads/backb.png")
    bg = pygame.image.load("C:/Users/gebruiker/Downloads/bg2.jpg")
    mb = pygame.image.load("C:/Users/gebruiker/Desktop/movebutton.png")
    defend = pygame.image.load("C:/Users/gebruiker/Desktop/defence.png")
    attack = pygame.image.load("C:/Users/gebruiker/Desktop/attack.png")
    attackb = pygame.image.load("C:/Users/gebruiker/Desktop/attack_button.png")
    hpon = pygame.image.load("C:/Users/gebruiker/Desktop/healthon.png")
    hpoff = pygame.image.load("C:/Users/gebruiker/Desktop/healthoff.png")
    nextt = pygame.image.load("C:/Users/gebruiker/Desktop/next.png")

    def instructionPage5():
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(backb, ((width * 0.03), (heigth * 0.93)))
        def text_objects(text, font, color, bool):
            textSuface = font.render(text, bool, color)
            return textSuface, textSuface.get_rect()

        def message_to_screen(text, x, y, size, color, bool):
            largeText = pygame.font.Font("freesansbold.ttf", size)
            textsuf, textrect = text_objects(text, largeText, color, bool)
            textrect.center = ((x), (y))
            gameDisplay.blit(textsuf, textrect)

        def text(text, x, y, size, color, bool):
            largeText = pygame.font.Font("freesansbold.ttf", size)
            textsuf, textrect = text_objects(text, largeText, color, bool)
            textrect = ((x), (y))
            gameDisplay.blit(textsuf, textrect)

        pageExit = False
        while not pageExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pageExit = True
                message_to_screen("INSTRUCTIONS", width * 0.5, heigth * 0.1, 45, white, True)
                message_to_screen("Functions", width * 0.5, heigth * 0.16, 30, white, True)
                text("move button:", width * 0.02, heigth * 0.21, 15, white, True)
                gameDisplay.blit(mb, ((width * 0.02), (heigth * 0.24)))
                text("This is the move button. This is the button which you can move your boats with",
                     width * 0.07, heigth * 0.27, 15, red, False)
                text("attack button:", width * 0.55, heigth * 0.21, 15, white, True)
                gameDisplay.blit(attackb, ((width * 0.55), (heigth * 0.24)))
                text("This is the attack button. You can attack your opponent's boat",
                     width * 0.60, heigth * 0.27, 15, red, False)
                text("when you press this button.", width * 0.60, heigth * 0.30, 15, red, False)
                text("Defending position:", width * 0.02, heigth * 0.32, 15, white, True)
                gameDisplay.blit(defend, ((width * 0.02), (heigth * 0.35)))
                text("Press this button to switch to the defensive position",
                     width * 0.08, heigth * 0.37, 15, red, False)
                text("attacking position:", width * 0.40, heigth * 0.32, 15, white, True)
                gameDisplay.blit(attack, ((width * 0.40), (heigth * 0.35)))
                text("Press this button to switch to the attacking position",
                     width * 0.46, heigth * 0.37, 15, red, False)
                text("Health on:", width * 0.02, heigth * 0.43, 15, white, True)
                gameDisplay.blit(hpon, ((width * 0.02), (heigth * 0.46)))
                text("This button shows you HP. When it's like this you still have HP left",
                     width * 0.08, heigth * 0.48, 15, red, False)
                text("Health off:", width * 0.48, heigth * 0.43, 15, white, True)
                gameDisplay.blit(hpoff, ((width * 0.48), (heigth * 0.46)))
                text("When the button is shown like this you don't have any HP left",
                     width * 0.53, heigth * 0.48, 15, red, False)
                text("End  your turn:", width * 0.02, heigth * 0.55, 15, white, True)
                gameDisplay.blit(nextt, ((width * 0.02), (heigth * 0.58)))
                text("Press this button when you're done with your turn",
                     width * 0.15, heigth * 0.61, 15, red, False)
                text("press the left key button to go back to page 4", width * 0.08, heigth * 0.95, 23, black, True)
                message_to_screen("5", width * 0.5, heigth * 0.98, 45, white, True)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        instructionPage4()
                pygame.display.update()
        pygame.quit()
        quit()

    def instructionPage4():
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(backb, ((width * 0.03), (heigth * 0.93)))
        gameDisplay.blit(nextb, ((width * 0.93), (heigth * 0.92)))
        def text_objects(text, font, color, bool):
            textSuface = font.render(text, bool, color)
            return textSuface, textSuface.get_rect()

        def message_to_screen(text, x, y, size, color, bool):
            largeText = pygame.font.Font("freesansbold.ttf", size)
            textsuf, textrect = text_objects(text, largeText, color, bool)
            textrect.center = ((x), (y))
            gameDisplay.blit(textsuf, textrect)

        def text(text, x, y, size, color, bool):
            largeText = pygame.font.Font("freesansbold.ttf", size)
            textsuf, textrect = text_objects(text, largeText, color, bool)
            textrect = ((x), (y))
            gameDisplay.blit(textsuf, textrect)
        pageExit = False
        while not pageExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pageExit = True
                message_to_screen("INSTRUCTIONS", width * 0.5, heigth * 0.1, 45, white, True)
                message_to_screen("Rules", width * 0.5, heigth * 0.2, 30, white, True)
                text("1.", width * 0.02, heigth * 0.25, 15, white, True)
                text("      Every player picks 1 card on every turn before the game starts, "
                     "until every player has 2 cards.", width * 0.02, heigth * 0.25, 15, red, False)
                text("2.", width * 0.02, heigth * 0.28, 15, white, True)
                text("      Afterwords, every player will place their boats in turns on the field with the"
                     "backside on the starting line", width * 0.02, heigth * 0.28, 15, red, False)
                text("Changing positions", width * 0.02, heigth * 0.33, 23, white, True)
                text("1.", width * 0.02, heigth * 0.36, 15, white, True)
                text("      When your turn is up you may move all your boats", width * 0.02, heigth * 0.36, 15, red, False)
                text("2.", width * 0.02, heigth * 0.39, 15, white, False)
                text("      You also may change their positions (attack or defence) which will count as one step",
                     width * 0.02, heigth * 0.39, 15, red, False)
                text("      -", width * 0.02, heigth * 0.42, 15, white, False)
                text("          A ship has its regular attacking range when it's in attacking position (vertical)",
                     width * 0.02, heigth * 0.42, 15, red, False)
                text("      -", width * 0.02, heigth * 0.45, 15, white, False)
                text("          When a ship is in its defending position, it's not able to be moved (helpcards will still be active)",
                     width * 0.02, heigth * 0.45, 15, red, False)
                text("3.", width * 0.02, heigth * 0.48, 15, white, True)
                text("      Player can attack 2 times on each turn. Attacking is only possible when your opponent's boat"
                     "is within the attacking range of your boat and every boat can attack only once",
                     width * 0.02, heigth * 0.48, 15, red, False)
                text("Normal cards:", width * 0.02, heigth * 0.53, 15, white, True)
                text("1.", width * 0.02, heigth * 0.56, 15, white, True)
                text("      On the start of every turn the player may pick a card", width * 0.02, heigth * 0.56, 15, red, False)
                text("      -", width * 0.02, heigth * 0.59, 15, white, True)
                text("          When it's a trickcard it should be place on the map with the matching"
                     "field", width * 0.02, heigth * 0.59, 15, red, False)
                text("      -", width * 0.02, heigth * 0.62, 15, white, True)
                text("          a trickcard can be activated at any time. Even when it's the opponent's turn",
                     width * 0.02, heigth * 0.62, 15, red, False)
                text("2.", width * 0.02, heigth * 0.65, 15, white, True)
                text("      A player can have a maximum of 6 cards in his position. The 7th card has to be thrown away",
                     width * 0.02, heigth * 0.65, 15, red, False)
                text("3.", width * 0.02, heigth * 0.68, 15, white, True)
                text("      Players can use a maximum of 2 cards on every turn "
                     "(trickcards are excluded, because they are activated and not used).", width * 0.02, heigth * 0.68, 15, red, False)
                text("4.", width * 0.02, heigth * 0.71, 15, white, True)
                text("      When the set of normal cards is empty, the cards which are thrown away will be used again",
                     width * 0.02, heigth * 0.71, 15, red, False)
                text("Special cards:", width * 0.02, heigth * 0.76, 23, white, True)
                text("~", width * 0.02, heigth * 0.79, 15, white, True)
                text("      A player can pick a special card when he reaches the other side with one of his boats."
                     "When it happens to be a perk card, the card will be assigned to the boat that reached",
                     width * 0.02, heigth * 0.79, 15, red, False)
                text("the other side", width * 0.02, heigth * 0.82, 15, red, False)
                text("Ships:", width * 0.02, heigth * 0.87, 23, white, True)
                text("1.", width * 0.02, heigth * 0.90, 15, white, True)
                text("      When a ship is wrecked, it becomes an obstacle and other ships can't navigate there, "
                     "because they can't ride on obstacles", width * 0.02, heigth * 0.90, 15, red, False)
                text("2.", width * 0.02, heigth * 0.93, 15, white, True)
                text("      A player wins after he defeats all the opponent's ships", width * 0.02, heigth * 0.93, 15, red, False)
                text("press the left key button to go back to page 3", width * 0.08, heigth * 0.95, 23, black, True)
                text("press the right key button to go to page 5", width * 0.56, heigth * 0.95, 23, black, True)
                message_to_screen("4", width * 0.5, heigth * 0.98, 45, white, True)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        instructionPage3()
                    if event.key == pygame.K_RIGHT:
                        instructionPage5()

                pygame.display.update()

        pygame.quit()
        quit()

    def instructionPage3():
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(backb, ((width * 0.03), (heigth * 0.93)))
        gameDisplay.blit(nextb, ((width * 0.93), (heigth * 0.92)))
        def text_objects(text, font, color, bool):
            textSuface = font.render(text, bool, color)
            return textSuface, textSuface.get_rect()

        def message_to_screen(text, x, y, size, color, bool):
            largeText = pygame.font.Font("freesansbold.ttf", size)
            textsuf, textrect = text_objects(text, largeText, color, bool)
            textrect.center = ((x), (y))
            gameDisplay.blit(textsuf, textrect)

        def text(text, x, y, size, color, bool):
            largeText = pygame.font.Font("freesansbold.ttf", size)
            textsuf, textrect = text_objects(text, largeText, color, bool)
            textrect = ((x), (y))
            gameDisplay.blit(textsuf, textrect)
        pageExit = False
        while not pageExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pageExit = True
                message_to_screen("INSTRUCTIONS", width * 0.5, heigth * 0.1, 45, white, True)
                message_to_screen("The cards", width * 0.5, heigth * 0.2, 30, white, True)
                text("Defensive cards:", width * 0.02, heigth * 0.35, 23, white, True)
                text("2x Reinforced Hull:", width * 0.02, heigth * 0.38, 15, white, True)
                text("Adds one HP to one of your boats", width * 0.15, heigth * 0.38, 15, red, False)
                text("4x Sonar:", width * 0.02, heigth * 0.41, 15, white, True)
                text("Choose a coordinate from one of the 9 mines. It will be activated when your opponent has the"
                     "matching card", width * 0.15, heigth * 0.41, 15, red, False)
                text("2x Smokescreen:", width * 0.02, heigth * 0.44, 15, white, True)
                text("This is a trickcard which can be used to block the enemy's attack", width * 0.15, heigth * 0.44, 15, red, False)
                text("2x sabotage:", width * 0.02, heigth * 0.47, 15, white, True)
                text("When you activate this trickcard the enemy's attack will affect his own boat",
                     width * 0.15, heigth * 0.47, 15, red, False)
                text("Help cards:", width * 0.02, heigth * 0.52, 23, white, True)
                text("2x backup:", width * 0.02, heigth * 0.55, 15, white, True)
                text("Pick two cardS", width * 0.15, heigth * 0.55, 15, red, False)
                text("6x Extra Fuel:", width * 0.02, heigth * 0.58, 15, white, True)
                text("Choose one of your ships which will be able to move 2 extra steps", width * 0.15, heigth * 0.58, 15, red, False)
                text("1x Rally:", width * 0.02, heigth * 0.61, 15, white, True)
                text("All your ships may move 1 extra step", width * 0.15, heigth * 0.61, 15, red, False)
                text("4x Adrenaline Rush:", width * 0.02, heigth * 0.64, 15, white, True)
                text("Choose one of your ships. The ship you choose may do another moveset", width * 0.15, heigth * 0.64, 15, red, False)
                text("Special cards:", width * 0.02, heigth * 0.69, 23, white, True)
                text("2x repair:", width * 0.02, heigth * 0.72, 15, white, True)
                text("Choose one of your ships to recover its HP", width * 0.15, heigth * 0.72, 15, red, False)
                text("2x Flack:", width * 0.02, heigth * 0.75, 15, white, True)
                text("This ship can't get any damage from mines", width * 0.15, heigth * 0.75, 15, red, False)
                text("1x Hack Intel:", width * 0.02, heigth * 0.78, 15, white, True)
                text("Choose the first 3 cards of the set of the special cards", width * 0.15, heigth * 0.78, 15, red, False)
                text("1x Far sight:", width * 0.02, heigth * 0.81, 15, white, True)
                text("The ship gets an extra range of +2", width * 0.15, heigth * 0.81, 15, red, False)
                text("1x Aluminium hull:", width * 0.02, heigth * 0.84, 15, white, True)
                text("The ship may do his moveset twice on every turn", width * 0.15, heigth * 0.84, 15, red, False)
                text("1x Jack Sparrow:", width * 0.02, heigth * 0.87, 15, white, True)
                text("The enemy needs to show his cards. You can choose one card to steal "
                     "and one card which he needs to throw away", width * 0.15, heigth * 0.87, 15, red, False)
                text("press the left key button to go back to page 2", width * 0.08, heigth * 0.95, 23, black, True)
                text("press the right key button to go to page 4", width * 0.56, heigth * 0.95, 23, black, True)
                message_to_screen("3", width * 0.5, heigth * 0.98, 45, white, True)
                pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        instructionPage2()
                    if event.key == pygame.K_RIGHT:
                        instructionPage4()

        pygame.quit()
        quit()

    def instructionPage2():
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(backb, ((width * 0.03), (heigth * 0.93)))
        gameDisplay.blit(nextb, ((width * 0.93), (heigth * 0.92)))

        def text_objects(text, font, color, bool):
            textSuface = font.render(text, bool, color)
            return textSuface, textSuface.get_rect()

        def message_to_screen(text, x, y, size, color, bool):
            largeText = pygame.font.Font("freesansbold.ttf", size)
            textsuf, textrect = text_objects(text, largeText, color, bool)
            textrect.center = ((x), (y))
            gameDisplay.blit(textsuf, textrect)

        def text(text, x, y, size, color, bool):
            largeText = pygame.font.Font("freesansbold.ttf", size)
            textsuf, textrect = text_objects(text, largeText, color, bool)
            textrect = ((x), (y))
            gameDisplay.blit(textsuf, textrect)
        pageExit = False
        while not pageExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pageExit = True
                message_to_screen("INSTRUCTIONS", width * 0.5, heigth * 0.1, 45, white, True)
                message_to_screen("The cards", width * 0.5, heigth * 0.2, 30, white, True)
                text("Regular cards:", width * 0.02, heigth * 0.31, 23, white, True)
                text("The regular cards are within the normal \"base\" deck. "
                     "This deck has the most cards, all the offensive and defensive "
                     "help cards are within this deck and most cards", width * 0.02, heigth * 0.34, 15, red, False)
                text("can only be used within your own turn.", width * 0.02, heigth * 0.37, 15, red, False)
                text("But beware of some of the cards which are trick cards. "
                     "These cards need to be place upside down on the field and while they are "
                     "on the field they can be activated", width * 0.02, heigth * 0.40, 15, red, False)
                text("at any moment.", width * 0.02, heigth * 0.43, 15, red, False)
                text("Special cards:", width * 0.02, heigth * 0.48, 23, white, True)
                text("These cards are within a different deck and can be earned by "
                     "reaching the other side of the field. The effects of the cards are different, ", width * 0.02, heigth * 0.51, 15, red, False)
                text("but most cards are permanent upgrades for your boat.", width * 0.02, heigth * 0.54, 15, red, False)
                text("Offensive cards:", width * 0.02, heigth * 0.59, 23, white, True)
                text("2x FMJ Update:", width * 0.02, heigth * 0.62, 15, white, True)
                text("When this card is used. The next attack will cause a damage to the enemy of +1",
                     width * 0.15, heigth * 0.62, 15, red, False)
                text("2x Rifling:", width * 0.02, heigth * 0.65, 15, white, True)
                text("The next attack will have a range of +1", width * 0.15, heigth * 0.65, 15, red, False)
                text("2x Advanced Rifling:", width * 0.02, heigth * 0.68, 15, white, True)
                text("The next attack will have a range of +2", width * 0.15, heigth * 0.68, 15, red, False)
                text("6x Naval mine:", width * 0.02, heigth * 0.71, 15, white, True)
                text("Activate the mine with coordinates X and Y (trickcard)", width * 0.15, heigth * 0.71, 15, red, False)
                text("4x EMP upgrade:", width * 0.02, heigth * 0.74, 15, white, True)
                text("Your next attack or mine will deactivate the enemies boat for 1 turn", width * 0.15, heigth * 0.74, 15, red, False)
                text("press the left key button to go back to page 1", width * 0.08, heigth * 0.95, 23, black, True)
                text("press the right key button to go to page 3", width * 0.56, heigth * 0.95, 23, black, True)
                message_to_screen("2", width * 0.5, heigth * 0.98, 45, white, True)
                pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        instructionPage3()
                    if event.key == pygame.K_LEFT:
                        instructionPage1()

        pygame.quit()
        quit()

    def instructionPage1():
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(nextb, ((width * 0.93), (heigth * 0.92)))
        def text_objects(text, font, color, bool):
            textSuface = font.render(text, bool, color)
            return textSuface, textSuface.get_rect()

        def message_to_screen(text, x, y, size, color, bool):
            largeText = pygame.font.Font("freesansbold.ttf", size)
            textsuf, textrect = text_objects(text, largeText, color, bool)
            textrect.center = ((x), (y))
            gameDisplay.blit(textsuf, textrect)

        def text(text, x, y, size, color, bool):
            largeText = pygame.font.Font("freesansbold.ttf", size)
            textsuf, textrect = text_objects(text, largeText, color, bool)
            textrect = ((x), (y))
            gameDisplay.blit(textsuf, textrect)
        pageExit = False
        while not pageExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pageExit = True
                message_to_screen("INSTRUCTIONS", width * 0.5, heigth * 0.1, 45, white, True)
                message_to_screen("What is Shipwars?", width * 0.5, heigth * 0.2, 30, white, True)
                text("Shipwars is a mix between the Dutch game Zeeslag and Hearthstone. "
                     "The gameplay is the same as the gameplay of Zeeslag, but with Shipwars", width * 0.02, heigth * 0.25, 15, red, False)
                text("you also have two decks and cards which will help you with defeating your enemy.", width * 0.02, heigth * 0.28, 15,
                     red, False)
                text("Both players wil get three boats and a set of cards. The goal of the game is to"
                     "eliminate all the boats of your enemy. Use your tuns in a tactical way and", width * 0.02, heigth * 0.31, 15, red, False)
                text("play your card at a smart moment.", width * 0.02, heigth * 0.34, 15, red, False)
                message_to_screen("How does it work?", width * 0.5, heigth * 0.45, 30, white, True)
                text("Preparations:", width * 0.02, heigth * 0.5, 23, white, True)
                text("Every player starts with three boats and two cards. The players will at first take two cards and "
                     "then at", width * 0.02, heigth * 0.53, 15, red, False)
                text("every turn they place their boats on their own harbor.", width * 0.02, heigth * 0.56, 15, red, False)
                text("Now the preparations are finished we can start the game.", width * 0.02, heigth * 0.59, 15, red, False)
                text("Attack and Defence:", width * 0.02, heigth * 0.63, 23, white, True)
                text("While playing Shipwars, the boats can bet set into two different positions,", width * 0.02, heigth * 0.66, 15, red, False)
                text("into an attacking position and an defence position.", width * 0.02, heigth * 0.69, 15, red, False)
                text("The attacking position is the default position and if you're in this position "
                     "you can move and attack", width * 0.02, heigth * 0.72, 15, red, False)
                text("in a normal way. The defending position is much more suitable for defending,", width * 0.02, heigth * 0.75, 15, red, False)
                text("like the name says. When you're defending, you're attack range "
                     "increases with + 1,but you can only attack vertically.", width * 0.02, heigth * 0.78, 15, red, False)
                text("Gameplay:", width * 0.02, heigth * 0.82, 23, white, True)
                text("When it's the players turn. The player can pick a card from the regular deck."
                     "A card can be used before attacking", width * 0.02, heigth * 0.85, 15, red, False)
                text("The player can now move his boat. The player can attack when the "
                     "boat is in the attacking range of the other player "
                     "(two attacks within one turn).", width * 0.02, heigth * 0.88, 15, red, False)
                text("press the right key button to go to page 2", width * 0.56, heigth * 0.95, 23, black, True)
                message_to_screen("1", width * 0.5, heigth * 0.98, 45, white, True)
                pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        instructionPage2()

        pygame.quit()
        quit()

    pageExit = False
    while not pageExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pageExit = True
        instructionPage1()

    pygame.quit()
    quit()

instructionPage()
