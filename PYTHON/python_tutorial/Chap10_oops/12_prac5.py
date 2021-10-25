# write a class train
# it has methods to book ticket, get status, and get fare information
# of the trains running under indian railways

class train():
    company = "Indian Railways"

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print(f"The name of the train is {self.name}")
        print(f"the seats available are:{self.seats}")
    
    def getfare(self):
        print(f"The price of the ticket is {self.fare}")

    def bookticket(self):
        if (self.seats>0):
            print(f"Your ticket has been booked, your seat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry, the seats are full, Kindly try in tatkal")

    def cancelticket(self):
        pass


intercity = train("'Intercity Express: 14901'", 90, 2)

intercity.getstatus()    # intercity status before booking
intercity.getfare()
print()                    # for blank space

intercity.bookticket()   # booking a seat-->no.2, in intercity
intercity.bookticket()     #booking a seat-->no.1, in intercity
intercity.bookticket()     # as there is no seats available in the train, it showa a sorry message
print()
intercity.getstatus()      # intercity status after booking the seats
intercity.cancelticket()
