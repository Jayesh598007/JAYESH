# variables, datatypes and typecatsing

#variable
var1 = "Hello world"       # string
var2 = 50           # integer 
var3= 2.5      #float
var4 = "Jayesh"   # string
var5 = "20"   # string


print(var1)
print(var2 + var3)
print(var3)
print(var5)
print("***************************")


# string concatination
print(var1 + var4)


#datatypes 
'''
str()
int()
float().... and many more
'''
print(type(var1))
print(type(var2))
print(type(var3))


#type casting
# Converting possible datatype to other

# print(var2 + var5)   # this will show error, but
print(var2 + int(var5))

print(10 * var4)   # var4 is a str()
print(10 * str(var2 + int(var5)) )   # coverting int() to str() to get deserved o\p


#input from user
a= input()   # input is always taken as str()
b= input()
print(int(a) + int(b))   # we need to convert str() to int() before adding





