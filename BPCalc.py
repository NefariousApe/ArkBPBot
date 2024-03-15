
from NameToBpDict import bpDict, tierDict
from Item import Item
import json

exampleOrder = "15 asc theri"
exampleHappy = "15 jr theri"

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

with open("AdatBp.json") as bpFile:
    data = json.load(bpFile)


def placeOrder(order):
    resetTotals()
    parsedOrder = parseOrder(order)
    status = getCosts(parsedOrder)
    if parsedOrder == "Error" or status == "Error":
        return matTotals, " ", "Error"

    return matTotals, orderToString(parsedOrder), ""


def resetTotals():
    for k in matTotals:
        matTotals[k] = 0


def lookupBP(bp):
    name = lookupName(bp)
    bps = "Error"
    if name != "Error":
        bps = getBps(name)
    return bps


def getBps(bp):
    bps = []
    for item in data:
        if item["Name"] == bp:
            bps.append(item)
    return bps


def orderToString(order):
    string = ""
    first = True
    for item in order:
        if first:
            string = item.toString()
            first = False
        else:
            string = string + ", " + item.toString()
    return string


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

    if len(items) > 0:
        for item in items:
            item = item.strip()
            singleItem = str.split(item, ' ')
            if len(singleItem) < 3:
                return "Error"
            amount = singleItem[0]
            tier = lookupTier(singleItem[1])
            name = lookupName(" ".join(singleItem[2:]))
            if tier == "Error" or name == "Error":
                return "Error"
            parsedOrder.append(Item(name, tier, amount))
    else:
        return "Error"
    return parsedOrder


def getCosts(order):
    for item in order:
        itemFound = False
        for bp in data:

            if bp["Name"] == item.getName() and bp["Rarity"] == item.getTier():
                itemFound = True
                start = False
                for key in bp.keys():
                    if key == "Fiber":
                        start = True
                    if start and bp[key] != None:
                        matTotals[key] = round(matTotals[key] +
                                               bp[key] * int(item.getAmount()) * 1.5)
        if not itemFound:
            return "Error"
    return "Success"


# bps = lookupBP("stego")
# response = ""
# for bp in bps:
#     response = response + f'''
#     # {bp["Rarity"]} {bp["Name"]}\n
# '''
#     for k, v in bp.items():
#         if v != None:
#             response = response + f'''
#             ## {k}: {v}\n
# '''
# print(response)

# test = lookupBP("rex")
# print(test)
# order, orderString, errMsg = placeOrder(exampleHappy)
# print(errMsg)
