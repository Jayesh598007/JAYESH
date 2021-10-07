#Open(), Read() & Readline() For Reading File


from os import close


f = open("jayesh.txt")         # open the file 
# ^^ can also be written as -->>>  f = open("jayesh.txt", "rt") ie; read as text(default)

content= f.read(2)      # reads 2 characters
print(content)

content= f.read(4)       # reads 4 characters
print(content)

content= f.read()        # reads remaining characters
print(">>>", content)        # prints given charc before content

f.close()         #close the file                     

print("*****************************")

f = open("jayesh.txt")
# print(f.readlines())        #stores all lines in a list
print(f.readline())         #readline 1
print(f.readline())         #readline 2

print("*****************************")

f = open("jayesh.txt")
for line in f:          #to print all lines
    print(line)        
    
f.close()