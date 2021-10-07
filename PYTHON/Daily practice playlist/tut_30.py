# Using 'With Block' to open Python Files


'''
f = open("jayesh.txt")      
print(f.readline()) 
f.close()
'''

with open('jayesh.txt') as f:   # this do not require to close the file 
    print(f.readline()) 
