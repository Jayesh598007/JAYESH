# Concatenating two strings

name= 'JAyesh'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# String Slicing
print(name[0:7])
print(name[0:4])
print(name[3:5])

print(name[0:]) # is same as [0:7]
print(name[:4]) # is same as [0:4]


# negative indexing

print(name[-1])
print(name[-3])
print(name[-6:-1]) # is same as [1:7]

#slicing with skip value
name = "JAyesh"
d = name[1:7:2]
print(d) 

