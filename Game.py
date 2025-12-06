'''


'''
import pygame, random
import Character, Player, Dealer

class Game:
    def __init__(self):
        self.size = (800,600)
        self.running = True
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#00850b')
        self.clock = pygame.time.Clock()
        self.user = Player.Player()
        self.cpu = Dealer.Dealer()
        self.turn = ['player']
        self.list_of_cards = []

        self.stand_button = pygame.image.load('Game_Images/stand_button.png').convert_alpha()
        self.stand_button = Button(100, 200, self.stand_button, self.screen, self.turn, 'Stand',self.user)

        self.raise_bet = pygame.image.load('Game_Images/Plus Button.png').convert_alpha()
        self.raise_bet = Button(100, 400, self.raise_bet, self.screen, self.turn, 'Raise',self.user)

        self.lower_bet = pygame.image.load('Game_Images/Minus Button.png').convert_alpha()
        self.lower_bet = Button(100, 300, self.lower_bet, self.screen, self.turn, 'Lower',self.user)

        # self.ss = Spritesheet('Game_Images/Heart Cards.png',self.screen)
        # image = self.ss.image_at((0,0,0,0))


    def turn_of_play(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # The code above allows the game to quit

            if  self.turn[:] == ['player']:
                # if event.type == pygame.KEYDOWN:
                    keypress = pygame.key.get_pressed()
                    if keypress[pygame.K_SPACE]:
                        print('players turn to draw a card')
                        self.user.card_picker()
                        self.card_display(self.user.suit, self.user.card, self.user.number_of_cards)
                    # Above are the functions and methods that the player can call
                    if self.user.card_values > 21:
                        print(f'You lost! Total is {self.user.card_values}.')
                        self.user.money -= self.user.bet
                        self.turn[:] = ['game_over']
                        self.turn_of_play()

                    if keypress[pygame.K_s]: # s stands fors stand so when the s key is hit it activates
                        self.turn[:] = ['dealer']


            elif self.turn == ['dealer']:
                print("Dealer's turn..")
                self.cpu.dealers_turn()
                self.showdown()
                self.turn[:] = ['game_over']


            elif self.turn == ['game_over']:
                keypress = pygame.key.get_pressed()
                print('Play again?') # TODO make this only print once not every frame.
                if keypress[pygame.K_SPACE]:
                    self.user.bet = 50
                    self.user.card_values = 0
                    self.user.number_of_aces = 0
                    self.user.number_of_cards = 0
                    self.cpu.card_values = 0
                    self.cpu.number_of_aces = 0
                    self.cpu.number_of_cards = 0
                    self.turn[:] = ['player']

            # The functions below add the objects to the screen
            self.stand_button.draw()
            self.lower_bet.draw()
            self.raise_bet.draw()
            # These update the display every 12 frames
            # for i in self.list_of_cards:
            #     length = length(self.list_of_cards)
            #     self.screen.blit(self.list_of_cards[i], self.list_of_cards.index(i))
            # TODO This function above may lead to indexing the number of cards in the list (gives us access to remove the images later).

            pygame.display.update()
            self.clock.tick(12)

    def card_display(self, suit, card, num_of_cards):
        if card == 1:
            self.ss = Spritesheet('Game_Images/Club Cards.png',self.screen)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        elif card == 2:
            self.ss = Spritesheet('Game_Images/Diamond Cards.png', self.screen)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        elif card == 3:
            self.ss = Spritesheet('Game_Images/Heart Cards.png', self.screen)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)
        else:
            self.ss = Spritesheet('Game_Images/Spade Cards.png', self.screen)
            ss = self.ss.image_at((0 + (90 * (card - 1)), 0,90, 130), num_of_cards)
            self.list_of_cards.append(ss)

    def showdown(self):
        if self.user.card_values > 21:
            print('You Lose!')
            self.user.money -= self.user.bet
            self.turn[:] = ['game_over']
            self.turn_of_play()
        elif self.user.card_values > self.cpu.card_values or self.cpu.card_values > 21:
            print('You Win!')
            self.user.money += self.user.bet
            self.turn[:] = ['game_over']
            self.turn_of_play()
        else:
            print('You lose!')
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
                    print('standing')
                    self.turn[:] = ['dealer']
                if self.name == 'Raise':     # Adds 50 to their bet
                    self.player.bet += 50
                    if self.player.bet > self.player.money:
                        self.player.bet = self.player.money
                    print(self.player.bet)
                if self.name == 'Lower':     # Removes 50 to their bet
                    self.player.bet -= 50
                    if self.player.bet < 50:
                        self.player.bet = 50
                    print(self.player.bet)
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

class Spritesheet:
    def __init__(self, filename,screen):
        self.screen = screen
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error:
            print(f'Could not load image {filename}')
    def image_at(self, rectangle,num_of_cards):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        self.screen.blit(self.sheet, (250,300), rect)
        return image



def main():
    game = Game()
    game.turn_of_play()



main()