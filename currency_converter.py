# Need a dictionary to store all the wanted conversion rates.
# Rates are all towards converting per USD.
conversion_rate = {"USD": 1, "EUR": .89, "BTC": .0016, "JPY": 100.3}
money_c = 0

def conversion(self, other):
    other.amount = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
    return other.amount

class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


    def __add__(self, other):
        # Got help with the equation to convert from Tommy.
        conversion(self, other)
        return self.amount + other.amount

    def __sub__(self, other):
        conversion(self, other)
        return self.amount - other.amount

    def __ge__(self, other):
        conversion(self, other)
        return self.amount >= other.amount

    def __le__(self, other):
        conversion(self, other)
        return self.amount <= other.amount

    def __gt__(self, other):
        conversion(self, other)
        return self.amount > other.amount

    def __lt__(self, other):
        conversion(self, other)
        return self.amount < other.amount

    def __mul__(self, other):
        conversion(self, other)
        return self.amount * other.amount

    def __eq__(self, other):
        conversion(self, other)
        return self.amount == other.amount

    def __ne__(self, other):
        conversion(self, other)
        return self.amount != other.amount

# Prints out the Math functions of the converting rates.
print("{0:.2f}".format(Money(10, "USD") + Money(10, "EUR")))
# Prints out the Boolean functions of the converting rates.
print(Money(10, "USD") >= Money(10, "EUR"))
