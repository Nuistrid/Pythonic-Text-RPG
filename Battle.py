import random as rnd
import Generators as gen
import Actions as act
import os,time,math

def ModifyWeapon(weapon,modifA=[1,1,1,1,1],modifB=[1,1,1,1,1],extraA=[0,0,0,0,0],extraB=[0,0,0,0,0]):

    S = [i+" Damage" for i in ["Physical","Fire","Ice","Earth","Lightning"]]

    for k,j in S:
        weapon[k][0] = [weapon[k][0]*modifA[S.index(k)]+extraA[S.index(k)]]
        weapon[k][1] = [weapon[k][1]*modifB[S.index(k)]+extraB[S.index(k)]]
    
    return weapon

def AttackEnemy(weapon,enemy):
    multiplier = 1
    EnmyName = enemy["Name"]
    WpName = weapon["Name"]
    phys,fire,ice,earth,lght = 0,0,0,0,0
    if rnd.uniform(0,1) < weapon["Hit Rate"]:
        multiplier += sum(weapon["Physical Damage"])
    if rnd.uniform(0,1) < weapon["Critical Rate"]:
        multiplier += weapon["Critical Multiplier"]
    phys =  round(multiplier*(1-enemy["Physical Resistance"])*rnd.uniform(weapon["Physical Damage"][0],weapon["Physical Damage"][1]+1)-.5*enemy["Defense"],3)
    if phys < 0:
        phys = round(0,3)
    fire =  round(multiplier*(1-enemy["Fire Resistance"])*rnd.uniform(weapon["Fire Damage"][0],weapon["Fire Damage"][1]+5)-.3*enemy["Defense"],3)
    if fire < 0:
        fire = round(0,3)       
    ice =  round(multiplier*(1-enemy["Ice Resistance"])*rnd.uniform(weapon["Ice Damage"][0],weapon["Ice Damage"][1]+5)-.3*enemy["Defense"],3)
    if ice < 0:
        ice = round(0,3)        
    earth =  round(multiplier*(1-enemy["Earth Resistance"])*rnd.uniform(weapon["Earth Damage"][0],weapon["Earth Damage"][1]+5)-.4*enemy["Defense"],3)
    if earth < 0:
        earth = round(0,3)        
    lght = round(multiplier*(1-enemy["Lightning Resistance"])*rnd.uniform(weapon["Lightning Damage"][0],weapon["Lightning Damage"][1]+5)-.8*enemy["Defense"],3)
    if lght < 0:
        lght = round(0,3)
    dmg = round(phys+fire+ice+earth+lght,3)
    Dmg = "You did "+str(phys)+" Damage (+"+str(fire)+" Fire +"+str(ice)+" Ice +"+str(earth)+" Earth) +"+str(lght)+" Lightning) to (the) "+EnmyName+" with your "+WpName+"\""
    if dmg == 0:
        Dmg = "(The) "+EnmyName+" dodged your Attack!"
    return [dmg,Dmg]

def AttackPlayer(player,enemy):
    multiplier = 1
    phys,fire,ice,earth,lght = 0,0,0,0,0
    if rnd.uniform(0,1) < enemy["Hit Rate"]:
        multiplier += .05*enemy["Physical Damage"][0]
    if rnd.uniform(0,1) < enemy["Critical Rate"]:
        multiplier += enemy["Critical Multiplier"]
        phys =  round(multiplier*(1-player["Physical Resistance"])*rnd.uniform(enemy["Physical Damage"][0],enemy["Physical Damage"][1]+5)-player["Defense"],3)
    if phys < 0:
        phys = round(0,3)
    fire =  round(multiplier*(1-player["Fire Resistance"])*rnd.uniform(enemy["Fire Damage"][0],enemy["Fire Damage"][1]+5)-.3*player["Defense"],3)
    if fire < 0:
        fire = round(0,3)
    ice =  round(multiplier*(1-player["Ice Resistance"])*rnd.uniform(enemy["Ice Damage"][0],enemy["Ice Damage"][1]+5)-.3*player["Defense"],3) 
    if ice < 0:
        ice = round(0,3)
    earth =  round(multiplier*(1-player["Earth Resistance"])*rnd.uniform(enemy["Earth Damage"][0],enemy["Earth Damage"][1]+5)-.8*player["Defense"],3)
    if earth < 0:
        earth = round(0,3)        
    lght = round(multiplier*(1-player["Lightning Resistance"])*rnd.uniform(enemy["Lightning Damage"][0],enemy["Lightning Damage"][1]+5)-.4*player["Defense"],3)
    if lght < 0:
        lght = round(0,3)
    dmg = round(phys+fire+ice+earth+lght,3)
    Dmg = "You Dodged the Attack!"
    if dmg > 0:
        Dmg = "(The) "+enemy["Name"]+" did "+str(phys)+" Damage (+"+str(fire)+" Fire +"+str(ice)+" Ice +"+str(earth)+" Earth) +"+str(lght)+" Lightning) to "+player["Name"]+"\""
    return [dmg,Dmg]

def Battle(player, enemy, region, dungeon=False, left=0, total=1):
    itp = ""
    N = ""
    if dungeon and left > 0:
        N = "Enemies left: "+str(left)+" / "+str(total)+"\n"
    Exp=lambda P,R,E,t=N: "Map : "+R["Name"]+" explored: "+str(R["Unexplored Regions"])+" / "+str(R["Total Regions"])+"\n"+str(P["Current HP"])+" / "+str(P["Maximum HP"])+" HP: "+P["Name"]+"\n"+str(E["Current HP"])+" / "+str(E["Maximum HP"])+" HP: "+E["Name"]+"\n"+t+"Action? 1> Basic Attack  2> Double Strike 3>  Heal 4> Mana Restore 5> Inspect Inventory"
    while player["Current HP"] > 0 and enemy["Current HP"] > 0:
        os.system("cls")
        print(Exp(P=player,R=region,E=enemy))
        itp = input(">   ")
        if itp == "1":
            damageEny = AttackEnemy(player["Weapon 1"],enemy)
            print(damageEny[1])
            enemy["Current HP"] -= damageEny[0]
            print("(The) "+enemy["Name"]+" lost "+str(damageEny[0])+" Health! "+str(enemy["Current HP"])+" / "+str(enemy["Maximum HP"])+" HP left!")
            damagePly = AttackPlayer(player,enemy)
            print(damagePly[1])
            player["Current HP"] -= damagePly[0]
            print("\""+player["Name"]+" lost "+str(damagePly[0])+" Health! "+str(player["Current HP"])+" / "+str(player["Maximum HP"])+" HP left!")
        if itp == "2" and player["Weapon 2"] == None:
            print("No Second Weapon!")
        if itp == "2" and player["Weapon 2"] != None and player["Current MP"] > 0:
            Mhalf = [.5 for i in range(5)]
            player["Weapon 1"] = ModifyWeapon(player["Weapon 1"],modif=Mhalf,modifB=Mhalf)
            player["Weapon 2"] = ModifyWeapon(player["Weapon 2"],modif=Mhalf,modifB=Mhalf) 
            damageEny1 = AttackEnemy(player["Weapon 1"],enemy)
            damageEny2 = AttackEnemy(player["Weapon 2"],enemy)
            MTwo = [2 for i in range(5)]
            player["Weapon 1"] = ModifyWeapon(player["Weapon 1"],modif=MTwo,modifB=MTwo)
            player["Weapon 2"] = ModifyWeapon(player["Weapon 2"],modif=MTwo,modifB=MTwo) 
            player["Current MP"] -= 10
            print(damageEny1[1])
            print(damageEny2[1])
            enemy["Current HP"] -= damageEny1[0]+damageEny2[0]
            print("(The) "+enemy["Name"]+" lost "+str(damageEny1[0]+damageEny2[0])+" Health! "+str(enemy["Current HP"])+" / "+str(enemy["Maximum HP"])+" HP left!")
            damagePly = AttackPlayer(player,enemy)
            print(damagePly[1])
            player["Current HP"] -= damagePly[0]
            print("\""+player["Name"]+" lost "+str(damagePly[0])+" Health! "+str(player["Current HP"])+" / "+str(player["Maximum HP"])+" HP left!")
        if itp == "3":
            act.Heal(player)
        if itp == "4":
            act.RestoreMana(player)
        if itp == "5":
            act.InspectInventory(player)
    if player["Current HP"] < 0:
        print("You Lost!")
    if enemy["Current HP"] < 0:
        os.system("cls")
        print("You Win! ")
        player["Experience"] += 10*rnd.triangular(1,1.3,1.02)*player["Level"]**.2
        if player["Experience"] > 3.3*player["Level"]**1.5:
            player["Experience"] = 3.3*player["Level"]**1.5
            player["Level"] += 1
            player["Skill Points"] += 5
            player = act.LevelUp(player)
        player["Gold"] += 8*rnd.triangular(1,1.3,1.02)*player["Level"]**.1
        os.system("cls")
        del enemy
    return 0

