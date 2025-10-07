from game import Player 
from dice import *


# Ask for the player's name
name = input(" Welcome to Blackjack! What's your name? ")

# Create a Player object
player = Player(name)

# Greet the player
print(f"Hello, {player.name}! Let's play Blackjack!")

age= int(input(" How old are you?"))

if age >= 18:
    sub_total_score = 0  # the starting score

    while True:
        di = player_hit()  
        sub_total_score += di
        print(f"{player.name}, you rolled: {di}. Your total is now {sub_total_score}.")

        # 🃏 Check for bust
        if sub_total_score > 21:
            print(f" {player.name}, you busted with a total of {sub_total_score}!")
            break  

        # ask player if they want to hit or stand
        choice = input("Hit or stand? ").strip().lower()

        if choice == "stand":
            print(f"You chose to stand with a total of {sub_total_score}.")
            break
        elif choice != "hit":
            print("Invalid choice. Please type 'hit' or 'stand'.")

else:
    print("You're too young to gamble, sorry.")
