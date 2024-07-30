

user1_wins = 0
user2_wins = 0

options=["rock", "paper","scissors"]

while True:
    user1_input = input("Type user 1 Rock/Paper/Scissors or Q to quit: ").lower()
    if user1_input == "q":
        break
    
    user2_input = input("Type  user2 Rock/Paper/Scissors or Q to quit: ").lower()
    if  user2_input == "q":
        break
    

    if user1_input not in options or user2_input not in options:
        continue

    if user1_input == "rock" and user2_input == "scissors":
        print("User1 Won!,Congratulations")
        user1_wins += 1

    elif user1_input == "paper" and user2_input == "rock":
        print("User1 Won!,Congratulations")
        user1_wins += 1
       

    elif user1_input == "scissors" and user2_input == "paper":
        print("User1 Won!,Congratulations")
        user1_wins += 1
    
    elif user1_input == user2_input:
        print("No points")

    else:
        print("User1 Lost!,Better luck next time")
        user2_wins += 1

if user1_wins < user2_wins:
    print("user2 Won!")
else:
    print("User1 Won!")

print("User1 won",user1_wins,"times." )
print("User2 Won",user2_wins,"times.")
print("Goodbye!")


