f = open("sample.txt", 'rt')  
data = f.readline()  # it read only 1st line
print(data)   
data=f.readline()  # it reads only 2nd line
print(data)
data=f.readline()  # it reads only 3rd line
print(data)
f.close() 

# modes of opening a file
'''
1) r -- open for reading
2) w -- open for writing
3) a -- open for appending
4) t -- open for updating
'''

# IMP-- to open a binary file , 'rb' is used to read a file