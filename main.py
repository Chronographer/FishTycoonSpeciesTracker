import easygui
import json


class fish:
    def __init__(self, name, parent1, parent2, price, environment, fish_dict, magic):
        self.__dict__.update(fish_dict)
        self.name = name
        self.parent1 = parent1
        self.parent2 = parent2
        self.price = price
        self.environment = environment
        self.magic = magic


def makeFish():
    name = pickName()
    easygui.msgbox("Select the 2 parent fish")
    parent1 = pickParent()
    parent2 = pickParent()
    price = setPrice()
    environment = setEnvironment()
    emptyDictionary = {}
    magic = isMagic()
    newFish = fish(name, parent1, parent2, price, environment, emptyDictionary, magic)
    return newFish


def pickName():
    name = easygui.enterbox("Enter the name of the fish")
    easygui.choicebox("this is a choice box", "title text", [0, 1, 3, 4, 5, 6])
    return name


def setPrice():
    price = easygui.integerbox("Enter the price of the fish")
    return price


def setEnvironment():
    environment = easygui.buttonbox("Select minimum environment", "Environment select", ["basic", "intermediate", "advanced", "unknown"])
    return environment


def isMagic():
    magic = easygui.boolbox("Is this fish magic?")
    return magic


def fishSelector(fishNameList):
    masterList = []
    target = len(fishNameList)
    counter = 0

    while target > 0:
        subList = ["no data", "no data", "no data", "no data", "no data", "manual", "back", "next"]
        masterList.append(subList)
        target = target - 5
    for index in range(0, len(masterList)):
        for sub_index in range(0, 5):
            masterList[index][sub_index] = fishNameList[counter]
            counter = counter + 1
            if counter == len(fishNameList):
                break
    fishSelect = "null"
    nameSubList = 0
    while fishSelect == "next" or fishSelect == "back" or fishSelect == "null" or fishSelect == "no data":
        fishSelect = easygui.buttonbox("Select the appropriate fish", "Fish Select", masterList[nameSubList])
        if fishSelect == "next":
            if len(masterList) >= nameSubList + 2:
                nameSubList = nameSubList + 1
            else:
                easygui.msgbox("There are no more fish in that direction")
        elif fishSelect == "back":
            if nameSubList - 1 >= 0:
                nameSubList = nameSubList - 1
            else:
                easygui.msgbox("There are no more fish in that direction")
        elif fishSelect == "no data":
            easygui.msgbox("You are not allowed to press this button.")
        elif fishSelect == "manual":
            easygui.msgbox("WARNING: This should ONLY be used to select parents who are not in the existing database.")
            fishSelect = pickName()
    print(fishSelect)
    return fishSelect


def manualParent():  # This lets you manually assign a parent fish name to a new fish even if the parent is not in the database.
    parent = pickName()
    return parent


def pickParent():
    fishNameList = constructFishCatalog()
    fishSelect = fishSelector(fishNameList)
    parent = getFishObjectFromName(fishList, fishSelect)
    return parent.name


def saveFish(obj_list):
    with open("jsonFish.json", "w") as f:
        f.write(json.dumps([obj.__dict__ for obj in obj_list], indent=4))
    return


def dict_to_fish(fish_dict):
    return json.loads(json.dumps(fish_dict), object_hook=fish)


def loadFish():
    fishCatalog = []
    with open("jsonFish.json", "r") as read_file:
        data = json.load(read_file)
    for index in range(0, len(data)):
        localFish = data[index]
        name = localFish["name"]
        parent1 = localFish["parent1"]
        parent2 = localFish["parent2"]
        price = localFish["price"]
        environment = localFish["environment"]
        magic = localFish["magic"]
        fish_dict = {}
        loadedFish = fish(name, parent1, parent2, price, environment, fish_dict, magic)
        fishCatalog.append(loadedFish)
    return fishCatalog


def constructFishCatalog():
    fishNameList = []
    for index in range(0, len(fishList)):
        fishNameList.append(fishList[index].name)
    return fishNameList


def getFishObjectFromName(fishList, fishSelect):
    fishObject = fish(fishSelect, "null", "null", "NaN", "null", {}, "false")  # This creates a dummy fish object for when you need to provide a parent fish name which does not exist in the database yet. It is discarded after; only its name is kept in its offspring's file.
    for index in range(0, len(fishList)):
        if fishSelect == fishList[index].name:
            fishObject = fishList[index]
    return fishObject


fishList = loadFish()
action = ""
while not action == "Exit":
    action = easygui.buttonbox("This is the main menu.", "main menu", ["New Fish", "View Fish", "Save Fish", "Exit"])
    if action == "New Fish":
        newFish = makeFish()
        fishList.append(newFish)
    elif action == "View Fish":
        fishNameList = constructFishCatalog()
        fishSelect = fishSelector(fishNameList)
        fishObject = getFishObjectFromName(fishList, fishSelect)
        easygui.textbox("Details for selected fish:", "Fish Details", "Name: " + fishObject.name + "\nParent: " + fishObject.parent1 + "\nParent: " + fishObject.parent2 + "\nPrice: " + str(fishObject.price) + "\nEnvironment: " + fishObject.environment + "\nMagic: " + str(fishObject.magic))
    elif action == "Save Fish":
        saveFish(fishList)
