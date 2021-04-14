import random

"""Calculates the logics of the game.

Contains the methods make_guess to check if guess is correct, clue which generates an equation of division or multiplication for the answer.

input other than an integer will crash the game.
"""
class GameLogic:

    def __init__(self, max_tries):
        self.max_tries = max_tries
        self.answer = random.randint(1,1000)
        self.curr_tries = 0

    def make_guess(self, guess):
        if(not self.__is_lost()):
            if(int(guess) == self.answer):
                return True
            else:
                self.curr_tries += 1
                return False
        else:
            return False

    def __is_lost(self):
        return False if self.curr_tries != self.max_tries else True

    def tries_left(self):
        return self.max_tries - self.curr_tries

    def __gen_unique_base(self):
        run = True
        while run:
            base_int = random.randint(1,1000)
            run = (base_int == self.answer)
        return base_int

    def clue(self):
        clue_type = random.randint(1,2)
        if(clue_type == 1):
            base_int = self.__gen_unique_base()
            top_int = self.answer / base_int
            return f"Answer = {base_int} * {top_int}"
        else:
            base_int = self.__gen_unique_base()
            top_int = self.answer * base_int
            return f"Answer = {top_int} / {base_int}"