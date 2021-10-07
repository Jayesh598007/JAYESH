# break and continue statement 

'''
i = 0

while (True):
    if (i<20):
        i =i+2
        continue     # skips the currentiteration (for given condition) and executes the very next interation

    print( i+2, end=" ")

    if (i==50): 
        break     # teminates the whole loop at given conditions
        
    i= i+2

'''

# Exercise for loop
# take input from user until the input is more than 100

num = int(input("Enter any num: ")) 

while(True):
    num = int(input("Enter any num: "))

    if num>100:
        print("Your number is greater than 100  !!!")
        break
    else:
        print("Try again!")
        continue




