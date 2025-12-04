'''

'''
import pygame
import random

class Character:
    def __init__(self):
        self.money = 500
        self.card_values = 0
        self.number_of_cards = 0
        self.number_of_aces = 0
        self.bet = 50
        self.card = 0

    def card_picker(self):
        self.card = random.randint(1,13)
        suit = random.randint(1,4)
        self.number_of_cards += 1
        if self.card == 1:
            print('you drew a {0}'.format(self.card))
            self.number_of_aces += 1
            self.card_values += 11
        elif 1 < self.card <= 10:
            print('you drew a {0}'.format(self.card))
            self.card_values += self.card
        else:
            print('you drew a {0}'.format(self.card))
            self.card_values += 10

        if self.card_values > 21:
            if self.number_of_aces >= 1:
                print('ace is now 1 not 11')
                self.card_values -= 10
                self.number_of_aces -= 1
            else:
                return
        print(self.card_values)

if __name__ == '__main__':
    player = Character()
    player.card_picker()
    player.card_picker()
    player.card_picker()


