from game import Player 
from dice import *

valid= True
bet_time=True
money=1000
bet_amount=0

# Ask for the player's name
name = input(" Welcome to Blackjack! What's your name? ")

# Create a Player object
player = Player(name)

# Greet the player
try_again=1
print(f"Hello, {player.name}! Let's play Blackjack!")
while try_again==True:
    try:
        age= int(input("How old are you?"))
        try_again=False
    except:
        print("Your age has to be a number")
        tried_again= True
        continue


    if age >= 18:
        while True:
            if valid==True:
                print("round:",n+1)
                di = player_hit()  
                sub_total_score += di
                print(f"{player.name}, you rolled: {di}. Your total is now {sub_total_score}.")
                if bet_time==True:
                    print("print time")
                    bet_time=False
            else:
                print("still round:",n+1,"still roll",sub_total_score)
                print("Invalid choice. Please type 'hit' or 'stand'.")
                choice = input("Hit or stand?").strip().lower()
                if choice=="hit":
                    valid=True
                    di = player_hit()  
                    sub_total_score += di
                    print(f"{player.name}, you rolled: {di}. Your total is now {sub_total_score}.")
                elif choice == "stand" and sub_total_score == 21:
                    stand_player(sub_total_score)
                    sub_total_score=0
                    stand_dealer(sub_total_score)
                    all_wins=all_wins+1
                    print(f"{player.name} wins {player_score[n]} to {dealer_score[n]} by Black Jack\n")
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        valid=True
                        continue
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        break
                
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
                        all_wins=all_wins+1
                        stand_dealer(sub_total_score)
                        print(f"The dealer has busted!! with a score of {dealer_score[n]}.")
                        print(f"{player.name}, your score is {player_score[n]} you won!")
                        play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                        
                        if play_again=="yes" or play_again=="y" or play_again=="1":
                            n=n+1
                            sub_total_score=0
                            valid=True
                            continue
                        else:
                            print(f"{player.name} you've played {n+1} rounds")
                            print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                            break
                    stand_dealer(sub_total_score)
                    if dealer_score[n] >= player_score[n]:
                        all_loses=all_loses+1
                        print(f"Dealer wins {dealer_score[n]} to {player_score[n]}\n")
                        play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                        if play_again=="yes" or play_again=="y" or play_again=="1":
                            n=n+1
                            sub_total_score=0
                            valid=True
                            continue
                        else:
                            print(f"{player.name} you've played {n+1} rounds")
                            print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                            break
                    else:
                        all_wins=all_wins+1
                        print(f"{player.name} wins {player_score[n]} to {dealer_score[n]}\n")
                        play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                        if play_again=="yes" or play_again=="y" or play_again=="1":
                            n=n+1
                            sub_total_score=0
                            valid=True
                            continue
                        else:
                            print(f"{player.name} you've played {n+1} rounds")
                            print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                            break
                        

                else:
                    continue    

                # 🃏 Check for bust 
            if sub_total_score > 21:
                print("round:",n+1)
                all_loses=all_loses+1
                stand_player(sub_total_score)
                stand_dealer(0)
                print(f" {player.name}, you busted with a total of {player_score[n]}! Dealer has score of {dealer_score[n]}")
                play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                if play_again=="yes" or play_again=="y" or play_again=="1":
                    n=n+1
                    sub_total_score=0
                    continue
                else:
                    print(f"{player.name} you've played {n+1} rounds")
                    print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                    break


            # ask player if they want to hit or stand
            choice = input("Hit or stand? ").strip().lower()
            
            if choice == "stand" and sub_total_score == 21:
                    stand_player(sub_total_score)
                    sub_total_score=0
                    stand_dealer(sub_total_score)
                    all_wins=all_wins+1
                    print(f"{player.name} wins {player_score[n]} to {dealer_score[n]} by Black Jack\n")
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        valid=True
                        continue
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        break
            elif choice == "stand":
                stand_player(sub_total_score)
                print(f"You chose to stand with a total of {player_score[n]}.")
                sub_total_score=0
                while sub_total_score<18:
                    di = dealer_hit()
                    sub_total_score += di
                    print(f"dealer rolled a {di} his current score:{sub_total_score}")
                if sub_total_score >21:
                    all_wins=all_wins+1
                    stand_dealer(sub_total_score)
                    print(f"The dealer has busted!! with a score of {dealer_score[n]}.")
                    print(f"{player.name}, your score is {player_score[n]} you won!")
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()

                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        sub_total_score=0
                        continue
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        break
                stand_dealer(sub_total_score)
                if dealer_score[n] >= player_score[n]:
                    all_loses=all_loses+1
                    print(f"Dealer wins {dealer_score[n]} to {player_score[n]}\n")
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        sub_total_score=0
                        valid=True
                        continue
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        break

                else:
                    all_wins=all_wins+1
                    print(f"{player.name} wins {player_score[n]} to {dealer_score[n]}\n")
                    play_again=input(f"Want to play again {player.name}? yes/y/1 for yes, other keys to cashout").strip().lower()
                    if play_again=="yes" or play_again=="y" or play_again=="1":
                        n=n+1
                        sub_total_score=0
                        valid=True
                        continue
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        break
                            
                
            elif choice != "hit":
                valid=False

    else:
        print("You're too young to gamble, sorry.")
    