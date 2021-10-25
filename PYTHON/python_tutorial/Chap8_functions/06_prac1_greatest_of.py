num1= int(input("Enter: "))
num2= int(input("Enter: "))
num3= int(input("Enter: "))

def max(num1, num2, num3):
    if (num1> num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = max(num1, num2, num3)
print("The max num is:", str(m))

# we are here checking the greatest value among the three
    