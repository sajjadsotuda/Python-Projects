name = input("Hello There and welcom \n what is your name? ")
print(f"Hello {name}, Let's start the game!")

point = 0
Answer = input("What is chemical symbol of water? ").lower()
if Answer != "H20":
    print("Wrong Answer")
else: 
    print("Correct")
    point += 1

Answer = input("What is the chemical symbol of oxygen? ").lower()
if Answer != "O":
    print("Wrong Answer")
else: 
    print("Correct")
    point += 1

Answer = input("Which subatomic particle found in an atom has a negative electrical charge? ").lower()
if Answer != "Electrone":
    print("Wrong Answer")
else: 
    print("Correct")
    point += 1

Answer = input("Which state of matter has a definite volume but no definite shape? ").lower()
if Answer != "Liquid":
    print("Wrong Answer")
else: 
    print("Correct")
    point += 1

Answer = input("What element does the chemical symbol \"Na\" stand for? ").lower()
if Answer != "H20":
    print("Sodium")
else: 
    print("Correct")
    point += 1

Answer = input("Where are protons and neutrons located in an atom? ").lower()
if Answer != "Nucleus":
    print("Wrong Answer")
else: 
    print("Correct")
    point += 1

print("This is the end of the quiz")
print(f"You got {int(point)} questions correct")