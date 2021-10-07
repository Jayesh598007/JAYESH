# F-Strings & String Formatting In Python 
# F-strings are faster than the two most commonly used string formatting mechanisms, which are % formatting and str.format() 


me = 'jayesh'
fth = "sanjay"
sur = "chaudhari"

# % formating  
a = "my name is %s %s %s" %(me, fth, sur)
print(a)


# str.format()
a = "my name is {} {} {}"
a = a.format(me, fth, sur)
print(a)
 

# f-strings 
print(f"my name is {me} {fth} {sur}, you can contact him on {8380884059}, 24x7 ")