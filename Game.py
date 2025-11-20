'''


'''
import pygame, random
import Character, Player, Dealer

def turn_of_play():
    while turn == 'player':
        user.cardpicker()
    else:
        cpu.dealers_turn()


def main():
    global turn
    turn = 'player'
    user = Player.Player()
    cpu = Dealer.Dealer()
    turn_of_play()



main()