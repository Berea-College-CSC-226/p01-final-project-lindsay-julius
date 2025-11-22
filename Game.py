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
        self.turn = 'dealer'

    def turn_of_play(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # The code above allows the game to quit

            if  self.turn == 'player':
                print('players turn')
                # Above are the functions and methods that the player can call

            elif self.turn == 'dealer':
                self.cpu.dealers_turn()
                self.showdown()
                #These are the actions that the dealer will take

            else:
                print('game end')
                #Logic at the end of the game that will allow the player to replay the game.

            pygame.display.update()
            self.clock.tick(24)
            # Handles the screen not crashing



    def showdown(self):
        if self.user.card_values > self.cpu.card_values:
            print('You win!')
        else:
            print('You lose!')



def main():
    game = Game()
    game.turn_of_play()



main()