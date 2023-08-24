import random




def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ")
    return choice.lower()

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
    
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "paper":
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == "paper":
        if computer_choice == "scissors":
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == "scissors":
        if computer_choice == "rock":
            return "Computer wins!"
        else:
            return "You win!"
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again."



def play_game():
    print("Let's play Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

play_game()
