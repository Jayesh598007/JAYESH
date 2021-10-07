# Dictionary and its functions 
# it is nothing but (key:value) pairs

d1 = {
    "harry" : "burger",
    "rohan" : "fish",
    "rohit" : "roti",
    "shubham":{
        "breakfast":"egg",
        "lunch":"paneer",
        "dinner":"chicken",
    }
}
print(type(d1))   #type

#print all dictionary
print(d1)   
print(d1.keys())
print(d1.values())
print(d1.items())

# print value of  specific key
print(d1["harry"])           #only single dict
print(d1["shubham"] ["breakfast"])           # dict within a dict

# adding new key and value to the dict 
d1["ankit"] = "pizza"
d1["jayesh"]= "laddo"
print(d1)

# remove any key and value from dict
del d1["ankit"]
print(d1)

# copy of any dict 
d2 = d1.copy()
del d2["shubham"]
print(d2)

# get the value of key 
print(d2.get("jayesh"))

# update the key value 
d2.update({"kartik":"toffee"})
print(d2)

# changing the value of keys in dict 
d2["jayesh"]= "halwa"
print(d2)



