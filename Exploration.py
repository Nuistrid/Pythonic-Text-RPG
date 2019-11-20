import Generators as gen
import Battle as btl
import Actions as act
import random as rnd
import collections as clts
import os,math

def ExploreRegion(player,region):
    os.system("cls")
    Exp = "You are currently in "+region["Name"]+" with "+str(region["Unexplored Regions"])+" explored out of "+str(region["Total Regions"])
    while 0 < region["Unexplored Regions"] <= region["Total Regions"]:
        print("1>  ")
        itp = input("(a)ssess,(e)xplore,(i)nspect,(h)eal,(m)ana,(p)ass,(q)uit>  ")
        Act = 0
        while itp not in list("aAeEhHiImMqQ"):
            player = act.ModifyPlayer(player)
            itp = input("(a)ssess,(e)xplore,(i)nspect,(h)eal,(m)ana,(p)ass,(q)uit>  ")
        if itp in ["q","Q"]:
            quit()
        elif itp in ["p","P"]:
            pass
        elif itp in ["a","A"]:
            act.SelfAssessment(player)
        elif itp in ["m","M"]:
            player = btl.RestoreMana(player)
        elif itp in ["h","H"]:
            player = btl.Heal(player)
        elif itp in ["i","I"]:
            os.system("cls")
            print(Exp)
            act.DisplayInventory(player)
            Inv = player["Inventory"]
            itp = input("now what? (s)ocket gems, (u)nsocket gems, (e)quip, u(n)quip, (b)ack>   ")
            if itp in ["b","B"]:
                pass
            elif itp in ["e","E","n","N"]:
                player = act.EquipItem(player)
                itp = 0
            elif itp in ["s","S"]:
                print("Socket what? (E)quips, (I)nventory")
                itp = input(">   ")
                if itp in ["e","E"]:
                    ky = ""
                    types = "(w/W)eapon 1, (w/W)eapon 2, (h/H)elm, (wr/Wr)ists,(f/F)eet, (ar/Ar)ms, (l/L)egs, (c/C)hest, (r/R)ing #(1-4) = (r/R)#, (i)nventory"
                    thing = clts.OrderedDict()
                    itp = input(types+">   ")
                    if itp in ["w1","W1"]:
                        ky = "Weapon 1"
                        thing = player[ky]
                    elif itp in ["w2","W2"]:
                        ky = "Weapon 2"
                        thing = player[ky]
                    elif itp in ["h","H"]:
                        ky = "Helm"
                        thing = player["Helm"]
                    elif itp in ["wr","Wr","WR"]:
                        ky = "Wrists"
                        thing = player["Wrists"]
                    elif itp in ["c","C"]:
                        ky = "Chest"
                        thing = player["Chest"]
                    elif itp in ["ar","Ar","AR"]:
                        ky = "Arms"
                        thing = player["Arms"]
                    elif itp in ["l","L","lg","Lg","LG"]:
                        ky = "Legs"
                        thing = player["Legs"]
                    elif itp in ["f","F"]:
                        ky = "Feet"
                        thing = player["Feet"]
                    elif itp in ["r1","R1"]:
                        ky = "Ring 1"
                        thing = player["Ring 1"]
                    elif itp in ["r2","R2"]:
                        ky = "Ring 2"
                        thing = player["Ring 2"]
                    elif itp in ["r3","r3"]:
                        ky = "Ring 3"
                        thing = player["Ring 3"]
                    elif itp in ["r4","R4"]:
                        ky = "Ring 4"
                        thing = player["Ring 4"]
                    print("what gem?")
                    InvGem = thing["Gems"]
                    itp = input("0-"+str(len(InvGem))+">   ")
                    while not 0 <= int(itp) < len(InvGem):
                        itp = input("0-"+str(len(InvGem))+">   ")
                    gem = thing["Gems"][int(itp)]
                    print("Proceed? (y/n)")
                    itp = input(">   ")
                    while itp not in ["y","Y"]:
                        itp = input(">   ")
                    player[ky] = act.SocketGem(thing,gem)
                    del gem,ky
                elif itp in ["i","I"]:
                    itp = input("0-"+str(len(Inv))+">   ")
                    while not 0 <= int(itp) < len(Inv):
                        itp = input("0-"+str(len(Inv))+">   ")
                    thing = Inv[int(itp)]
                    print("what gem?")
                    InvGem = list(filter(lambda x: x["Type"] == "Gem",Inv))
                    itp = input("0-"+str(len(InvGem))+">   ")
                    while not 0 <= int(itp) < len(InvGem):
                        itp = input("0-"+str(len(InvGem))+">   ")
                    gem = InvGem[int(itp)]
                    print("Proceed? (y/n)")
                    itp = input(">   ")
                    if itp in ["y","Y"]:
                        Thing = act.SocketGem(thing,gem)
                        Inv[Inv.index(thing)] = Thing
                    del InvGem
            elif itp in ["u","U"]:
                print("Unsocket from what? (e)quips, (i)nventory")
                itp = input(">   ")
                if itp in ["e","E"]:
                    ky = ""
                    thing = clts.OrderedDict()
                    itp = input(">   ")
                    if itp in ["w1","W1"]:
                        ky = "Weapon 1"
                        thing = player[ky]
                    elif itp in ["w2","W2"]:
                        ky = "Weapon 2"
                        thing = player[k]
                    elif itp in ["h","H"]:
                        ky = "Helm"
                        thing = player["Helm"]
                    elif itp in ["wr","Wr","WR"]:
                        ky = "Wrists"
                        thing = player["Wrists"]
                    elif itp in ["c","C"]:
                        ky = "Chest"
                        thing = player["Chest"]
                    elif itp in ["ar","Ar","AR"]:
                        ky = "Arms"
                        thing = player["Arms"]
                    elif itp in ["lg","Lg","LG"]:
                        ky = "Legs"
                        thing = player["Legs"]
                    elif itp in ["f","F"]:
                        ky = "Feet"
                        thing = player["Feet"]
                    elif itp in ["r1","R1"]:
                        ky = "Ring 1"
                        thing = player["Ring 1"]
                    elif itp in ["r2","R2"]:
                        ky = "Ring 2"
                        thing = player["Ring 2"]
                    elif itp in ["r3","r3"]:
                        ky = "Ring 3"
                        thing = player["Ring 3"]
                    elif itp in ["r4","R4"]:
                        ky = "Ring 4"
                        thing = player["Ring 4"]
                    print("what gem?")
                    InvGem = thing["Gems"]
                    itp = input("0-"+str(len(InvGem))+">   ")
                    while 0 <= int(itp) < len(InvGem):
                        itp = input("0-"+str(len(InvGem))+">   ")
                    gem = thing["Gems"][int(itp)]
                    print("Proceed? (y/n)")
                    itp = input(">   ")
                    while itp not in ["y","Y"]:
                        itp = input(">   ")
                    player[ky] = act.UnsocketGem(thing,gem)
                    del gem,ky
                elif itp in ["i","I"]:
                    itp = input("0-"+str(len(Inv))+">   ")
                    while 0 <= int(itp) < len(Inv):
                        itp = input("0-"+str(len(Inv))+">   ")
                    thing = Inv[int(itp)]
                    print("what gem?")
                    InvGem = thing[""]
                    itp = input("0-"+str(len(InvGem))+">   ")
                    while 0 <= int(itp) < len(InvGem):
                        itp = input("0-"+str(len(InvGem))+">   ")
                    gem = InvGem[int(itp)]
                    print("Proceed? (y/n)")
                    itp = input(">   ")
                    if itp in ["y","Y"]:
                        Thing = act.UnsocketGem(thing,gem)
                        Inv[Inv.index(thing)] = Thing
                    del InvGem
        if itp in ["e","E"]:
            Act = rnd.choices([1,2,3],[.6,.2,.2],k=1)[0]
        if Act == 1:
            creature = gen.GenerateCreature(int(round(math.ceil(player["Level"]*rnd.choices([0.05,.3,.5,.7],[.15,.35,.15,.35],k=1)[0]+region["Rank"]))))
            Creature = gen.ModifyObject(creature,region)
            btl.Battle(player,Creature,region)
            player["Current HP"] = player["Maximum HP"]
            print("You found loot!")
            Lt = gen.GenerateLoot(player,rnd.randint(1,12),rnd.choice([.3,.5,.7,1]))
            for k in Lt:
                print(str(Lt.index(k))+": "+str(k["Name"]))
            print("pick up what? Pressing a key outside range quits looting: 0-"+str(len(Lt)-1))
            R = len(Lt)
            itp = input(">   ")
            while int(itp) in range(R) and R > 0:
                os.system("cls")
                for k in Lt:
                    print(str(Lt.index(k))+": "+str(k["Name"]))
                print("pick up what? Pressing a key outside range quits looting: 0-"+str(len(Lt)-1))
                itp = input(">   ")
                if int(itp) > R-1 or int(itp) < 0:
                    break
                player["Inventory"].append(Lt[int(itp)])
                del Lt[int(itp)]
                R = len(Lt)
            region["Unexplored Regions"] -= 1
            os.system("cls")
        elif Act == 2:
            print("You found loot!")
            Lt = gen.GenerateLoot(player,rnd.randint(1,12),rnd.choice([.3,.5,.7,1]))
            for k in Lt:
                print(str(Lt.index(k))+": "+str(k["Name"]))
            print("pick up what? Pressing a key outside range quits looting: 0-"+str(len(Lt)-1))
            R = len(Lt)
            itp = input(">   ")
            while int(itp) in range(R) and R > 0:
                os.system("cls")
                for k in Lt:
                    print(str(Lt.index(k))+": "+str(k["Name"]))
                print("pick up what? Pressing a key outside range quits looting: 0-"+str(len(Lt)-1))
                itp = input(">   ")
                if int(itp) > R-1 or int(itp) < 0:
                    break
                player["Inventory"].append(Lt[int(itp)])
                del Lt[int(itp)]
                R = len(Lt)
            region["Unexplored Regions"] -= 1
            os.system("cls")
        elif Act == 3:
            Grd = 1+int(rnd.uniform(0,2)*region["Rank"])
            print(Exp)
            print("You Stumbled upon a guarded area protected by "+str(Grd)+" Monsters! Proceed? (Y/N)?")
            itp = input(">   ")
            while itp not in ["n","N","y","Y"]:
                os.system("cls")
                print(Exp)
                print("You Stumbled upon a guarded area protected by "+str(Grd)+" Monsters! Proceed? (Y/N)?")
                itp = input(">   ")
            if itp in ["n","N"]:
                pass
            elif itp in ["y","Y"]:
                enemy = Grd
                while 0 < enemy <= Grd:
                    os.system('cls')
                    creature = gen.GenerateCreature(rnd.choices([round(player["Level"]*i+region["Rank"],1) for i in [.3,.5,.8,1,1.5,2]],[.13,.11,.26,.42,.03,.02],k=1)[0])
                    Creature = gen.ModifyObject(creature,region)
                    btl.Battle(player,Creature,region,dungeon=True,left=enemy,total=Grd)
                    player["Current HP"] = player["Maximum HP"]
                    enemy -= 1
                print("You won! Here's your prizes!")
                Lt = gen.GenerateLoot(player,rnd.choice([10,15]),rnd.choice([.9,1,1.1,1.2,1.25]))
                for k in Lt:
                    print(str(Lt.index(k))+": "+str(k["Name"]))
                print("pick up what? Pressing a key outside range quits looting: 0-"+str(len(Lt)-1))
                itp = input(">   ")
                R = len(Lt)
                while itp in list(range(R)) and R > 0:
                    for k in Lt:
                        print(str(Lt.index(k))+": "+str(k["Name"]))
                    print("pick up what? Pressing a key outside range quits looting: 0-"+str(R-1))
                    itp = input(">   ")
                    if int(itp) > R-1 or int(itp) < 0:
                        break
                    player["Inventory"].append(Lt[int(itp)])
                    del Lt[int(itp)]
                    R = len(Lt)
                region["Unexplored Regions"] -= 1
