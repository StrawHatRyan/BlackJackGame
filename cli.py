from game import Player 
from dice import *

valid= True
# Ask for the player's name
name = input(" Welcome to Blackjack! What's your name? ")

# Create a Player object
player = Player(name)

# Greet the player
print(f"Hello, {player.name}! Let's play Blackjack!")

age= int(input("How old are you?"))


if age >= 18:
    while True:
        if valid==True:
            print("round:",n+1)
            di = player_hit()  
            sub_total_score += di
            print(f"{player.name}, you rolled: {di}. Your total is now {sub_total_score}.")
        else:
            print("still round:",n+1)
            print("Invalid choice. Please type 'hit' or 'stand'.")
            choice = input("Hit or stand?").strip().lower()
            if choice=="hit":
                valid=True
                di = player_hit()  
                sub_total_score += di
                print(f"{player.name}, you rolled: {di}. Your total is now {sub_total_score}.")

            elif choice =="stand":
                print("round:",n+1)
                stand_player(sub_total_score)
                print(f"You chose to stand with a total of {player_score[n]}.")
                sub_total_score=0
                while sub_total_score<18:
                    di = dealer_hit()
                    sub_total_score += di
                    print(f"dealer rolled a {di} his current score:{sub_total_score}")
                    if sub_total_score >21:
                        stand_dealer(sub_total_score)
                        print(f"The dealer has busted!! with a score of {dealer_score[n]}.")
                        print(f"{player.name}, your score is {player_score[n]} you won!")
                        play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                        
                        if play_again=="yes" or play_again=="y" or play_again=="1":
                            n=n+1
                            sub_total_score=0
                            continue
                        else:
                            break
                stand_dealer(sub_total_score)
                if dealer_score[n] >= player_score[n]:
                    print(f"Dealer wins {dealer_score[n]} to {player_score[n]}\n")
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        sub_total_score=0
                        valid=True
                        continue
                    else:
                        break
                else:
                    print(f"{player.name} wins {player_score[n]} to {dealer_score[n]}\n")
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        sub_total_score=0
                        valid=True
                        continue
                    else:
                        break
                    

            else:
                continue    

            # 🃏 Check for bust 
        if sub_total_score > 21:
            print("round:",n+1)
            stand_player(sub_total_score)
            stand_dealer(0)
            print(f" {player.name}, you busted with a total of {player_score[n]}! Dealer has score of {dealer_score[n]}")
            play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
            if play_again=="yes" or play_again=="y" or play_again=="1":
                n=n+1
                sub_total_score=0
                continue
            else:
                break


        # ask player if they want to hit or stand
        choice = input("Hit or stand? ").strip().lower()
        

        if choice == "stand":
            stand_player(sub_total_score)
            print(f"You chose to stand with a total of {player_score[n]}.")
            sub_total_score=0
            while sub_total_score<18:
                di = dealer_hit()
                sub_total_score += di
                print(f"dealer rolled a {di} his current score:{sub_total_score}")
                if sub_total_score >21:
                    stand_dealer(sub_total_score)
                    print(f"The dealer has busted!! with a score of {dealer_score[n]}.")
                    print(f"{player.name}, your score is {player_score[n]} you won!")
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()

                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        sub_total_score=0
                        continue
                    else:
                        break
            stand_dealer(sub_total_score)
            if dealer_score[n] >= player_score[n]:
                print(f"Dealer wins {dealer_score[n]} to {player_score[n]}\n")
                play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                if play_again=="yes" or play_again=="y" or play_again=="1":
                    n=n+1
                    sub_total_score=0
                    valid=True
                    continue
                else:
                    break

            else:
                print(f"{player.name} wins {player_score[n]} to {dealer_score[n]}\n")
                play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                if play_again=="yes" or play_again=="y" or play_again=="1":
                    n=n+1
                    sub_total_score=0
                    valid=True
                    continue
                else:
                    break
                           
            
        elif choice != "hit":
            valid=False

    
else:
    print("You're too young to gamble, sorry.")
