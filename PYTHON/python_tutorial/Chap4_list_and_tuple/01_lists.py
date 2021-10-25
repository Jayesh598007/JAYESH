'''  Python lists are the containers to store a set of values
  Values can of diff data types
'''

# creating a list using []
a= [13 , 62 , 73 , 45 , 51, 36]

# print the list using print() functn
print(a)
''' thus the output is in same order'''

# access with index using a[0], a[3], a[2]

print(a[0])   # value at 0 postn
print(a[0:4]) # all values betn 0-4
print(a[-1])  # value at 1 postn from behind
print(a[0:])  # all values rom 0 postn

# change the value of list using
a[0] = 98
print(a)  

# we can create a list with items of diff data types

c= [45,"harry",4.6,False]
print(c)
print(type(c[1]))


