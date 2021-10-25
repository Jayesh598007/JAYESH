#strip function
'''
this = "    Jayesh    "
print(this)   # o/p is in the form of quote as given ie: with spaces
print(this.strip())  # with this, o/p changes as  the quote without strip
'''
# remove a word and also strip the comment

def remove_and_strip(string, word):
    newStr = string.replace(word, "")   # func for  replacing the word
    return newStr.strip()   # func for striping the spaces

this = "    Jayesh is a good boy    "
n = remove_and_strip(this, "Jayesh")  # in o/p we are expecting to print the item wihtout Jayesh and without spaces
print(n)   # o/p will be 'is a good boy'





