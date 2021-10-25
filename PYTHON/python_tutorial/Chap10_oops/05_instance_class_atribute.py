class Employee:  
    company = "Google" 
    salary = 100     # class attribute


harry = Employee() 
rajni = Employee()

#creating instance attribute salary for both the objects
# harry.salary = 300
rajni.salary = 400         # instance attribute

print(harry.salary)          # as instance attribute is missing, this will print the class attribute
print(rajni.salary)          # as instance attribute is present, this will not print the class attribute