'''


'''
import pygame, random
import Character, Player, Dealer

class Game:
    def __init__(self):
        self.size = (800,600)
        self.running = True
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((1,1,1))
        self.user = Player.Player()
        self.cpu = Dealer.Dealer()
        self.turn = 'player'

    def turn_of_play(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            while self.turn == 'player':
                pass
                #self.user.card_picker()
            self.cpu.dealers_turn()
            self.showdown()

    def showdown(self):
        if self.user.card_values > self.cpu.card_values:
            print('You win!')
        else:
            print('You lose!')



def main():
    game = Game()
    game.turn_of_play()



main()