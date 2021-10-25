# multiplication = n X 1 = (n*1)

def print_table(num):
    for i in range(1,11):
        print(str(num), "X" , i, "=", str(num*i))

n= int(input("Enter the num: "))
print_table(n)


