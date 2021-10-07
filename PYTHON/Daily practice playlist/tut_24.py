# Try Except Exception Handling In Python 

# error can stop the execution of program 
# Try and Except statement is used to handle these errors within our code in Python 
# thus it is used to make code run even if error occurs to ru the code


num1 = input("Enter num1: ")
num2 = input("Enter num2: ")

try:          # this code runs if no error occurs
    print( "the Sum is",int(num1) + int(num2))
except Exception as e:        # this code runs if error occurs
    print(e)
finally:            # this code runs regardless of any exception(ie; error occurs or not)
    print("Thank You")



