import pygame
import random
import Character

class Dealer(Character.Character):
    def __init__(self):
        super().__init__()
    def dealers_turn(self):
        while self.card_values <= 16:
            self.card_picker()

    def card_picker(self):
        self.card = random.randint(1, 13)  # Cards 1-13 The cpu has no access to the special cards.
        self.suit = random.randint(1, 4)  # Suit no. 5 is for special cards only.
        self.number_of_cards += 1
        if self.card == 1:
            self.number_of_aces += 1
            self.card_values += 11
        elif 1 < self.card <= 10:
            self.card_values += self.card
        elif 10 < self.card < 14:
            self.card_values += 10
        if self.card_values > 21:
            if self.number_of_aces >= 1:
                self.card_values -= 10
                self.number_of_aces -= 1
            else:
                return



# dealer = Dealer()
# dealer.dealers_turn()