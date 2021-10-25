with open('sample.txt', 'r') as f:
    a = f.read()
with open('sample.txt', 'w') as f:
    a = f.write("me")
print(a)
print('done')


# benefits of above with func is we do NOT need to close the func
# it automatically opens and closes the file

