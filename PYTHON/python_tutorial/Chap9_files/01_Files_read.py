# a RAM is a volatile memory, so it deletes all the data when the browser/application is closed.
# in order to persist the data forever, we use "Files".

# A pthon program can read and write data into the file.
''' 
Types of files:
1)text files (.txt, etc)
2)binary files (.jpg, etc )
'''

# python has a lot of func to read, write, update, delete a file

# use open func() to read a file!

f = open("sample.txt" , 'r')  # 'r' is to read(mode)
# f = open("sample.txt")   # file can also be opened without 'r' to only read,  
data = f.read()  # read func
print(data)   # print the data in file
f.close()  # we need to close a file



