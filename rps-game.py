import random

user_choices = ["rock", "paper", "scissor"]

def init(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie.")
    elif user_choice == "rock" and computer_choice == "paper":
        print("Computer win")
    elif user_choice == "rock" and computer_choice == "scissor":
        print("You win")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win")
    elif user_choice == "paper" and computer_choice == "scissor":
        print("Computer win")
    elif user_choice == "scissor" and computer_choice == "rock":
        print("Computer win")
    elif user_choice == "scissor" and computer_choice == "paper":
        print("You win")

while True:
    print("====== Welcome to RPS game ======")
    print("Please enter a valid option: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("4. Exit")

    user_option = input("Enter a choice (1-4): ")

    if user_option == "4":
        print("Exiting the game. GoodBye!")
        break

    if user_option in ["1", "2", "3"]:
        user_choice = user_choices[int(user_option) - 1]
        ai_choice = random.choice(user_choices)

        print(f"You choosed {user_choice} and computer choosed {ai_choice}")
        init(user_choice, ai_choice)
    else:
        print("Invalid input. Please select a valid option.")