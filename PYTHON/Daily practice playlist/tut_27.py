# Writing And Appending a File 


# to write 
'''
f = open("jayesh.txt", "w")        # this (can create new file and) opens a file to write in it
f.write("Jayesh is a scholor student and he loves science \n")
# this deletes the content of the file and write another statement in the file
f.write("Jayesh has more interest in maths and science \n")
f.close()
'''


# to append 
'''
f = open("jayesh.txt", "a")     # this (can create new file and) opens a file to append(add at end)
f.write("Jayesh Chaudhari \n")
# this doesn't delete previous content but add new
f.write("Jayesh loves science \n")
f.close()
'''


# to read and write both 
f = open("jayesh1.txt", "r+")    # open new file, read and write in it
print(f.read())            # read
f.write("Thank You \n")         #write
f.close()


