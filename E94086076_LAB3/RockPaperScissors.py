import random


class RockPaperScissors(object):
    def __init__(self):
        self.tie_counter = 0
        self.win_counter = 0
        self.loss_counter = 0
        self.initial = True

    def play(self):
        if self.initial:
            print("Welcome to ROCK, PAPER, SCISSORS game!")
        self.initial = False
        win = self.win_counter + 1
        while self.win_counter != win:
            user_input = input("Enter your move: (r)ock (p)aper, (s)cissors ")
            computer_input = random.choice(['ROCK', 'PAPER', 'SCISSORS'])

            # convert user input char to words
            if user_input == 'r':
                user_input_converted = "ROCK"
            elif user_input == 'p':
                user_input_converted = "PAPER"
            else:
                user_input_converted = "SCISSORS"

            # print the versus sentences
            print(f"{user_input_converted}  versus...\n{computer_input}")

            # compare
            if user_input_converted == computer_input:
                print("It is a tie!")
                self.tie_counter = self.tie_counter + 1
            elif user_input_converted == 'ROCK' and computer_input == 'PAPER':
                print("You lose!")
                self.loss_counter = self.loss_counter + 1
            elif user_input_converted == 'ROCK' and computer_input == 'SCISSORS':
                print("You win!")
                self.win_counter = self.win_counter + 1
            elif user_input_converted == 'PAPER' and computer_input == 'ROCK':
                print("You win!")
                self.win_counter = self.win_counter + 1
            elif user_input_converted == 'PAPER' and computer_input == 'SCISSORS':
                print("You lose!")
                self.loss_counter = self.loss_counter + 1
            elif user_input_converted == 'SCISSORS' and computer_input == 'PAPER':
                print("You win!")
                self.win_counter = self.win_counter + 1
            else:
                print("You lose!")
                self.loss_counter = self.loss_counter + 1

        # print out the final answer
        print(
            f"You have {self.tie_counter} ties, {self.loss_counter} losses and {self.win_counter} wins.")


game = RockPaperScissors()
game.play()
game.play()
