# Anonymous/Lambda Functions In Python 
# A lambda function can take any number of arguments, but can only have one expression 


# below add function can also be written as lambda function

'''
def add(a,b):
    return a+b
print(add(5,6))
'''

add = lambda a, b: a+b
print(add(5,6))


# sorting using lambda instea of 

'''
def first(a):
    return a[1]

a = [[1, 14], [5,6], [8, 23], [2,4]]
a.sort(key = first)
print(a)
'''

a = [[1, 14], [5,6], [8, 23], [2,4]]
a.sort(key = lambda a:a[1])
print(a)



 