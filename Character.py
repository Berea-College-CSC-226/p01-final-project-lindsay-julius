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
        self.card = random.randint(1,17) # Cards 1-13 are normal while 14, 15, 16, and 17 are special
        self.suit = random.randint(1,4)  # Suit no. 5 is for special cards only.
        self.number_of_cards += 1
        if self.card == 1:
            self.number_of_aces += 1
            self.card_values += 11
        elif 1 < self.card <= 10:
            self.card_values += self.card
        elif 10 < self.card < 14:
            self.card_values += 10
        elif self.card == 14:
            # Give more money
            self.money += 500
            self.suit = 5
        elif self.card == 15:
            # Removes your money
            self.money -= 250
            self.suit = 5
        elif self.card == 16:
            # Adds more to your bet
            self.bet += 250
            self.suit = 5
        elif self.card == 17:
            # Removes some money from your bet
            self.bet -= 250
            self.suit = 5
            if self.bet < 0:
                self.bet = 50
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


