# Exercise no: 6
# Game Development: Snake Water Gun 

print("\nHello,\nThis programme is developed by MK.\n")
print("Welcome to the Stone-Paper-Scissors Game.")
print("1 for Stone\n2 for Paper\n3 for Scissors")

import random
list = ["St", "P", "Sc"]

chances=10
no_of_chanse=0
your_point=0
computer_point=0

while (no_of_chanse<10):

    num = int(input("\nEnter your choise:"))
    rand = random.choice(list)

    if (num==rand):
        print(f"\nYour guess: {num}\nComputer's guess: {rand}")
        print("Tie.\nBoth have 0 point.")

    elif (num==1 and rand=="P"):
        computer_point += 1
        no_of_chanse+=1
        print("\nYour guess: Stone\nComputer's guess: Paper\n\nComputer wins 1 point.\n")
        print(f"Your points: {your_point}\nComputer's points: {computer_point}\n")

    elif (num==1 and rand=="Sc"):
        your_point += 1
        no_of_chanse += 1
        print("\nYour guess: Stone\nComputer's guess: Scissors\n\nCongratulation, you wins 1 point.\n")
        print(f"Your points: {your_point}\nComputer's points: {computer_point}\n")

    elif (num==2 and rand=="St"):
        your_point += 1
        no_of_chanse += 1
        print("\nYour guess: Paper\nComputer's guess: Stone\n\nCongratulation, you wins 1 point.\n")
        print(f"Your points: {your_point}\nComputer's points: {computer_point}\n")

    elif (num==2 and rand=="Sc"):
        computer_point += 1
        no_of_chanse += 1
        print("\nYour guess: Paper\nComputer's guess: Scissors\n\nComputer wins 1 point.\n")
        print(f"Your points: {your_point}\nComputer's points: {computer_point}\n")

    elif (num==3 and rand=="St"):
        computer_point += 1
        print("\nYour guess: Scissors\nComputer's guess: Stone\n\nComputer wins 1 point.\n")
        print(f"Your points: {your_point}\nComputer's points: {computer_point}\n")

    elif (num==3 and rand=="P"):
        your_point += 1
        no_of_chanse += 1
        print("\nYour guess: Scissors\nComputer's guess: Paper\n\nCongratulation, you wins 1 point.\n")
        print(f"Your points: {your_point}\nComputer's points: {computer_point} \n")

    else:
        print("\nInvalid input!!!")
        print("Please, enter 1 for Stone, 2 for Paper and 3 for Scissors.")

while (no_of_chanse==10):

    if (your_point>computer_point):
        print(f"\nCongratulation, you win with {your_point} points.")

    elif (your_point<computer_point):
        print(f"\nOhhh no, Computer is win with {computer_point} points.")

    else:
        print("\nMatch is Draw.\n")
        print(f"Your points: {your_point}\nComputer's points: {computer_point}\n")

    break