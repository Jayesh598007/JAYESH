# default parameter value is a value added in func, whichis when used if no argument is passed/entered

name = input(" Enter:")
def greet(name= " Stranger"):  # 'stranger' here is a default parameter value
    print("Hello!" + name)
greet(" " + name)   # thus output here is "name"
greet()   # thus output here is stranger
