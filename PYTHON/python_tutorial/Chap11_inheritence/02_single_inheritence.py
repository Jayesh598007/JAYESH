'''
Types of Inheritence:
1) single inheritence
2) miltiple inheritence
3) Multilevel inheritence
'''

# Single Inheritence
# it occurs when child class inherits only one/single base class

    #  parent ------> child1

class Employee:
    company = "Google"     
    def showdetails(self):   
        print("This is an employee")

class Programmer(Employee):   
    lang ="Python"
    def getlang(self):      
        print(f"The language is {self.lang}")


e = Employee()
p = Programmer()

e.showdetails()    
p.showdetails()

print(e.company)      
print(p.company)   

p.getlang()