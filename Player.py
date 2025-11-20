'''

'''

import pygame, random, Character


class Player(Character.Character):
    def __init__(self):
        super().__init__()

    # def Stand(self):
    #     player_turn = 'dealer'
    # Unused code for now, if it needs to be reimplemented it can
    def Double(self):
        if self.card_values >= 11:
            self.card_picker()
            self.bet *= 2