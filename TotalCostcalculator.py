
from NameToBpDict import bpDict, tierDict
from Item import Item
import json

exampleOrder = "3 mc anky, 4 asc bary"


matTotals = {
    'Fiber': 0,
    'Hide': 0,
    'Metal': 0,
    'Wood': 0,
    'Cementing Paste': 0,
    'Flint': 0,
    'Obsidian': 0,
    'Chitin': 0,
    'Stone': 0,
    'Pelt': 0,
    'Silica Pearls': 0,
    'Crystal': 0,
    'Polymer': 0
}


def lookupName(name):
    for k, v in bpDict.items():
        for key in k:
            if key == name:
                return v
    return "Error"


def lookupTier(tier):
    for k, v in tierDict.items():
        for key in k:
            if key == tier:
                return v
    return "Error"


def parseOrder(order):
    parsedOrder = []
    items = order.split(',')

    for item in items:
        item = item.strip()
        singleItem = str.split(item, ' ')
        amount = singleItem[0]
        tier = lookupTier(singleItem[1])
        name = lookupName(" ".join(singleItem[2:]))
        parsedOrder.append(Item(name, tier, amount))
    return parsedOrder


order = parseOrder(exampleOrder)


with open("AdatBp.json") as bpFile:
    data = json.load(bpFile)

for item in order:
    for bp in data:
        if bp["Name"] == item.getName() and bp["Rarity"] == item.getTier():
            start = False
            for key in bp.keys():
                if key == "Fiber":
                    start = True
                if start and bp[key] != None:
                    matTotals[key] = matTotals[key] + \
                        bp[key] * int(item.getAmount())

print(matTotals)


# for bp in data:
#     if bp["Name"] == "Ankylo":
#         print("Hello")
