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

    def turn_of_play(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # The code above allows the game to quit

            if  self.turn == 'player':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('players turn to draw a card')
                    #add draw function here
                # Above are the functions and methods that the player can call
                    if self.user.card_values > 21:
                        print(f'You lost! Total is {self.user.card_values}.')
                        self.turn = 'game over'



            elif event.key == pygame.K_s: # s stands fors stand
                self.turn = 'dealer'


        if self.turn == 'plater':
            pass


        elif self.turn == 'dealer':
            print("Dealer's turn..")
            self.cpu.dealers_turn()
            self.showdown()
            self.turn = 'game_over'

        elif self.turn == 'game_over':
            pass

        else:
            print('game end')
            # elif self.turn == 'dealer':
            #     self.cpu.dealers_turn()
            #     self.showdown()
            #     #These are the actions that the dealer will take
            #
            # else:
            #     print('game end')
            #     #Logic at the end of the game that will allow the player to replay the game.
            #
            pygame.display.update()
            self.clock.tick(24)
            # Handles the screen not crashing



    def showdown(self):
        if self.user.card_values > 21:
            print('You Lose!')
        elif self.user.card_values > self.cpu.card_values:
            print('You Win!')
        else:
            print('You lose!')



def main():
    game = Game()
    game.turn_of_play()



main()