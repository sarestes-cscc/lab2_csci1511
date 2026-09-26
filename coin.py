"""
Match Coins game
Sarah Estes
To stimulate a coin matching game
Standard Python Library used, Random Module
9/25/26
"""

from random import randint

class Coin:
    """
    Represents a single, tossable coin.
    It only knows about its own state (heads or tails).
    """

    def __init__(self):
        """Initialize attributes for the coin"""
        self.__sideup = "Heads" or "Tails"

    def toss(self):
        random_number = randint(1, 2)
        if random_number == 1:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
        return self.__sideup
        
    def get_sideup(self):
        __sideup = self.__sideup
        return __sideup
