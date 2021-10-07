# this program gives the list of all data input by the user


data = []
while (True):
    x = input('Enter:')
    if x == '+':
        break
    data.append(x)
print(data)
    

for item in data:
    print(item)

