# How to create a Indian Kirana Store Calculator and receipt generator

# write a python program which keep adding a stream of numbers input by the user.
# the adding stops as soon as the user hits + key on the keyboard


'''
Jay Ambe Kirana Store
'''

sum = 0
while(True):
    userInput = input("Enter the price ( or press '+' to quit): \n")
    if(userInput != '+'):
        sum = sum + int(userInput)
        print('Bill total so far: ', sum)

    else:
        print()
        print()
        print()
        print()
        print("Your total amount is:", sum)
        print('  Thanks for shopping!   ')
        print(' JAY AMBE KIRANA STORE  ')
        print('      Visit Again     ')
        print()
        print()
        print()
        print()
        break
