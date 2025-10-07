from game import Player 
from dice import *


# Ask for the player's name
name = input("Welcome to Blackjack! What's your name? ")

# Create a Player object
player = Player(name)

# Greet the player
print(f"Hello, {player.name}! Let's play Blackjack!")

age= int(input("How old are you?"))
if age>18:
    while age>18:
        di = player_hit()
        sub_total_score = sub_total_score+di
        print(f"{player.name} you rolled:",di," hit or stand? \n")
        # Will be addimg some if clauses tommorrow.
        

        
else:
    print("You're too young to gamble, sorry.")