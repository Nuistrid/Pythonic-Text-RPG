import Actions as act
import Exploration as expr
import random as rnd
import Generators as gen
import Battle as btl
import collections as clts
import os

def NewGame():
    name = input("What is you name? >  ")
    Sword = gen.GenerateWeapon(1)
    Player = clts.OrderedDict()
    Player["Name"] = name
    Player["Current HP"] = 10
    Player["Maximum HP"] = 10
    Player["Current MP"] = 10
    Player["Maximum MP"] = 10
    Player["Level"] = 1
    Player["Experience"] = 1
    Player["Gold"] = 0
    Player["Skill Points"] = 0
    Player["Strength"] = 1
    Player["Constitution"] = 1
    Player["Intelligence"] = 1
    Player["Dexterity"] = 1
    Player["Luck"] = 1
    Player["Hit Rate"] = Sword["Hit Rate"]
    Player["Critical Rate"] = Sword["Critical Rate"]
    Player["Critical Multiplier"] = Sword["Critical Multiplier"]
    Player["Defense"] = 1
    Player["Weapon 1"] = Sword
    Player["Weapon 2"] = None
    Player["Helm"] = None
    Player["Arms"] = None
    Player["Chest"] = None
    Player["Wrists"] = None
    Player["Legs"] = None
    Player["Feet"] = None
    Player["Ring 1"] = None
    Player["Ring 2"] = None
    Player["Ring 3"] = None
    Player["Ring 4"] = None
    Player["Current Location"] = None
    for i in [j+" Resistance" for j in ["Physical","Fire","Ice","Earth","Lightning"]]:
        Player[i] = 0
    Player["Inventory"] = []

    return Player

def Game():
    os.system("cls")
    print("Welcome to A Text Based RPG")
    print("Developed by Malachi Wadas \n\n\n\n")
    itp = input("(n)ew / (l)oad game? >   ")
    if itp in ["n","N"]:
        Player = NewGame()
        Easyregions = [gen.GenerateRegion(rnd.choice([1,2,3]),themes=rnd.choice(["fire","ice","earth","lightning","random","special",""]))]*200
        Medregions = [gen.GenerateRegion(rnd.choice([4,5]),themes=rnd.choices(["fire","ice","earth","lightning","random","special",""],k=2))]*100
        Hardregions = [gen.GenerateRegion(rnd.choice([6,7]),themes=rnd.choices(["fire","ice","earth","lightning","random","special",""],k=2))]*25
        Reg = rnd.sample(Easyregions+Medregions+Hardregions,5)

        for i in range(len(Reg)):
            print(str(i)+":  "+Reg[i]["Name"]+", Regions: "+str(Reg[i]["Total Regions"]))
        itp = int(input("Which one do you wnat to explore? 0 - "+str(len(Reg)-1)+" >  "))
        while not (0 <= itp <= len(Reg)-1):
            for i in range(len(Reg)):
                print(str(i)+":  "+Reg[i]["Name"]+", Regions: "+str(Reg[i]["Total Regions"]))
            itp = int(input("Which one do you wnat to explore? 0 - "+str(len(Reg)-1)+" >  "))
        reg = Reg[itp]
        Player["Current Location"] = reg
        expr.ExploreRegion(Player,reg)
    if itp in ["l","L"]:
        quit()

Game()
