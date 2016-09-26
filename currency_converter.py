# Need a dictionary to store all the wanted conversion rates.
# Rates are all towards converting per USD.
conversion_rate = {"USD": 1, "EUR": .89, "BTC": .0016, "JPY": 100.3}

class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        # Got help with the equation to convert from Tommy.
        money = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
        return self.amount + money

    def __sub__(self, other):
        money = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
        return self.amount - money

    def __ge__(self, other):
        money = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
        return self.amount >= money

    def __le__(self, other):
        money = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
        return self.amount <= money

    def __gt__(self, other):
        money = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
        return self.amount > money

    def __lt__(self, other):
        money = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
        return self.amount < money

    def __mul__(self, other):
        money = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
        return self.amount * money

    def __eq__(self, other):
        money = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
        return self.amount == money

    def __ne__(self, other):
        money = conversion_rate[self.currency]/conversion_rate[other.currency]*other.amount
        return self.amount != money


# Prints out the Math functions of the converting rates.
print("{0:.2f}".format(Money(1, "BTC") + Money(100, "EUR")))
# Prints out the Boolean functions of the converting rates.
print(Money(10, "USD") >= Money(10, "EUR"))
