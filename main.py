import random

'''
1 for Rock
-1 for Scissors
0 for Paper
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ")
youDict = {"r": 1, "p": 0, "s": -1}
reverseDict = {1: "Rock", 0: "Paper", -1: "Scissors"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw")
else:
    if (computer == 1 and you == -1):  # Rock vs Scissors
        print("You lose!")
    elif (computer == 1 and you == 0):  # Rock vs Paper
        print("You win!")
    elif (computer == 0 and you == 1):  # Paper vs Rock
        print("You lose!")
    elif (computer == 0 and you == -1): # Paper vs Scissors
        print("You win!")
    elif (computer == -1 and you == 0): # Scissors vs Paper
        print("You lose!")
    elif (computer == -1 and you == 1): # Scissors vs Rock
        print("You win!")
    else:
        print("Something went wrong!")
