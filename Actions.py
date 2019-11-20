import random as rnd
import collections as clts
import os

def SocketGem(thing,gem):
    NewThing = thing
    if NewThing["Sockets"] > 0:
        NewThing = ModifyObject(thing,gem)
        NewThing["Gems"].append(gem)
        NewThing["Sockets"] -= 1
    return NewThing

def UnsocketGem(thing,gem):
    NewThing = UnModifyObject(thing,gem)
    del NewThing["Gems"][NewThing["Gems"].index(gem)]
    NewThing["Sockets"] += 1
    return NewThing

def LevelUp(player):
    os.system('cls')
    itp = ""
    while player["Skill Points"] > 0:
        os.system('cls')
        print("Congrats! You are know Level "+str(player["Level"])+"!")
        print("Skill Points Remaining: "+str(player["Skill Points"]))
        for ky in ["Strength","Constitution","Intelligence","Dexterity","Luck"]:
            print(ky+": "+str(player[ky]))
        itp = int(input("Place points where? input 0 to 4>   "))
        if itp == 0:
            player["Strength"] += 1
            player["Defense"] += 5
            player["Physical Resistance"] += .0205
            player["Skill Points"] -= 1
        elif itp == 1:
            player["Constitution"] += 1
            player["Maximum HP"] += 10
            player["Current HP"] += 10
            player["Defense"] += 3.25
            player["Skill Points"] -= 1
        elif itp == 2:
            player["Intelligence"] += 1
            player["Maximum MP"] += 10
            player["Current MP"] += 10
            player["Skill Points"] -= 1
        elif itp == 3:
            player["Dexterity"] += 1
            player["Critical Rate"] += .005
            player["Hit Rate"] += .005
            player["Skill Points"] -= 1
        elif itp == 4:
            player["Luck"] += 1
            player["Critical Multiplier"] += 0.005
            player["Skill Points"] -= 1

    return player

def DisplayEquipment(player,typ):
    os.system("cls")
    for ky in ["Helm","Chest","Arms","Legs","Wrists","Feet","Weapon 1","Weapon 2"]+["Ring "+str(i+1) for i in range(3)]:
        for ar in player[ky]:
            if ar != None:
                print(ar["Name"])
            else:
                print("Nothing!")

def ModifyPlayer(player):

    for ky in ["Helm","Chest","Arms","Legs","Wrists","Feet","Weapon 1","Weapon 2"]+["Ring "+str(i+1) for i in range(3)]:
        for R in ["Fire Resistance","Ice Resistance","Earth Resistance","Lightning Resistance","Physical Resistance","Defense"]:
            if player[ky] != None and R in player[ky].keys():
                player[R] += player[ky][R]

    return player

def EquipItem(player):
    os.system("cls")
    ky = ""
    DisplayInventory(player)
    NewThing = clts.OrderedDict()
    itp = input("Equip what? 0-"+str(len(player["Inventory"])-1)+">  ")
    while not 0 <= int(itp) <= len(player["Inventory"])-1:
        os.system("cls")
        DisplayInventory(player)
        itp = input("Equip what? 0-"+str(len(player["Inventory"])-1)+">  ")
    J = int(itp)
    itp = input("What? (w/W)eapon #1-2, (h/H)elm, (c/C)hest, (wr/Wr)ists, (f/F)eet, (Ar/ar)ms, (l/L)egs, (r/R)ing #1-4>   ")
    if itp in ["w1","W1"]:
        ky = "Weapon 1"
    elif itp in ["w2","W2"]:
        ky = "Weapon 2"
    elif itp in ["h","H"]:
        ky = "Helm"
    elif itp in ["wr","Wr","WR"]:
        ky = "Wrists"
    elif itp in ["c","C"]:
        ky = "Chest"
    elif itp in ["ar","Ar","AR"]:
        ky = "Arms"
    elif itp in ["l","L","lg","Lg","LG"]:
        ky = "Legs"
    elif itp in ["f","F"]:
        ky = "Feet"
    elif itp in ["r1","R1"]:
        ky = "Ring 1"
    elif itp in ["r2","R2"]:
        ky = "Ring 2"
    elif itp in ["r3","r3"]:
        ky = "Ring 3"
    elif itp in ["r4","R4"]:
        ky = "Ring 4"

    player[ky], player["Inventory"][J] = player["Inventory"][J], player[ky]

    return player

def DisplayInventory(player):
    Inventory = player["Inventory"]
    for obj in Inventory:
        if obj != None:
            print(str(Inventory.index(obj))+":  "+str(obj["Name"]))
        else:
            print(str(Inventory.index(obj))+":   Nothing!")

def InspectInventory(player):
    os.system('cls')
    DisplayInventory(player)
    Inventory = player["Inventory"]
    itp = input("Select Item 0"+"-"+str(len(Inventory)-1)+":   ")
    while not (0 <= int(itp) < len(Inventory)):
        os.system('cls')
        DisplayInventory(player)
        itp = input("Select Item 0"+"-"+str(len(Inventory)-1)+":   ")
    obj = Inventory[itp]
    for v in obj:
        S = K[v]
        if type(S) == list:
            S = "min: "+str(K[v][0])+" / max: "+str(K[v][1])
            if S[0] == S[1]:
                S = str(K[v][0])
        print(str(K)+":  "+str(S))

def Heal(player):
    HealthRestore = 0
    CurrHealth = player["Current HP"]
    MaxHP = player["Maximum HP"]
    Inventory = player["Inventory"]
    DisplayInventory(player)
    itp = input("Select Item 0"+"-"+str(len(Inventory)-1)+":   ")
    while not ("HP Flask" in Inventory[itp]["Name"] and 0 <= int(itp) < len(Inventory)):
        CurrHealth = player["Current HP"]
        MaxHP = player["Maximum HP"]
        Inventory = player["Inventory"]
        DisplayInventory(player)
        itp = input("Select Item 0"+"-"+str(len(Inventory)-1)+":   ")
    if "HP Flask" in Inventory[itp]["Name"] and 0 <= int(itp) < len(Inventory):
        HealthRestore = Inventory[itp]["Heal Value"]
        note = ""
        if Inventory[itp]["Current Charges"] <= 0:
            HealthRestore = 0
            note = "It failed! Not charges left"
        if CurrHealth > MaxHP:
            HealthRestore += CurrHealth - MaxHP
    Msg = "You Healed "+str(HealthRestore)+" Health! "+str(CurrHealth)+" / "+str(MaxHP)+"HP"+note 
    return Msg

def RestoreMana(player):
    ManaRestore = 0
    CurrMana = player["Current MP"]
    MaxMP = player["Maximum MP"]
    Inventory = player["Inventory"]
    DisplayInventory(player)
    itp = input("Select Item 0"+"-"+str(len(Inventory))+":   ")
    while not ("MP Flask" in Inventory[itp]["Name"] and 0 <= int(itp) < len(Inventory)):
        CurrMana = player["Current MP"]
        MaxMP = player["Maximum MP"]
        Inventory = player["Inventory"]
        for i in Inventory:
            print(Inventory.index(i)+": "+str(i))
        itp = input("Select Item 0"+"-"+str(len(Inventory))+":   ")
    if "MP Flask" in Inventory[itp]["Name"] and 0 <= int(itp) < len(Inventory):
        ManaRestore = Inventory[itp]["Restore Value"]
        note = ""
        if Inventory[itp]["Current Charges"] <= 0:
            ManaRestore = 0
            note = "It failed! Not charges left"
        if CurrMana > MaxMP:
            ManaRestore += CurrMana - MaxMP
    Msg = "You Restored "+str(ManaRestore)+" CurrMana! "+str(CurrMana)+" / "+str(MaxMP)+"MP"+note
    return Msg

def SelfAssessment(player):
    os.system('cls')
    print("Name: "+player["Name"])
    print("Health: "+str(player["Current HP"])+" / "+str(player["Maximum HP"]))
    print("Mana: "+str(player["Current MP"])+" / "+str(player["Maximum MP"]))
    print("Defense: "+str(player["Defense"]))
    print("Luck: "+str(player["Luck"]))
    print("Strength: "+str(player["Strength"]))
    print("Constitution: "+str(player["Constitution"]))
    print("Intelligence: "+str(player["Intelligence"]))
    print("Dexterity: "+str(player["Dexterity"]))
    print("Luck: "+str(player["Luck"]))
    print("Hit Rate "+str(player["Hit Rate"]))
    print("Critical x "+str(player["Critical Multiplier"]))
    print("Critical % "+str(player["Critical Rate"]))
    print("Physical Resistance: "+str(10**4*(player["Physical Resistance"])))
    print("Fire Resistance: "+str(10**4*(player["Fire Resistance"])))
    print("Ice Resistance: "+str(10**4*(player["Ice Resistance"])))
    print("Geo Resistance: "+str(10**4*(player["Earth Resistance"])))
    print("Lightning Resistance: "+str(10**4*(player["Lightning Resistance"])))
    for ky in ["Weapon 1","Weapon 2","Helm","Arms","Chest","Wrists","Feet","Ring 1","Ring 2","Ring 3","Ring 4"]:
        Nm = "Nothing!"
        if player[ky] != None:
            Nm = player[ky]["Name"]
        print(ky+": "+Nm)
    itp = input("(q)uit>   ")
    while itp not in ["q","Q"]:
        itp = input("(q)uit>   ")
