myDict = {
    "Fast": " In a quick manner" ,
    "Jayesh": " A Coder" ,
    "spps": "Smita Patil Public School", 
    "dyp": "D Y Patil",
    "marks": [1, 4, 2],
    "anotherdict": {"harry": 'player'}
}

 # dictionary methods
'''
print(myDict.keys())  # printing all keys in dict
print(myDict.values()) # printing all values in dict
print(myDict.keys() and myDict.values()) # printing keys and values
print(list(myDict.keys())) # print all keys in a list[]

print(myDict.items())  # print all items(keys, values) of the dict
'''
###

'''
print(myDict)
updateDict = {    # new contents to update in mydict
    "Kunal": 'friend', 
    "pooja": 'friend'
}

# adding/update any new contents in mydict
myDict.update(updateDict)    
print(list(myDict)) 
'''

print(myDict.get("spps")) 
print(myDict['spps']) 

# diff bet .get and [] syntax in dict
print(myDict.get("spps1")) # wrong key output will shoow none
''' print(myDict['spps1']) ''' # wrong key arrow will show error
