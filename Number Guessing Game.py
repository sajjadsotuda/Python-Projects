import random

top_of_range = input("Type your top of range number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print("Please type a number next time.")
    quit()
if top_of_range <= 0:
    print("please type a number more than 0")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Please type in your guess: ")
    
    if user_guess.isdigit():
       
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
       
        continue
        
    if user_guess == random_number:
        print("You got it right!")
        break
    else:
        print("You got it wrong, please try again.")

print(f"You got it in {guesses} guesses ")



