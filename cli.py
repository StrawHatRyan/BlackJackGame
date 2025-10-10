from game import Player 
from dice import *

valid= True
bet_time=True
money=1000
bet_amount=0
house_busts_player_response_chooser=[1,2,3,4,5,6,7,8,9,0]
house_busts_player_response=["Karl the dealer: \n Sorry {player.name} better luck next time","Karl the dealer:\nThe house wins! {player.name}","Karl the dealer:\nI hope you had fun {player.name} I'm going to miss you","Karl the dealer:\nYou can't tell me you expected this to be easy right?","Karl the dealer: \nSorry {player.name} that you lost so much money but life is rough","Karl the dealer:\n: I won, I will get a raise.{player.name}\n: You're serious? Karl the dealer \n: I just make 14 an hour of course I'm not serious.","{player.name}:I wish I had more money. Karl the dealer: \n Yeah that is really too bad.","Karl the dealer: \n{player.name} You lost, the house wins, drinks on me.","Karl the dealer:\nCheer up {player.name} you're money will be well kept with the house, maybe","Karl the dealer:\n It's 12am just like that, I have kids at home, thank you for ending my shift {player.name}"]
# Ask for the player's name
name = input(" Welcome to Blackjack! What's your name? ").title()

# Create a Player object
player = Player(name)

# Greet the player
try_again=True
print(f"Hello, {player.name}! Let's play Blackjack!")
while try_again==True:
    try:
        age= int(input("How old are you?"))
        
        if age<0:
            print("Your age can't be negative you were born atleast sometime today.")     
            continue
        else:
            try_again=False
    except:
        print("Your age has to be a whole number")
        tried_again= True
        continue
    
    if age >= 18:
        while True:
            if valid==True:
                if money==0:
                    que=input("would you like to rebuy in? \n(yes/y/1 for yes other keys for no)")
                    if que== "yes" or que=="y" or que=="1":
                        print("Okay Good Luck")
                        money=1000
                    else:
                        print(house_busts_player_response[random.choice(house_busts_player_response_chooser)])

                print("round:",n+1)
                di = player_hit()  
                sub_total_score += di
                print(f"{player.name}, you rolled: {di}. Your total is now {sub_total_score}.")
                while bet_time==True:
                    try:
                        bet_amount=int(input(f"{player.name} you have ${money}.00  \nHow much would you like to bet, no max, minimun is $1."))
                        if bet_amount<=0:
                            print("The bet must be positive")
                            continue
                        else:
                            money=money-bet_amount
                            print(f"{player.name}'s money: {money}")
                            bet_time=False
                            print(f"{player.name} bet: {bet_amount}")
                            print(f"{player.name} you have cashed out with %{money}\n That is %{money/1000} of the starting starting stack")
                            
                    except:
                        print("Type whole numbers")

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
                        bet_time=True
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
                            bet_time=True
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
                            bet_time=True
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
                            bet_time=True
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
                    bet_time=True
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
                        bet_time=True
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
                        bet_time=True
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
                        bet_time=True
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
                        bet_time=True
                        continue
                    else:
                        print(f"{player.name} you've played {n+1} rounds")
                        print(f"{player.name} you have: \n{all_wins} wins and {all_loses} loses")
                        break
                            
                
            elif choice != "hit":
                valid=False

    else:
        print("You're too young to gamble, sorry.")
    