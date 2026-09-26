"""
Match Coins game
Sarah Estes
To stimulate a coin matching game
Standard Python Library used, Random
9/25/26
"""

from player import Player

def main():
    player1 = Player("Player1")
    player2 = Player("Player2")

    play_condition = True

    print("--- Coin Match Game ---")

    while play_condition:
        want_to_play = input("\nDo you want to toss the coins? (y/n): ")
        
        if want_to_play == "n":
            play_condition = False
            print("\nCome back if you change your mind.")

        print("\nTossing...")

        player1 = Player("Player 1")
        player1.toss_coin()
        player1_coin = player1.get_coin_side()
        print(f"Player 1 tossed {player1_coin}.")

        player2 = Player("Player 2")
        player2.toss_coin()
        player2_coin = player2.get_coin_side()
        print(f"Player 2 tossed {player2_coin}.")

        if player1_coin == player2_coin:
            print("...It's a match! Player 1 wins a coin.")
            player1.win_coin()


        if player1_coin != player2_coin:
            print("...No Match! Player 2 wins a coin.")
            player2.win_coin()  