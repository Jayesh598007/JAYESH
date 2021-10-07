# Python list and list functons

# list 
# list is a mutable datattype thus can be appended
grocery = ["harpic", "bhindi", "mela", 56, "lollipop", "karela"]
print(grocery)

# list slicing
print(grocery[4])
print(grocery[2:5]) 
print(grocery[::2])  # [start:end:gap]
print(grocery[::-1]) # reverse the list


# list of number
num = [2, 4, 5, 8, 3]
print(num)

# access the list item
print(num[2])

#reversing the list as it is (without any order)
print(num[::-1])

# sorting the list (in ascending order)
num.sort()
print(num)

# reversing the list (in descending order)
num.reverse()
print(num)

# max and min numbers from the list 
print(min(num))
print(max(num))

#appending (add at end) the list
num.append(7)
num.append(37)
print(num)

# inserting any value at specific position into the list 
num.insert(2, 67)   # (position,value)
print(num)

num[3] =300    # another way
print(num)

# removing any value from list 
num.remove(37)   
print(num)

# popping (remove from end) from the list
num.pop()
print(num)

# extend the data of list1 to list2
list=[ ]
list.extend(num)
print(list)

# clear all items for the list
num.clear()
print(num)


print("**********************************")
print("**********************************")


# tuple 
# tuple is immutable thus cannot be appended 
tp =(2, 9, 4.5, 7, 3)
print(tp)





