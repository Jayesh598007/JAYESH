mydict= {
"pankha": 'fan',
"Dabba": 'tiffin',
"rumaal": 'towel',
}

print("options are:" , mydict.keys())  # will show the hindi words( keys) available in dict
a = input("Enter the hindi Word:\n")  # user will enter the hindi word(keys) in dict
print("The meaning of your word is:", mydict.get(a))  # will show the answer/meaning of the hindi words in english(values) 
# if the keys entered in the input is not available in the dict, then it will show none