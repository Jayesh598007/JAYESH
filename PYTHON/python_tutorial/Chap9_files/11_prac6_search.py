# to check whether a word 'python' is present in 'log.txt' file

with open("log.txt") as f:
    content = f.read()

if 'python' in content.lower():  # it will also search for the lower characters of the words if any
    print("python is present")
else:
    print("no python is present")