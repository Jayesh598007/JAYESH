# Exercise No: 2
# create Faulty calculator which will correctly solve all the problems except below ones

'''
Addition :   56+8 = 75
Division:  430/6 = 14
Multiplication:   234*4 = 630
'''

# solution >>>>>>

print("This is a Calculator: \n     pls enter below details as per given instructions \n + for addition \n - for substraction \n * for multiplication \n / for division")
print(" a and b are the numbers \n")

a = int(input("a: "))
op = input("(+, -, *, /): ")
b = int(input("b: "))

# Addition :   56+8 = 75
if op == "+":
    if (a==56 and b==8) or (b==56 and a==8) :
        print("75")
    else:
        result = a + b
        print(result)


# Division:  430/6 = 14
if op == "/":
    if (a==430 and b==6) or (b==430 and a==6) :
        print("14")
    else:
        result = a / b
        print(result)


# Multiplication:   234*4 = 630
if op == "*":
    if (a==234 and b==4) or (b==234 and a==4) :
        print("630")
    else:
        result = a * b
        print(result)

