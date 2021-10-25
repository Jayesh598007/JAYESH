#  create a class with class attribute a,
# and check whether the class attribute changes by changing the instance attribute

class sample:    # class
    a = "harry"  # class attribute


obj = sample()     # object/ instance
obj.a = "vicky"    # instance attribute
print(sample.a)    # printing class sttribute
print(obj.a)       # printing instance attribute

sample.a = "Jayesh"   # changed class attribute
print(sample.a)       # printing the changed class attribute


# thus we find that by changing instance attibute, it does not affect the class attribute
# but, by changing class attribute, instance attribute is changed by-default ONLY if it is not specified
