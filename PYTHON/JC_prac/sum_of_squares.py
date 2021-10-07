n = int(input("Enter the number: "))
sum = 0
if n>0:
    for i in range(1, n+1):
        j = i*i    # square
        sum +=j   # sum of square
    print(f"The sum of squares of first {n} number {sum}")
    if sum%2 ==0:
        print(f"{sum} is an even number")
    else:
        print(f"{sum} is an odd number")