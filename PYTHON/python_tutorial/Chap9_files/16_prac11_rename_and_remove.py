# renaming a new file and deleting the old one
# import os

with open("sample2.txt") as f:
    content = f.readline()

with open("now_python.txt", 'w') as f:
    f.write(content)

# os.remove("sample.txt")