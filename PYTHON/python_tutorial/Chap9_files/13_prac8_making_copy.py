# make a copy of a file 'this.txt'

with open("this.txt") as f:
    content = f.read()  # this reads the content of the file

with open("copy_this.txt" , 'w') as f:
    f.write(content)  # this creates and writes the content in the copied file
