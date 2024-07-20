import random


def determine_winner():
    user_choice_input = input("Enter Your Choice (Rock,Paper,Scissors): ").lower()
    computer_choice_input = random.choice(["rock","paper","scissors"])
    print(f"Computer Choice: {computer_choice_input}")
    
    if user_choice_input == computer_choice_input:
        print("It's a Tie")

    elif user_choice_input == "rock":
        if computer_choice_input =='scissors':
            print("Rock Crushesh Scissors: You Win!")
        else:
            print("Paper Covers Rock: You Lose")
    elif user_choice_input == "paper":
        if computer_choice_input == "rock":
            print("Paper Covers rock : You Win!")
        else:
            print("Scissors Cuts Paper: You Lose")
    elif user_choice_input == 'scissors':
        if computer_choice_input=='paper':
            print("Scissors Cuts Paper: You Win!")
        else:
            print("Rock Crushesh Scissors: You Lose")
    else:
        print("You made a Wrong Choice! Please Select From Above")


determine_winner()











