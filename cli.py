from game import Player 

# Ask for the player's name
name = input("Welcome to Blackjack! What's your name? ")

# Create a Player object
player = Player(name)

# Greet the player
print(f"Hello, {player.name}! Let's play Blackjack!")
