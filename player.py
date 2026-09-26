"""
Match Coins game
Sarah Estes
To stimulate a coin matching game
Standard Python Library used, Random
9/25/26
"""

from coin import Coin

class Player:
    """
    Represents a player who has a name, wallet of coins, 
    and Coin object to toss
    """

    def __init__(self, __name):
        """
        Initialize attributes for Player
        """
        self.__name = __name
        self.__coin = Coin()
        self.__wallet = 20