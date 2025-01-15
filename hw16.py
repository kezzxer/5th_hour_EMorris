#Name:Ethan Morris
#Class: 5th Hour
#Assignment: HW16

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
import random
def play_round():
    user_choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors!!!: "))
    player_choice = random.randint(1, 3)
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"Your choice: {choices[user_choice]}")
    print(f"Opponent's choice: {choices[player_choice]}")
    if user_choice == player_choice:
        print("It's a tie!")
    elif (user_choice == 1 and player_choice == 3) or (user_choice == 2 and player_choice == 1) or (
            user_choice == 3 and player_choice == 2):
        print("You win!")
    else:
        print("You lose!")
def play_again():
    while True:
        play_round()
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing!")
            break
play_again()

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
# Function to prompt user if they want to play again
def play_again():
    while True:
        play_round()


        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing!")
            break



play_again()