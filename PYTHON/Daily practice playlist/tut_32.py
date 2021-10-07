# Scope, Global  Variables and Global Keyword


# The availability of any variable is called as Scope 

# Global variables are available from within any scope, global and local, thus belongs to the global scope
l = 20           # global variable 
b = 12
m = 15
print(l)


# Local variables are created inside a function belongs to the local scope of that function, and can only be used inside that function 
def func1(n):
    l = 5        # local variable 
    m = 28
    l = l + 450
    print(l)
    print(m+b)   # here "m is local var(available)" and "b is global var( not available)"
    print(n) 
func1("jay")
print(l)


# If you need to create/change a global variable, but are stuck in the local scope, you can use the global keyword 
def func2(n):
    print(n)
    global l    # accessing global values 
    l = l+ 450        # global var changed in local scope 
    print(l)
func2("kartik")
print(l)



'''

x = 20
def r():
    x = 30
    def h():
        global x 
        x = 50
    print(x)
    h()
print(x)
r()
print(x)

'''









