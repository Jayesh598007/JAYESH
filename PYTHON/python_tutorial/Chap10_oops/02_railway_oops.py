class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

railApl = RailwayForm()
railApl.name = "Jayesh"
railApl.train = "Rajdhani Express"
railApl.printData()

