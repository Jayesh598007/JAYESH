favlang = {}
a = input("Enter your favorite language Harshal\n:")
b = input("Enter your favorite language Mohit\n:")
c = input("Enter your favorite language Pooja\n:")
d = input("Enter your favorite language Yash\n:")

favlang['Harshal'] = a
favlang['Mohit'] = b
favlang['Pooja'] = c
favlang['Yash'] = d

print(favlang)
print(favlang.items())


# keys should be uinique in dict, no necessary for the values.
# thus , in above example, names should be unique, not necessary for languages.


