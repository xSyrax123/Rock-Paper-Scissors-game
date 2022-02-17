#!/usr/bin/env python3
# Rock, Paper, Scissors
from enum import Enum
from os import system
from random import randint
from sys import exit


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
       return self.name.title()

    
class rock_paper_scissors:
    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0

    def _spacer_size(self, length=65):
        return '-' * length

    def _player_move(self):
        while True:
            try:
                option = int(input('Choose an option between Rock (1), Paper (2), Scissors (3): '))

                if 1 <= option <= 3:
                    break
                else:
                    print('You can only enter a number between 1 and 3.')    
            except ValueError:
                print('The value entered is invalid. You can only enter numeric values.')

        return option

    def _computer_move(self):
        return randint(1,3)

    def _check_winner(self):
        if self.player_wins == self.computer_wins:
            return 'Tie.'
        elif self.player_wins > self.computer_wins:
            return 'You won the set.'
        else:
            return 'Computer wins the set.'

    def _play(self):
        times = int(input("How many times do you wish to play?: "))

        for i in range(times):
            player = self._player_move()
            computer = self._computer_move()
            print(f'You chose {Hand(player)}')
            print(f'The computer chose {Hand(computer)}')

            if player == computer:
                print('Tie.\n')
                print(self._spacer_size(), '\n')
            elif (player-computer) % 3 == 1:
                print('You won.\n')
                print(self._spacer_size(), '\n')
                self.player_wins += 1
            else:
                print('You lost.\n')
                print(self._spacer_size(), '\n')
                self.computer_wins += 1

        print(self._check_winner())
        input("Press a key to return to the main menu...")
        system("CLS")
        self.main()
            
    def main(self, length=95):
        while True:
            try:
                print('-' * length, '\n')
                print('''
                █▀█ █▀█ █▀▀ █▄▀ ░   █▀█ ▄▀█ █▀█ █▀▀ █▀█ ░   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
                █▀▄ █▄█ █▄▄ █░█ █   █▀▀ █▀█ █▀▀ ██▄ █▀▄ █   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█                                                   
                '''.center(10))
                print('-' * length, '\n')
                print('1. Play'.center(length))
                print('2. Instructions'.center(length))
                print('3. Exit'.center(length))
                choice = int(input('\nEnter an option: '))
            except ValueError:
                print('The value entered is invalid. You can only enter numeric values.')

            if choice == 1:
                system("CLS")
                self._play()
                break
            elif choice == 2:
                system("CLS")
                print("  Instructions for Rock, Paper, Scissors: ")
                print("- Rock wins over scissors (because rock smashes scissors).")
                print("- Scissors wins over paper (because scissors cut paper).")
                print("- Paper wins over rock (because paper covers rock).")
                print("- If both players show the same sign, it's a tie.\n")
                input("Press a key to return to the main menu...")
                system("CLS")
            elif choice == 3:
                exit()
            else:
                print("You have entered a number that isn't in the list.")
                system("CLS")
            

if __name__ == '__main__':
    game = rock_paper_scissors()
    game.main()