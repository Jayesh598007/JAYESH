# we need donkey work to be replaced by some characters

with open("donkey.txt") as f:   # file name
    content = f.read()

content = content.replace("donkey", "$#$#$#$#")  # 'donkey' will be replace by '$#$#$#'

with open("donkey.txt" , 'w') as f:
    f.write(content)

print("done")
