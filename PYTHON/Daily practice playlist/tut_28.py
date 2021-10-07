# Exercise: 4
# print a pattern, taking input from user

'''
*
**
***
****
*****
'''
while True:

    n = int(input("Please enter any no: "))
    b = int(input("Please enter 1 or 0: "))

    if b==1:        # forward
        for i in range(1,n+1):
            print(i * '*')

    else:           # backward
        for i in range(n+1,0,-1):
            print(i * '*')
    pass

    if input('Do you want to repeat(y/n)') == 'n':
        break