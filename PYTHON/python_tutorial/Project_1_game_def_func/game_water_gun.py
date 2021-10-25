import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, You):
     # If two values are equal, declare a tie!
    if comp == You:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if You == 'w':
            return False
        elif You =='g':
            return True

    # Check for all possibilities when computer chose w        
    elif  comp == 'w': 
        if You == 'g':
            return False
        elif You =='s':
            return True

    #  Check for all possibilities when computer chose g       
    elif  comp == 'g': 
        if You == 's':
            return False
        elif You == 'w':
            return True

print("Comp Turn: Snake(s) water(w) or gun(g)")
randNO = random.randint(1, 3)
if randNO == 1:
    comp = 's'
elif randNO == 2:
    comp = 'w'
elif randNO == 3:
    comp = 'g'

You = input("Your Turn: Snake(s) water(w) or gun(g): \n")
a = gameWin(comp,You )

print(f"computer chose{comp}")
print(f"you choose{You}")

if a == None:
    print("The game is a tie!")
elif a:
    print(" You win!")
else:
    print("You lose!")