num1= int(input("enter the no1: \n"))
num2= int(input("enter the no2: \n"))
num3= int(input("enter the no3: \n"))
num4= int(input("enter the no4: \n"))

if (num1> num4):  # here we get greatest amony both as 'f1'
    f1 = num1
else:
    f1 = num4

if (num2>num3):  #  here we get greatest amony both as 'f2'
    f2 = num2
else:
    f2 = num3

if ( f1>f2):  # here we get greatest amony both as 'num'
    num= f1
else:
    num = f2
print("The largest no. among above is", num) # printing num- greatest among all





