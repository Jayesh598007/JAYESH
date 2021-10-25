def farh(cel):
    return(cel* 9/5) + 32    #this is the formula of converting celcius to farhenheit

c = int(input(" Enter the temp in celcius: "))

f= farh(c)
print("farhenheit tempis: ", str(f), "F")

# thus we get the output as temp in farhenheit