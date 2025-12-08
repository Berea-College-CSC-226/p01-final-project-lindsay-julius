'''


'''
import pygame, random, time
import Character, Player, Dealer

class  Game:
    def __init__(self):
        self.size = (900,700)
        self.running = True
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#00850b')
        self.clock = pygame.time.Clock()
        self.user = Player.Player()
        self.cpu = Dealer.Dealer()
        self.turn = ['betting']
        self.list_of_cards = []

        self.stand_button = pygame.image.load('Game_Images/stand_button.png').convert_alpha()
        self.stand_button = Button(25, 200, self.stand_button, self.screen, self.turn, 'Stand',self.user)

        self.raise_bet = pygame.image.load('Game_Images/Plus Button.png').convert_alpha()
        self.raise_bet = Button(150, 75, self.raise_bet, self.screen, self.turn, 'Raise',self.user)

        self.lower_bet = pygame.image.load('Game_Images/Minus Button.png').convert_alpha()
        self.lower_bet = Button(0, 75, self.lower_bet, self.screen, self.turn, 'Lower',self.user)

        self.font = pygame.font.SysFont("CourierNew", 50, True)
        self.money_txt = self.font.render("Money:" + str(self.user.money), True, "black")
        self.bet_txt = self.font.render("Bet:" + str(self.user.bet), True, "black")
        self.altfont = pygame.font.SysFont("TimesNewRoman", 25, True)
        self.help_txt = self.altfont.render("Select the amount to bet, then press Space!", True, "darkblue")
        self.end_txt = self.altfont.render("You Lose!", True, "black")


    def turn_of_play(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # The code above allows the game to quit

            if  self.turn[:] == ['player']:
                # if event.type == pygame.KEYDOWN:
                self.help_txt = self.altfont.render("Press Space to HIT!", True, "darkblue")

                keypress = pygame.key.get_pressed()
                if keypress[pygame.K_SPACE]:
                    print('players turn to draw a card')
                    self.user.card_picker()
                    time.sleep(0.25)
                    self.card_display_player(self.user.suit, self.user.card, self.user.number_of_cards)
                # Above are the functions and methods that the player can call
                if self.user.card_values > 21:
                    self.showdown()
                    # Triggers the end of the game

                if keypress[pygame.K_s] or keypress[pygame.K_RETURN]: # s stands fors stand so when the s key is hit it activates
                    self.turn[:] = ['dealer']

            elif self.turn == ['dealer']:
                print("Dealer's turn..")
                self.help_txt = self.altfont.render("", True, "darkblue")
                while self.cpu.card_values <= 16:
                    self.cpu.card_picker()
                    self.card_display_dealer(self.cpu.suit, self.cpu.card, self.cpu.number_of_cards)
                    time.sleep(0.25)
                    pygame.display.update()
                    self.clock.tick(12)
                    #Updates the display since it will be stuck in a while loop
                self.showdown()
                self.turn[:] = ['game_over']


            elif self.turn == ['game_over']:
                if self.user.money > 0:
                    self.help_txt = self.altfont.render("Press Space to Play Again!", True, "darkblue")
                    keypress = pygame.key.get_pressed()
                    if keypress[pygame.K_SPACE]:
                        self.user.bet = 50
                        self.user.card_values = 0
                        self.user.number_of_aces = 0
                        self.user.number_of_cards = 0
                        self.cpu.card_values = 0
                        self.cpu.number_of_aces = 0
                        self.cpu.number_of_cards = 0
                        pygame.draw.rect(self.screen, '#00850b', ((0, 0), (900, 700)), 0)
                        self.help_txt = self.altfont.render("Select the amount to bet, then press Space!", True,"darkblue")
                        self.turn[:] = ['betting']
                        # Resets every attribute except the money the player has. Also clears the screen.
                else:
                    self.help_txt = self.altfont.render("Uh oh You've Ran out of Money!!!", True,"darkblue")

            elif self.turn == ['betting']:
                keypress = pygame.key.get_pressed()
                if keypress[pygame.K_SPACE]:
                    self.cpu.card_picker()
                    self.card_display_dealer(self.cpu.suit, self.cpu.card, self.cpu.number_of_cards)
                    self.turn[:] = ['player']
                    # Changes the turn-off of the betting turn once the space bar is pressed

            # The functions below add the objects to the screen
            self.stand_button.draw()
            self.lower_bet.draw()
            self.raise_bet.draw()

            self.money_txt = self.font.render("Money:" + str(self.user.money), True, "black")
            self.bet_txt = self.font.render("Current Bet:" + str(self.user.bet), True, "black")

            # Below clears the screen of the text variables, then readds the text onto the screen.
            pygame.draw.rect(self.screen, '#00850b',((500,500),(600,600)),0)
            pygame.draw.rect(self.screen, '#00850b', ((0, 0), (500, 50)), 0)
            pygame.draw.rect(self.screen, '#00850b', ((0, 625), (500, 625)), 0)
            self.screen.blit(self.money_txt, (600, 625))
            self.screen.blit(self.bet_txt, (0, 0))
            self.screen.blit(self.help_txt, (0, 625))

            #This updates the screen with all the new information
            pygame.display.update()
            self.clock.tick(12)

    def card_display_player(self, suit, card, num_of_cards):
        if card == 1:
            self.ss = Spritesheet('Game_Images/Club Cards.png',self.screen,self.user.number_of_cards)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        elif card == 2:
            self.ss = Spritesheet('Game_Images/Diamond Cards.png', self.screen,self.user.number_of_cards)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        elif card == 3:
            self.ss = Spritesheet('Game_Images/Heart Cards.png', self.screen,self.user.number_of_cards)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        else:
            self.ss = Spritesheet('Game_Images/Spade Cards.png', self.screen,self.user.number_of_cards)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        # Sets the image using a spritesheet before creating a pygame rectange with the dimensions of a card.
    def card_display_dealer(self, suit, card, num_of_cards):
        if card == 1:
            self.ss = Spritesheet_Dealer('Game_Images/Club Cards.png',self.screen,self.cpu.number_of_cards)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        elif card == 2:
            self.ss = Spritesheet_Dealer('Game_Images/Diamond Cards.png', self.screen,self.cpu.number_of_cards)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        elif card == 3:
            self.ss = Spritesheet_Dealer('Game_Images/Heart Cards.png', self.screen,self.cpu.number_of_cards)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        else:
            self.ss = Spritesheet_Dealer('Game_Images/Spade Cards.png', self.screen,self.cpu.number_of_cards)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        # The dealer uses a different function because it needs to position the cards differently.

    def showdown(self):
        # Handles all the value changes and end text before switching it to the end turns.
        if self.user.card_values > 21:
            self.end_txt = self.altfont.render(f'You lost! total hand is {self.user.card_values}.', True, "black")
            self.screen.blit(self.end_txt, (550, 300))
            self.user.money -= self.user.bet
            self.turn[:] = ['game_over']
            self.turn_of_play()
        elif self.user.card_values > self.cpu.card_values or self.cpu.card_values > 21:
            self.end_txt = self.altfont.render("You Win!", True, "black")
            self.screen.blit(self.end_txt, (550, 300))
            self.user.money += self.user.bet
            self.turn[:] = ['game_over']
            self.turn_of_play()
        else:
            self.end_txt = self.altfont.render("You Lose!", True, "black")
            self.screen.blit(self.end_txt, (550, 300))
            self.user.money -= self.user.bet
            self.turn[:] = ['game_over']
            self.turn_of_play()

class Button:
    def __init__(self, x, y, image, screen, turn, name, player):
        self.screen = screen
        width = image.get_width()
        height = image.get_height()
        self.image = image # or pygame.transform.scale(image,(int(width * 2), int(height * 2))) for scale
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.turn = turn
        self.name = name
        self.player = player

    def draw(self):

        pos = pygame.mouse.get_pos()
        # print(pos)

        if self.rect.collidepoint(pos):   # this is the click function
            if pygame.mouse.get_pressed()[0] == 1:
                if self.name == 'Stand':    # checking which button you're clicking
                    if self.turn == ['player']:
                        print('standing')
                        self.turn[:] = ['dealer']
                if self.name == 'Raise':     # Adds 50 to their bet
                    if self.turn == ['betting']:
                        self.player.bet += 50
                        if self.player.bet > self.player.money:
                            self.player.bet = self.player.money
                        print(self.player.bet)
                if self.name == 'Lower':     # Removes 50 to their bet
                    if self.turn == ['betting']:
                        self.player.bet -= 50
                        if self.player.bet < 50:
                            self.player.bet = 50
                        print(self.player.bet)
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

class Spritesheet:
    def __init__(self, filename,screen, number_of_cards):
        self.screen = screen
        self.number_of_cards = number_of_cards
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error:
            print(f'Could not load image {filename}')
    def image_at(self, rectangle,num_of_cards):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        self.screen.blit(self.sheet, (300 + (50 * self.number_of_cards),350), rect)
        return image

class Spritesheet_Dealer(Spritesheet):
    # The dealer needs a separate spritesheet so it can position the cards differently.
    def __init__(self, filename, screen, number_of_cards):
        super().__init__(filename,screen, number_of_cards)
    def image_at(self, rectangle,num_of_cards):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        self.screen.blit(self.sheet, (300 + (50 * self.number_of_cards), 150), rect)
        return image

def main():
    pygame.font.init()
    game = Game()
    game.turn_of_play()



main()