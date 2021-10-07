# Functions And Docstrings 

# function is a block of code that only runs when it is called
# it can be built-in  or user-defined 

# docstrings (or documentation strings) provide a brief info of Python modules, functions, etc 
# The docstrings can be accessed using the __doc__ method 


# bulit-in function
'''
a = 17
b = 6
c= sum((a,b))  
print(c)
'''

#user defined function
def func1(a, b):
    print("Hello, you are learning python", a + b)
func1(12, 5)


def func2(a, b):
    '''This is a function which will calculate average of two numbers,
    this function doesnt work for three numbers'''
    average = (a+b)/2
    return average
                    # Python functions return a value using a return statement, if one is specified 

v = func2(12, 6)
print("the avg is",v)
print("the avg is",str(v))
print("the avg is "+str(int(v)))

print(func2.__doc__)    # to print the docstring



# sample functions 
def recharge(n, no):
    print("Hello!", n +  ", your recharge of Rs.299 in '" + str(no) +  "' mobile number has been exhausted, recharge it to enjoy our service \n --Jio \n ")
    return recharge


def call(n , no):
    print("Hello!", n +  ", your have activated UNLIMITED calling package for the next month on your '" + str(no) + "' mobile number, pls Enjoy! \n --Jio \n")
    return call

recharge("jayesh" ,8380884059)
call("Sanket Patel", 8275590195)




