# sum(n) = sum(n-1) + n
# summation using func_recursion 

def sum(n):
    if (n==0):    # id n=0, then o/p will be 0
        return 0
    else:       # if n=/ 0, then o/p will be as per given condtn below
        return(sum(n-1) + n)

n = int(input("Enter:"))   # value of n to be entered by user

num= sum(n)
print(num)
