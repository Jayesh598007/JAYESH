# to find the line of the word 'python' in the 'log.txt' file

content = True
i = 1
with open("log.txt") as f:
    while content:
        Content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"yes the python is present on line number{i}")
        i+=1
print("done")


