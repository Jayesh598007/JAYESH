# Sets in python 
# set only contains unique values, it does not contain duplicate values

s = set ( )
print(type(s))   #type 

lst = [3,5,7,8,3,6]  #removes duplicate values
set_list = set(lst)
print(set_list)

s.add(1)   # add new values
s.add(1)   # it does not contain duplicate values
s.add(2)
s.add(3)
print(s)

s.remove(3)   # removes given value
print(s)

s1 = s.union({1,4,3,2})    # adds new values to the set
print(s, s1)

s.intersection({1,4,3,5})   # only keeps similar values from comparison
print(s, s1)

