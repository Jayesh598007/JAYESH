# can we change the self parameter inside a class to other name such as 'harry' or 'jayesh'


class sample:  
    a = "harry"  
    def __init__(jayesh, name):
        jayesh.name = name

obj = sample("harry")
print(obj.name)  

#yes we can change the 'self' identifier by other name
# self is used for better understandability
# otherwise we can changed it to any name
   
