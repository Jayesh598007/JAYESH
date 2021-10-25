# Creating a dictionary
'''
features of dict
1) it is unordered
2) it is mutable( changeable)
3) it is indexed
4) cannot contain duplicate keys
'''
# within a dictionary, it has, Key and its ValueE
''' key : value
    question : problem
'''

myDict = {
    "Fast": " In a quick manner" ,
    "Jayesh": " A Coder" ,
    "spps": "Smita Patil Public School", 
    "dyp": "D Y Patil",
    "marks": [1, 4, 2],
    "anotherdict": {"harry": 'player'}
}

print(myDict)
print(myDict["Fast"])
print(myDict["spps"])
print(myDict["Jayesh"])
print(myDict['marks'])  # here it prints the corresponding value of the key, in above dict
print(myDict["anotherdict"]['harry']) #here, we have found the value('player') of a key('harry'), within a key('anotherdict') in dictionary('myDict')


# editing the dictionary 
myDict['marks'] = [ 34, 56, 12]
print(myDict['marks'])
