# Need a dictionary to store all the wanted conversion rates.
# Rates are all towards converting per USD.
conversion_rate = {"USD": 1, "EUR": .89, "BTC": .0016, "JPY": 100.3, "GBP": 0.77, "CAD": 1.32, "MXN": 19.8981}

# Got help with the equation to convert from Tommy.
def conversion(self, other):
    other.amount = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
    return other.amount

class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        conversion(self, other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        conversion(self, other)
        return Money(self.amount - other.amount, self.currency)

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
        return Money(self.amount * other.amount, self.currency)

    def __eq__(self, other):
        conversion(self, other)
        return self.amount == other.amount

    def __ne__(self, other):
        conversion(self, other)
        return self.amount != other.amount

    def __str__(self):
        return "{} {}".format(self.amount, self.currency)

# Prints out the Math functions of the converting rates.
print(Money(100, "USD") + Money(56.32, "EUR") + Money(1.2, "BTC") + Money(8, "USD"))
# Prints out the Boolean functions of the converting rates.
print(Money(10, "USD") >= Money(10, "EUR"))
