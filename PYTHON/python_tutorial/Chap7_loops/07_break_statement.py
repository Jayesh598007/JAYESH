# break statement

for i in range(10):
    print(i)
    if i==5:       # condition of 'i' applied to break the for loop
        break      # this function breaks the whole loop at given condition.
else:              # this does not executes as the "for" function has not executed till end, it was breaked
    print("this is inside else of for")
