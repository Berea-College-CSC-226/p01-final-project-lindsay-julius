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
        self.bet = 0

    def card_picker(self):
        card = random.randint(1,13)
        suit = random.randint(1,4)
        self.number_of_cards += 1
        if card == 1:
            print('you drew a {0}'.format(card))
            self.number_of_aces += 1
            self.card_values += 11
        elif 1 < card <= 10:
            print('you drew a {0}'.format(card))
            self.card_values += card
        else:
            print('you drew a {0}'.format(card))
            self.card_values += 10

        if self.card_values > 21:
            if self.number_of_aces >= 1:
                print('ace is now 1 not 11')
                self.card_values -= 10
                self.number_of_aces -= 1
            else:
                print('You Lose')
                return
        print(self.card_values)

# player = Character()
# player.card_picker()
# player.card_picker()
# player.card_picker()


