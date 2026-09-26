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
        """ Initialize attributes for Player """
        self.__name = __name
        self.__coin = Coin()
        self.__wallet = 20

    def toss_coin(self):
        """ Tells the Player's coin to toss itself """
        self.__coin.toss()
        return self.__coin

    def get_coin_side(self):
        """ Gets the side of the player's coin """
        self.__coin.get_sideup()
        return self.__coin

    def win_coin(self):
        """ Adds 1 to wallet """
        self.__wallet += 1
        return self.__wallet

    def lose_coin(self):
        """ Subtracts 1 from wallet """
        self.__wallet -= 1
        return self.__wallet

    def get_wallet(self):
        """ Returns current value of wallet """
        __wallet = self.__wallet
        return __wallet

    def get_name(self):
        """ Returns current value of name """
        __name = self.__name
        return __name

    