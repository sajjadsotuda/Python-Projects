name = input("Type your Name: ").capitalize() 
print(f"Welcome {name} to this adventure") 

while True:
    answer = input("\nYou are on a dirt road which way would you like to choose to adventure - right or left? ").lower()

    if answer == "left":
       
        answer = input("You came to a river you can walk around it or swim across? type walk to walk around or swim to swim across: ").lower()
        
        if answer == "swim":
            print("You swam across and were eaten by an alligator")
        elif answer == "walk":
            print("You walked for miles and got tired and didn't survive")
        else:
            print("Not a valid option, you lose")

    elif answer == "right":
       
        answer = input("You came to a bridge that looks wobbly, do you want to cross or turn around, write yes if you want to cross and no if you don't: ").lower()
        
        if answer == "no":
            print("You decided to turn around, so you lose!")
        elif answer == "yes":
            answer = input("You were able to cross the bridge and now meet a stranger, write yes if you want to talk to the stranger and no if you don't: ").lower()
            
            if answer == "yes":
                print("The stranger was kind and gave you gold, you won!")
            elif answer == "no":
                print("You had the chance to find new people to adventure with but you ignored them. You are now lost in the middle of nowhere, you lose")
            else:
                print("Not a valid option, you lose")
    else:
        print("Not a valid option, you lose")
    
    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"\nThank you for playing, {name}!")
        quit()
p
