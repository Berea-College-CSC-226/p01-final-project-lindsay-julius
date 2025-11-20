'''


'''
import pygame, random
import Character, Player, Dealer

def turn_of_play(user, cpu):
    while turn == 'player':
        user.cardpicker()
    cpu.dealers_turn()
    showdown(user, cpu)

def showdown(user, cpu):
    if user.card_values > cpu.card_values:
        print('You win!')
    else:
        print('You lose!')

def main():
    global turn
    turn = 'player'
    user = Player.Player()
    cpu = Dealer.Dealer()
    turn_of_play(user, cpu)
    #the game is mad at the user because it thinks it doesn't have the method card picker (it's from its parent function)



main()