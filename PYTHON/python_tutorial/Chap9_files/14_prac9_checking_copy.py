# this checks whether the content in two files are similar or not

# entering the files names
file1 = "this.txt"
file2 = "copy_this.txt"
file3 = "log.txt"

# reading the file content
with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

with open(file3) as f:
    f3 = f.read()

# checking through conditions bet f1 and f2
if f1 == f2:
    print("file1 and file2 are identical")
else:
    print("file1 and file2 identical")

# checking through conditions bet f1 and f3
if f1 == f3:
    print("file1 and file3 are identical")
else:
    print("file1 and file3 are NOT identical")


