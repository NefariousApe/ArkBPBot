class Item(object):
    name = ""
    tier = ""
    amount = 0

    def __init__(self, name, tier, amount):
        self.name = name
        self.tier = tier
        self.amount = amount

    def setName(self, name):
        self.name = name

    def setTier(self, tier):
        self.tier = tier

    def setAmount(self, amount):
        self.amount = amount

    def getName(self):
        return self.name

    def getAmount(self):
        return self.amount

    def getTier(self):
        return self.tier

    def toString(self):
        return self.amount + ", " + self.tier + ", " + self.name


def createItem(name, tier, amount):
    item = Item(name, tier, amount)
    return item
