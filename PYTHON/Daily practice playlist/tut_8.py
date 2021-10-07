# string slicing and other functions 


myStr =("Jayesh is a good boy")   #string
print(myStr)
print("**********************")


# string slicing
print(myStr[0:6])   #string sliced till 6th element
print(len(myStr))   #string length
print(myStr[0:32])   # sliced till end (elements are less than 32)
print(myStr[0:12:2])    # sliced as [start:end:gap]
print(myStr[-6:-1])   # sliced by negative index
print(myStr[::-1])   #string written in reverse
print("**********************")



# other functions

# to check whether the str is alpha numeric(check whether it ia alpha/numeric, without spaces )
print(myStr.isalnum()) 
print(myStr.isalpha())

# to check whether the str endswith given values
print(myStr.endswith("boy"))

# to count the values in the String 
print(myStr.count("o"))

# to uppercase the str
print(myStr.upper())

# to lowercase the str
print(myStr.lower())

# to capitaize the first lwtter of the string
print(myStr.capitalize())

# to find the position of value 
print(myStr.find("is"))

# to replace the value 
print(myStr.replace("is", "are"))





