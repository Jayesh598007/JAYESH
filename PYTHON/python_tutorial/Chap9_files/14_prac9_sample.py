# entering the files names
file1 = str(input("Enter1:"))
file2 = str(input("Enter2:"))

# reading the file content
with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

# checking through conditions bet f1 and f2
if f1 == f2:
    print("file1 and file2 are identical")
else:
    print("file1 and file2 are not identical")