# Exercise no: 5
# create a health management system

'''
# design a diet system, exercise for your clients 
# wtite a function that when executed takes as input client name
# total 6 files 
'''


def getdate():
    import datetime
    return datetime.datetime.now()

def food():
    print("Which food do you add to the list")
    client_food = input()
    return client_food

def exercise():
    print("Which exercise do you add to the list")
    client_exercise = input()
    return client_exercise

print("For whom do you want to make/make changes the file ??")
client_name = int(input("Enter '1' for jainesh / '2' for garima / '3' for madhav: \n"))

print("What do you want to record ??")
client_record = int(input("Enter '1' for food / '2' for Exercise:\n"))

if client_name == 1:
    if client_record == 1:
        f = open('tut_31/jainesh-food.txt', "a")
        f_food = food()
        f_date = str(getdate())
        f.write("[" + f_date + "]   " + f_food + " \n ")
        print('Thank-You for adding', f_food, "to the list\n")
        f.close()
    elif client_record == 2:
        f = open('tut_31/jainesh-exercise.txt', "a")
        f_date = str(getdate())
        f_exercise = exercise()
        f.write("[" + f_date + "]   " + f_exercise)
        print('Thank-You for adding', f_exercise, "to the list\n")
        f.close()
    else:
        print("please enter a valid record")

if client_name == 2:
    if client_record == 1:
        f = open('tut_31/garima-food.txt', "a")
        f_food = food()
        f_date = str(getdate())
        f.write("[" + f_date + "]   " + f_food)
        print('Thank-You for adding', f_food, "to the list\n")
        f.close()
    elif client_record == 2:
        f = open('tut_31/garima-exercise.txt', "a")
        f_date = str(getdate())
        f_exercise = exercise()
        f.write("[" + f_date + "]   " + f_exercise)
        print('Thank-You for adding', f_exercise, "to the list\n")
        f.close()
    else:
        print("please enter a valid record")

if client_name == 3:
    if client_record == 1:
        f = open('tut_31/madhav-food.txt', "a")
        f_food = food()
        f_date = str(getdate())
        f.write("[" + f_date + "]   " + f_food)
        print('Thank-You for adding', f_food, "to the list\n")
        f.close()
    elif client_record == 2:
        f = open('tut_31/madhav-exercise.txt', "a")
        f_date = str(getdate())
        f_exercise = exercise()
        f.write("[" + f_date + "]   " + f_exercise)
        print('Thank-You for adding', f_exercise, "to the list\n")
        f.close()
    else:
        print("please enter a valid record")

