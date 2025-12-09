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
        self.display_card_heart = pygame.image.load('Game_Images/Heart Cards.png').convert_alpha()
        self.suit = 1

    def card_picker(self):
        self.card = random.randint(1,13)
        self.suit = random.randint(1,4)
        self.number_of_cards += 1
        if self.card == 1:
            self.number_of_aces += 1
            self.card_values += 11
        elif 1 < self.card <= 10:
            self.card_values += self.card
        else:
            self.card_values += 10

        if self.card_values > 21:
            if self.number_of_aces >= 1:
                self.card_values -= 10
                self.number_of_aces -= 1
            else:
                return

if __name__ == '__main__':
    player = Character()
    player.card_picker()
    player.card_picker()
    player.card_picker()


