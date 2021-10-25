# print a pattern as given below
#     *
#    ***
#   *****          ...... for n=3

n=  3 #int(input(" Enter the num: \n"))

for i in range(n):
    print(" " * (n-i-1), end=" ")
    print("*" * (2*i+1), end= " ")
    print(" " * (n-i-1))
