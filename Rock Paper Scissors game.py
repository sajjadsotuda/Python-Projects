import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Please type rock, paper, scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    print(f"computer picked {computer_pick}")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won")
        user_wins += 1
        continue

    if user_input == "scissors" and computer_pick == "paper":
        print("You won")
        user_wins += 1
        continue

    if user_input == "paper" and computer_pick == "rock":
        print("You won")
        user_wins += 1
        continue

    else:
        print("you lost")
        computer_wins += 1
    
if computer_wins > user_wins:
     print(f"computer won by {computer_wins} over {user_wins}")
elif computer_wins == user_wins:
    print(f"It is a draw by {computer_wins} to {user_wins}")
else:
     print(f"You won by {user_wins} over {computer_wins}")

print("Bye")
