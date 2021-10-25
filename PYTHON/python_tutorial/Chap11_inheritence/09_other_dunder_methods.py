class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):    # to obtain/print the number n
        return f"Decimal number: {self.num}"

    def __len__(self):   # to determine the len of num
            return 1

n = Number(5)
print(n)
print(len(n))
