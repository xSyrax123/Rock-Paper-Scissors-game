import colorama
from random import randint
from sys import exit
from Hand import *

    
class RockPaperScissors:
    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0
        self.draws = 0

    def _spacer_size(self, length=65):
        return "-" * length

    def _clear_screen(self):
        print(colorama.ansi.clear_screen(), end='')

    def _player_move(self):
        while True:
            try:
                option = int(input("Choose an option between Rock (1), Paper (2), Scissors (3): "))

                if 1 <= option <= 3:
                    break
                else:
                    print("You can only enter a number between 1 and 3.\n")
                    print(f'{self._spacer_size()}\n')    
            except ValueError:
                print("The value entered is invalid. You can only enter numeric values.")
        return option

    def _computer_move(self):
        return randint(1,3)

    def _check_winner(self):
        if self.player_wins == self.computer_wins:
            return "It's a tie."
        elif self.player_wins > self.computer_wins:
            return "You won the set."
        else:
            return "Computer wins the set."

    def _play(self):
        times = int(input("How many times do you wish to play?: "))

        for i in range(times):
            player = self._player_move()
            computer = self._computer_move()
            print(f"You chose {Hand(player)}. | The computer chose {Hand(computer)}.")

            if player == computer:
                print("It's a draw.\n")
                self.draws += 1
            elif (player-computer) % 3 == 1:
                print("You won.\n")
                self.player_wins += 1
            else:
                print("You lost.\n")
                self.computer_wins += 1

            print(f"Player wins: {self.player_wins} || Computer wins: {self.computer_wins} || Draws: {self.draws}\n")
            print(f'{self._spacer_size()}\n')
            
        self.player_wins = 0
        self.computer_wins = 0
        self.draws = 0
        print(self._check_winner())
        input("Press a key to return to the main menu...")
        self.main()
            
    def main(self, length=95):
        while True:
            try:
                print(f"{'-' * length}\n")
                print("""
                █▀█ █▀█ █▀▀ █▄▀ ░   █▀█ ▄▀█ █▀█ █▀▀ █▀█ ░   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
                █▀▄ █▄█ █▄▄ █░█ █   █▀▀ █▀█ █▀▀ ██▄ █▀▄ █   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█                                                   
                """.center(10))
                print(f"{'-' * length}\n")
                print("1. Play".center(length))
                print("2. Instructions".center(length))
                print("3. Exit".center(length))
                choice = int(input("\nEnter an option: "))
            except ValueError:
                print("The value entered is invalid. You can only enter numeric values.")

            self._clear_screen()

            if choice == 1:
                self._play()
                break
            elif choice == 2:
                input(f"""
                      Instructions for Rock, Paper, Scissors:
                    - Rock wins over scissors (because rock smashes scissors).
                    - Scissors wins over paper (because scissors cut paper).
                    - Paper wins over rock (because paper covers rock).
                    - If both players show the same sign, it's a tie.\n
                    Press a key to return to the main menu...                        
                    """.center(length))
            elif choice == 3:
                exit()
            else:
                print("You have entered a number that isn't in the list.")

            self._clear_screen()
            

if __name__ == '__main__':
    game = RockPaperScissors()
    game.main()
