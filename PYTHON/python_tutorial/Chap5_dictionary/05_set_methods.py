# empty set
b= set()
print(type(b))

# adding items in a set (hashable data only/ immutable)
b.add(4)
b.add(5)
b.add('#')
b.add(5)  #multiple elements are not saved in sets
b.add('Jay')
''' b.add([4, 5, 7]) ''' # list cannot be added in sets, as lists are mutable
b.add((3, 7, 8))  # tuple can be added, coz items in a tuple are immutable
''' b.add({4:5}) '''  #dictionary cannot be added
print(b)

# prints the length of set
print(len(b))   

# removal of an element written in ( )
b.remove(5) 
''' b.remove(15) '''  # thwors an error while tring to remove any element which is not present in the set
print(b)
print(len(b))
 
# pop out any arbitrary( selfly) item from set
print(b.pop())
print(b)

# clear the set
print(b.clear())
print(b)







