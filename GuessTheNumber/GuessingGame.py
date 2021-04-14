from GameLogic import GameLogic

"""Simple game where the user has to guess a generated number, while getting clues in form of equations for given number.

Takes max_tries (integer) as an argument. No argument when instantiating the object sets a default max_tries = 5.

After instantiation, use the start method to start the game.

input other than an integer will crash the game.
"""
class GuessingGame:

    def __init__(self, max_tries=5):
        self.logic = GameLogic(max_tries)

    def start(self):
        print(f"Welcome to NumGuesser!\n You have {self.logic.max_tries} tries to guess the right number between 1-1000.\n Do you want a starting clue?\nYes(Y), No(N)> ")
        choice = input()

        if(choice.lower() == "y"):
            print(self.logic.clue())
        elif(choice.lower() == "n"):
            print("No clue it is. Lets roll!")
        else:
            print("That's not a command, no clue for you. Lets roll!")

        running = True

        while running:
            print("Make your guess> ")
            guess = input()
            if(self.logic.make_guess(guess)):
                running = False
                print("Correct answer!")
            else:
                tries_left = self.logic.tries_left()
                if(tries_left == 0):
                    print(f"You're out of tries, game over! Correct Answer was {self.logic.answer}")
                    running = False
                else:
                    print(f"That's not quite it, You have {tries_left} tries left. here's a new clue!")
                    print(self.logic.clue())