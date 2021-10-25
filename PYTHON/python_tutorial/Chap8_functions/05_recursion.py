# recursion  example

# 4!  = 1 X 2 X 3 X 4     # Factoral of 4

# simple factorial method
'''
# n = int(input("Enter the num:"))
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)
'''

# factorial_iter method
'''
def factorial_iter(n):
    product = 1
    for i in range(n):
         product = product * (i+1)
    return(product)

print(factorial_iter(3))
'''

#factorial_recursive method
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(3))


# recursion is a func which calls itself,
# it is used to directly use a mathematical formula
#  n! = n X (n-1)!

#IMP: need to be careful while solving recursion, we need to put a condition, to ensure that the func doesnt call itself infinitely
