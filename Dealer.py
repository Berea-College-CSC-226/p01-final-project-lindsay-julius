import pygame
import random
import Character

class Dealer(Character.Character):
    def __init__(self):
        super().__init__()
    def dealers_turn(self):
        while self.card_values <= 16:
            self.card_picker()




# dealer = Dealer()
# dealer.dealers_turn()