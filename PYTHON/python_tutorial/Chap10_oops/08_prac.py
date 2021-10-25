  # Create a class programmer to store a data of programmers working at microsoft
class programmer:    # class
    company = "Microsoft"   #class atribute

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def info(self):
        print(f"Name of this {self.company} programmer is {self.name} and the product is {self.product}")


harry = programmer("harry", "Skype")      #harry is an object and the product here is instance atribute
alka = programmer("alka", "Github")
harry.info()
alka.info()

