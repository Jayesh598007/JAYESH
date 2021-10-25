# n! = 1 X 2 X 3 X 4 X 5... X n
# 5! = 1 X 2 X 3 X 4 X 5

num =int(input("Enter the num:"))
factorial =1
for i in range (1, num+1):
    factorial = factorial*i
# print("The factorial of" + str( num ) + "is: " + str(factorial))  #another method
print(f"the factorial of {num} is {factorial}")  

