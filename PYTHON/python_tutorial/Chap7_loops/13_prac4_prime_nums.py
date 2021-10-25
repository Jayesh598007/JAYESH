#prime number  = num which is divided by itself and 1 only

num = int(input(" Enter the num:\n"))
prime = True

for i in range(2, num):
    if(num%i==0):
        prime = False
        break

if prime:
    print("this is a prime num")
else:
    print("This is not a prime num")


