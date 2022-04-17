import json
f = open("save_0.sav", "r")
data = json.load(f)

def printCIDs():
    for i in range(len(data["LastPlayedRound"]["SavedCards"])):
        print(i, ":", " " ,data["LastPlayedRound"]["SavedCards"][i]["CardPrefabId"], end = '')
        if data["LastPlayedRound"]["SavedCards"][i]["IsFoil"]:
            print("-Foil", end = "")
        print()

print("welcome to the stax hax console \n type help for...      ...help")
active = True
while active:
    consoletext = input(">")
    if consoletext == "help":
        print("""Here are commands
cardids - print all card names with ids
rawcard [id] - get raw json of card
foil [id] - turn card into foil
defoil [id] - turn card into non foil (who needs this)
refab [id] [prefab] - change prefabid into new id
save - saves duh (closes console too)
attribute [id] [atr id] [str/int/flt] [value] - set an attribute value of a card
vecattribute [id] [atr id] [x/y/z] [value] - set an attribute to a vector value of a card
attributes [id] - get all attributes of a card
attributevalues [id] [atr id] - raw data of attribute of a card""")
    elif consoletext == "cardids":
       printCIDs()
    elif consoletext.split(" ")[0] == "rawcard":
        id = consoletext.split(" ")[1]
        print(data["LastPlayedRound"]["SavedCards"][int(id)])
    elif consoletext.split(" ")[0] == "foil":
        id = consoletext.split(" ")[1]
        data["LastPlayedRound"]["SavedCards"][int(id)]["IsFoil"] = True
    elif consoletext.split(" ")[0] == "defoil":
        id = consoletext.split(" ")[1]
        data["LastPlayedRound"]["SavedCards"][int(id)]["IsFoil"] = False
    elif consoletext.split(" ")[0] == "refab":
        id = consoletext.split(" ")[1]
        prefab = consoletext.split(" ")[2]
        data["LastPlayedRound"]["SavedCards"][int(id)]["CardPrefabId"] = prefab
    elif consoletext.split(" ")[0] == "save":
        wdata = open("save_0.sav", "w")
        wdata.truncate(0)
        wdata.writelines(json.dumps(data, indent=4))
        active = False
    elif consoletext == "close":
        active = False
    elif consoletext.split(" ")[0] == "attribute":
        id = consoletext.split(" ")[1]
        atrid = consoletext.split(" ")[2]
        if consoletext.split(" ")[3] == "str":
            data["LastPlayedRound"]["SavedCards"][int(id)]["ExtraCardData"][int(atrid)]["StringValue"] = consoletext.split(" ")[4]
        elif consoletext.split(" ")[3] == "int":
            data["LastPlayedRound"]["SavedCards"][int(id)]["ExtraCardData"][int(atrid)]["IntValue"] = int(consoletext.split(" ")[4])
        elif consoletext.split(" ")[3] == "flt":
            data["LastPlayedRound"]["SavedCards"][int(id)]["ExtraCardData"][int(atrid)]["FloatValue"] = float(consoletext.split(" ")[4])
    elif consoletext.split(" ")[0] == "vexattribute":
        id = consoletext.split(" ")[1]
        atrid = consoletext.split(" ")[2]
        data["LastPlayedRound"]["SavedCards"][int(id)]["ExtraCardData"][atrid]["VectorValue"][consoletext.split(" ")[3]] = float(consoletext.split(" ")[4])
    elif consoletext.split(" ")[0] == "attributes":
        id = consoletext.split(" ")[1]
        for i in range(len(data["LastPlayedRound"]["SavedCards"][int(id)]["ExtraCardData"])):
            print(i, ": ", data["LastPlayedRound"]["SavedCards"][int(id)]["ExtraCardData"][i]["AttributeId"])
    elif consoletext.split(" ")[0] == "attributevalues":
        id = consoletext.split(" ")[1]
        atrid = consoletext.split(" ")[2]
        print(data["LastPlayedRound"]["SavedCards"][int(id)]["ExtraCardData"][int(atrid)])
        
    
