# renaming and copying a new file 

with open("sample.txt") as f:
    content = f.readline()

with open("new_sample.txt", 'w') as f:
    f.write(content)