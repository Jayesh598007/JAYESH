# for Loops in python

lst = [["harry",16], ["jayesh" ,83],["mahesh",45], ["kartik",65]]

'''
for items in lst:
    print(items)
'''
for items,num in lst:
    print(num)
    print(items, num)
    


# typecasting list into dictionary 
'''
dct = dict(lst)   # converting a list into a dictionary 
print(dct)

for items in dct:  #for keys only
    print(items)

for items in dct.items():     # for both keys and values
    print(items)
'''


# exercise 
# make a list and print only those elements which are numbers and greater than 6

elem = (23, "sanjay", 6,int, 67, "kartik", 5,float, 10,4,"jayesh", 123,3 ,56, 32, 4, 23)

for items in elem:
    if type(items)==int and items>6:
        print(items)


        

