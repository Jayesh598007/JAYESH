# Recursions: Recursive Vs Iterative Approach

# factorial()
# n! = n * n-1 * n-3 * n-4 ....... *1
# n! = n * (n-1)!

'''
def factorial_iterative(n):
    """
    :paramameter(n):    Integer
    :return(n):   n * n-1 * n-3 * n-4 ..... *1
        (5! = 5*4*3*2*1)
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number = int(input("Enter num: "))
print("The factorial using iterative method is", factorial_iterative(number))

'''


def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n* factorial_recursive(n-1)
    # 5! = 5* factorial_recursive(4)
    # 5! = 5* 4* factorial_recursive(3)
    # 5! = 5* 4* 3* factorial_recursive(2)
    # 5! = 5* 4* 3* 2* factorial_recursive(1)
    # 5! = 5* 4* 3* 2* 1 = 120
    
    
number = int(input("Enter num: "))
print("The factorial using recursive method is", factorial_recursive(number))



'''
#fibonaacci number

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n= int(input("Enter n: "))
print(fibonacci(n))
'''