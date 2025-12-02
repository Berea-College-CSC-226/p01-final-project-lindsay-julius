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
        self.turn = 'player'
        self.stand_button = pygame.image.load('Game_Images/stand_button.png').convert_alpha()

        self.stand_button = Button(100, 200, self.stand_button, self.screen)


    def turn_of_play(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # The code above allows the game to quit

            if  self.turn == 'player':
                # if event.type == pygame.KEYDOWN:
                    keypress = pygame.key.get_pressed()
                    if keypress[pygame.K_SPACE]:
                        print('players turn to draw a card')
                        self.user.card_picker()
                    # Above are the functions and methods that the player can call
                    if self.user.card_values > 21:
                        print(f'You lost! Total is {self.user.card_values}.')
                        self.turn = 'game over'

                    if keypress[pygame.K_s]: # s stands fors stand so when the s key is hit it activates
                        self.turn = 'dealer'


            elif self.turn == 'dealer':
                print("Dealer's turn..")
                self.cpu.dealers_turn()
                self.showdown()
                self.turn = 'game_over'


            elif self.turn == 'game_over':
                pass
            self.stand_button.draw()
            pygame.display.update()
            self.clock.tick(12)


        # else:
        #
        #     print('game end')
            # elif self.turn == 'dealer':
            #     self.cpu.dealers_turn()
            #     self.showdown()
            #     #These are the actions that the dealer will take
            #
            # else:
            #     print('game end')
            #     #Logic at the end of the game that will allow the player to replay the game.
            #



            # Handles the screen not crashing



    def showdown(self):
        if self.user.card_values > 21:
            print('You Lose!')
        elif self.user.card_values > self.cpu.card_values or self.cpu.card_values > 21:
            print('You Win!')
        else:
            print('You lose!')

class Button():
    def __init__(self, x, y, image, screen):
        self.screen = screen
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width * 2), int(height * 2)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):

        pos = pygame.mouse.get_pos()
        print(pos)

        self.screen.blit(self.image, (self.rect.x, self.rect.y))




def main():
    game = Game()
    game.turn_of_play()



main()