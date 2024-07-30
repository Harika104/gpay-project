import random

user_wins = 0
computer_wins = 0

options=["rock", "paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    if user_input == "q":
        break

    if user_input  not in options:
        continue

    random_number = random.randint(0,2)
    
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("YOU Won!,Congratulations")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("YOU Won!,Congratulations")
        user_wins += 1
       

    elif user_input == "scissors" and computer_pick == "paper":
        print("YOU Won!,Congratulations")
        user_wins += 1
    
    elif user_input == computer_pick:
        print("No points")

    else:
        print("You Lost!,Better luck next time")
        computer_wins += 1

if user_wins < computer_wins:
    print("Computer Won!")
else:
    print("You Won!")

print("You won",user_wins,"times." )
print("Computer Won",computer_wins,"times.")
print("Goodbye!")


