# here we are replacing multiple words in the list by other words

words=["paagal", "mota", "chudel", "mental"]

with open("donkey.txt") as f:   # file name
    content = f.read()

for word in words:
    content = content.replace(word, "$#$#$#$#")  # words in the list will be replace by '$#$#$#'
    with open("donkey.txt" , 'w') as f:
        f.write(content)

print("done")
