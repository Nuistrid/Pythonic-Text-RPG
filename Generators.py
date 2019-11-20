import random as rnd
import collections as clts
import math

def Standardize(obj,ln):
    Obj = obj
    if type(obj) == str:
        Obj = obj
    if type(obj) in [float,int]:
        Obj = round(obj,ln)
    elif type(obj) == list:
        Lst = []
        for k in Obj:
            R = k
            if type(k) in [str,dict,clts.OrderedDict]:
                pass
            else:
                R = round(k,ln)
            Lst.append(R)
        Obj = Lst

    return Obj

def ModifyObject(objX,objY):
    NewObj = clts.OrderedDict()
    S = [k for k in [i in objX.keys() and i in objY.keys() and i or "None" for i in objX.keys()] if k != "None"]
    for ky in S:
        if type(objX[ky]) == str:
            NewObj[ky] = objX[ky]
        elif type(objX[ky]) in [float,int]:
            NewObj[ky] = objX[ky]+objY[ky]
        elif type(objX[ky]) == list:
            NewObj[ky] = [objX[ky][i]+objY[ky][i] for i in range(len(objX[ky]))]
    for obj in NewObj.keys():
        NewObj[obj] = Standardize(NewObj[obj],3)
    return NewObj

def UnModifyObject(objX,objY):
    NewObj = clts.OrderedDict()
    S = [k for k in [i in objX.keys() and i in objY.keys() and i or "None" for i in objX.keys()] if k != "None"]
    for ky in S:
        if type(objX[ky]) == str:
            NewObj[ky] = objX[ky]
        elif type(objX[ky]) in [float,int]:
            NewObj[ky] = objX[ky]-objY[ky]
        elif type(objX[ky]) == list:
            NewObj[ky] = [objX[ky][i]-objY[ky][i] for i in range(len(objX[ky]))]
    for obj in NewObj.keys():
        NewObj[obj] = Standardize(NewObj[obj],3)
    return NewObj

def GenerateGem(level,themes):
    cnt = rnd.choice([i*.1 for i in range(1,7)])
    point = math.ceil(rnd.triangular(1,level*1.25,level*.05)*.1)
    colors = ["Red","Orange","Yellow","Green","Blue","Cyan","Teal","Violet","Purple","Indigo","Grey","Ivory"]
    colorAdj = ["Dark","Light","Shimmering","Glowing","Shining","Basic","Fancy","Artistic","Random","Stochasticly","Erraticly"]
    nameAdj1 = ["Dangerous","Strange","Exotic","Rusted","Collapsing","Rustic"]
    EarthAdj = ["Damp","Muddy","Windy","Weathery"]
    FireAdj = ["Blazing","Burning","Firey","Flame","Flaming"]
    IceAdj = ["Damp","Watery","Submerged","Icy","Freezing","Freeze","Frozen","Blizzard"]
    LghtAdj = ["Shocking","Stroming","Electrifying","Winding","Blinding"]
    SpclAdj = ["Elemental","Chormatic","Plane","Ultra Void","Galactic",str(point)+"-dimensional Void"]
    if "earth" in themes:
        nameAdj1 += EarthAdj
    if "fire" in themes:
        nameAdj1 += FireAdj
    if "ice" in themes:
        nameAdj1 += IceAdj
    if "lightning" in themes:
        nameAdj1 += LghtAdj
    if "special" in themes:
        nameAdj1 += SpclAdj
    if "random" in themes:
        nameAdj1 += EarthAdj+FireAdj+IceAdj+LghtAdj+SpclAdj
    AdjA = [rnd.choice(nameAdj1),rnd.choice(nameAdj1)]
    K = AdjA[0]+" and "+AdjA[1]
    if AdjA[0]==AdjA[1]:
        K = "Very "+AdjA[0]
    name = "(+"+str(point)+") "+K+" "+rnd.choice(["gem","token","trinket","festoon","jewel"])
    HP = point*rnd.triangular(0,1.8,.3)
    maxP = point*rnd.triangular(0,2.5,.6)
    minP = point*rnd.triangular(0,2.5,.6)
    phys = [minP,maxP]; phys.sort()
    Gem = clts.OrderedDict([("Name", name),("Rank", level),("Current HP", HP),("Maximum HP", HP),("Physical Damage", phys),("Fire Damage", [0,0]),("Ice Damage", [0,0]),("Earth Damage", [0,0]),("Lightning Damage", [0,0]),("Defense", 0),("Fire Resistance", 0),("Ice Resistance", 0),("Earth Resistance",0),("Lightning Resistance", 0),("Physical Resistance",0),("Themes",themes),("Type","Gem")])
    Gem["Defense"] = round(abs(rnd.triangular(1,(point+1)*(cnt+.5+1),(point+1)*(cnt*.2+1))),3)
    Gem["Hit Rate"] = rnd.uniform(0,.35)
    Gem["Critical Rate"] = rnd.uniform(0,.35)
    Gem["Physical Resistance"] = rnd.triangular(0,1,cnt)*cnt
    if True in [bool(k in name) for k in IceAdj]:
        Gem["Ice Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Gem["Ice Damage"].sort()
        Gem["Ice Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in FireAdj]:
        Gem["Fire Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Gem["Fire Damage"].sort()
        Gem["Fire Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in EarthAdj]:
        Gem["Earth Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Gem["Earth Damage"].sort()
        Gem["Earth Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in LghtAdj]:
        Gem["Lightning Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Gem["Lightning Damage"].sort()
        Gem["Lightning Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in SpclAdj]:
        Gem["Fire Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Gem["Fire Damage"].sort()
        Gem["Ice Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Gem["Ice Damage"].sort()
        Gem["Earth Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Gem["Earth Damage"].sort()
        Gem["Physical Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75+point*.9,point*.2)]
        Gem["Physical Damage"].sort()
        Gem["Lightning Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Gem["Lightning Damage"].sort()
        Gem["Physical Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
        Gem["Fire Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
        Gem["Earth Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
        Gem["Lightning Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
        Gem["Ice Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt

    if Gem["Critical Rate"] > 1:
        Gem["Critical Rate"] = .95

    if Gem["Hit Rate"] > 1:
        Gem["Hit Rate"] = .95

    if Gem["Fire Resistance"] > 1:
        Gem["Fire Resistance"] = .95

    if Gem["Ice Resistance"] > 1:
        Gem["Ice Resistance"] = .95

    if Gem["Earth Resistance"] > 1:
        Gem["Earth Resistance"] = .95

    if Gem["Physical Resistance"] > 1:
        Gem["Physical Resistance"] = .95

    if Gem["Lightning Resistance"] > 1:
        Gem["Lightning Resistance"] = .95

    for J in Gem.keys():
        Gem[J] = Standardize(Gem[J],3)

    return Gem

def GenerateRegion(level,themes=[]):
    cnt = rnd.choices([.1,.2,.3,.4,.5,.6,.7,.8,.9],[.3,.3,.15,.1,.05,.05,.02,.02,.01],k=1)[0]
    point = math.ceil(round(rnd.triangular(1,level*1.25,level*cnt)))
    colors = ["Red","Orange","Yellow","Green","Blue","Cyan","Teal","Violet","Purple","Indigo","Grey","Ivory"]
    colorAdj = ["Dark","Light","Shimmering","Glowing","Shining","Basic","Fancy","Artistic","Random","Stochasticly","Erraticly"]
    nameAdj1 = ["Dangerous","Strange","Exotic","Rusted","Collapsing","Rustic"]
    EarthAdj = ["Damp","Muddy","Windy","Weathery"]
    EarthNouns = ["Cavern","Cave","Catacombs","Desert","Savanna"]
    FireAdj = ["Blazing","Burning","Firey","Flame","Flaming"]
    FireNouns = ["Desert","Inferno","Hellscape","Savanna"]
    IceAdj = ["Damp","Watery","Submerged","Icy","Freezing","Freeze","Frozen","Blizzard"]
    IceNouns = ["Glacier","Frostscape","Icescape","Tundra","Winter Wonderland","Rainstorm","Storm","Flooded Town"]
    LghtAdj = ["Shocking","Stroming","Electrifying","Winding","Blinding"]
    LghtNouns = ["Storm","Flooded Town","Electric Avenue","Factory"]
    SpclAdj = ["Elemental","Chormatic","Plane","Ultra Void","Galactic",str(point)+"-dimensional Void"]
    SpclNouns = ["Rubyspire","Jadespire","Sapphirespire"]+[k+"spire" for k in ["Gold","Silver","Metal","Bronze","Copper","Tin","Diamond"]]
    Nouns = ["Plains","Spire","Tower"]
    nameComm = ["Mythical","Legendary","Super Rare","Rare","Uncommon","Common"]
    if "earth" in themes:
        nameAdj1 += EarthAdj
        Nouns += EarthNouns
    if "fire" in themes:
        nameAdj1 += FireAdj
        Nouns += FireNouns
    if "ice" in themes:
        nameAdj1 += IceAdj
        Nouns += IceNouns
    if "lightning" in themes:
        nameAdj1 += LghtAdj
        Nouns += LghtNouns
    if "special" in themes:
        nameAdj1 += SpclAdj
        Nouns += SpclNouns
    if "random" in themes:
        nameAdj1 += EarthAdj+FireAdj+IceAdj+LghtAdj+SpclAdj
        Nouns += EarthNouns+FireNouns+IceNouns+LghtNouns+SpclNouns
    AdjA = [rnd.choice(nameAdj1),rnd.choice(nameAdj1)]
    K = AdjA[0]+" and "+AdjA[1]
    if AdjA[0]==AdjA[1]:
        K = "Very "+AdjA[0]
    name = "Tier "+str(level)+" "+rnd.choices(nameComm,[.01,.02,.02,.15,.3,.5],k=1)[0]+" "+K+" "+rnd.choice(Nouns)+" map"
    HP = point*rnd.triangular(0,1.8,.3+cnt)
    maxP = point*rnd.triangular(0,2.5,.6+cnt)
    minP = point*rnd.triangular(0,2.5,.6+cnt)
    phys = [minP,maxP]; phys.sort()
    Reg = int(10+rnd.randint(1,101)*rnd.triangular(0,1,.3))
    Region = clts.OrderedDict([("Name", name),("Rank", level),("Unexplored Regions", Reg),("Total Regions", Reg),("Current HP", HP),("Maximum HP", HP),("Hit Rate", 0),("Critical Rate", 0),("Critical Multiplier", 1),("Physical Damage", phys),("Fire Damage", [0,0]),("Ice Damage", [0,0]),("Earth Damage", [0,0]),("Lightning Damage", [0,0]),("Defense", 0),("Fire Resistance", 0),("Ice Resistance", 0),("Earth Resistance",0),("Lightning Resistance", 0),("Physical Resistance",0),("Themes",themes),("Type","Tier "+str(level)+" Map")])
    Region["Defense"] = round(abs(rnd.triangular(1,(point+1)*(cnt+.5+1),(point+1)*(cnt*.2+1))),3)
    Region["Hit Rate"] = rnd.triangular(0,1,.1)+cnt
    Region["Critical Multiplier"] += rnd.triangular(0,1.7,cnt)*cnt
    Region["Critical Rate"] += rnd.triangular(0,1,.05)+cnt
    Region["Physical Resistance"] = rnd.triangular(0,1,cnt)*cnt
    if True in [bool(k in name) for k in ["Legendary","Mythical","Super Rare"]]:
        Region["Critical Rate"] = abs(.5 + rnd.triangular(0,.5,.2))
    if "Rare" in name:
        Region["Critical Rate"] = abs(.35 + rnd.triangular(0,.25,.1))
    if "Uncommon" in name:
        Region["Critical Rate"] = abs(.1 + rnd.triangular(0,.05,.025))    
    if "Common" in name:
        Region["Critical Rate"] = abs(.05 + rnd.triangular(0,.03,.001))
    if True in [bool(k in name) for k in IceAdj+IceNouns]:
        Region["Ice Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Region["Ice Damage"].sort()
        Region["Ice Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in FireAdj+FireNouns]:
        Region["Fire Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Region["Fire Damage"].sort()
        Region["Fire Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in EarthAdj+EarthNouns]:
        Region["Earth Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Region["Earth Damage"].sort()
        Region["Earth Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in LghtAdj+LghtNouns]:
        Region["Lightning Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Region["Lightning Damage"].sort()
        Region["Lightning Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in SpclAdj+SpclNouns]:
        Region["Fire Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Region["Fire Damage"].sort()
        Region["Ice Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Region["Ice Damage"].sort()
        Region["Earth Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Region["Earth Damage"].sort()
        Region["Physical Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75+point*.9,point*.2)]
        Region["Physical Damage"].sort()
        Region["Lightning Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Region["Lightning Damage"].sort()
        Region["Physical Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
        Region["Fire Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
        Region["Earth Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
        Region["Lightning Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
        Region["Ice Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt

    if Region["Critical Rate"] > 1:
        Region["Critical Rate"] = .95

    if Region["Hit Rate"] > 1:
        Region["Hit Rate"] = .95

    if Region["Fire Resistance"] > 1:
        Region["Fire Resistance"] = .95

    if Region["Ice Resistance"] > 1:
        Region["Ice Resistance"] = .95

    if Region["Earth Resistance"] > 1:
        Region["Earth Resistance"] = .95

    if Region["Physical Resistance"] > 1:
        Region["Physical Resistance"] = .95

    if Region["Lightning Resistance"] > 1:
        Region["Lightning Resistance"] = .95

    for J in Region.keys():
        Region[J] = Standardize(Region[J],3)

    return Region

def GenerateArmor(level,typ="Helm",themes=[]):
    cnt = rnd.choices([.1,.2,.3,.4,.5,.6,.7,.8,.9],[.3,.3,.15,.1,.05,.05,.02,.02,.01],k=1)[0]
    pointA = math.ceil(round(rnd.triangular(1,level,level*.6)))
    point = math.ceil(round(rnd.triangular(1,pointA*1.05,pointA*.4)))
    colors = ["Red","Orange","Yellow","Green","Blue","Cyan","Teal","Violet","Purple","Indigo","Grey","Ivory","Red-Orange","Orange-Yellow","Yellow-Green","Green-Blue","Blue-Green","Orange-Red","Yellow-Orange","Green-Yellow"]
    colorAdj = ["Dark","Light","Shimmering","Glowing","Shining","Basic","Fancy","Artistic","Random","Stochasticly","Erraticly"]
    nameAdj = ["Brutal","Strange","Exotic","Rusty","Metallic","Unstable"]+[i+" "+j for i,j in zip(colorAdj,colors)]
    nameAdjB = []
    nameAdjC = ["Legendary","Super","Rare","Uncommon","Common"]
    EarthAdj = ["Earthy","Muddy","Dearth","Cragged"]
    FireAdj = ["Burning","Blazing","Explosive","Burnt","Charred","Firey"]
    IceAdj = ["Freezing","Blizzard","Icy","Icicle Laden"]
    LghtAdj = ["Shocking","Storming","Electrifying","Blinding"]
    SpclAdj = ["Elemental","Nuclear","Hyper-Chromatic","Binding","Vorpal","Warping"]

    material = ["Steel","Silver","Gold","Diamond","Iron","Bronze","Crystal","Leather","Cotton","Wool","Kevlar","Titanium","Bearskin","Flannel","Canvas","Macrame","Lace"]
    if "earth" in themes:
        nameAdjB += EarthAdj
    if "fire" in themes:
        nameAdjB += FireAdj
    if "ice" in themes:
        nameAdjB += IceAdj
    if "lightning" in themes:
        nameAdjB += LghtAdj
    if "special" in themes:
        nameAdjB += SpclAdj
    if "random" in themes:
        nameAdjB += EarthAdj+FireAdj+IceAdj+LghtAdj+SpclAdj
    if typ == "Ring":
        material = ["Iron","Bronze","Diamond","Crystal","Silver","Sapphire","Gold","Amythest","Ruby","Emerald"]
        nameAdjB += ["Ring"]
        point *= .05
        pointA *= .05
    if typ == "Helm":
        nameAdjB += ["Helmet","Hat","Cap","Burqa","Hijab","Ascot","Akubra","Ayam","Balaclava","Barretina","Beanie","Beret","Bicorne","Biretta","Bowler","Derby"]
    if True in [bool(k == typ) for k in ["Chest","Legs","Arms","Wrists","Feet"]]:
        nameAdjB += ["Chailmail","Mail","Splint Mail","Ring mail","Platemail","Plate","Straps","Greaves","Gambeson","Cuisses","Sollerets","Vambraces","Brassairts","Gauntlets"]
    AdjA = [rnd.choice(nameAdj),rnd.choice(nameAdj)]
    K = AdjA[0]+" and "+AdjA[1]
    if AdjA[0] == AdjA[1]:
        K = "Very "+AdjA[0]
    name = "(+"+str(pointA)+") "+rnd.choices(nameAdjC,[.01,.04,.15,.35,.45],k=1)[0]+" "+K+" "+rnd.choice(material)+" "+rnd.choice(nameAdjB)
    Armor = clts.OrderedDict()
    Armor["Name"] = name
    Armor["Type"] = typ
    Armor["Gems"] = []
    Armor["Defense"] = 0
    Armor["Critical Multiplier"] = 0
    Armor["Critical Rate"] = 0
    Armor["Physical Damage"] = [0,0]
    Armor["Fire Damage"] = [0,0]
    Armor["Ice Damage"] = [0,0]
    Armor["Earth Damage"] = [0,0]
    Armor["Lightning Damage"] = [0,0]
    Armor["Physical Resistance"] = 0
    Armor["Fire Resistance"] = 0
    Armor["Ice Resistance"] = 0
    Armor["Earth Resistance"] = 0
    Armor["Lightning Resistance"] = 0
    Armor["Defense"] = int(round(abs(rnd.triangular(pointA*.6,pointA*1.5,pointA*.8))))
    Armor["Hit Rate"] = abs(rnd.triangular(0,1,cnt))*cnt
    Armor["Sockets"] = rnd.choice(range(5))
    Armor["Gems"] = rnd.sample([GenerateGem(point,themes=rnd.choices(["","fire","ice","lightning","earth","random","special"],k=3))]*10,k=rnd.choice(range(Armor["Sockets"]+1)))
    Armor["Critical Multiplier"] += rnd.triangular(0,2,cnt+.1)
    Armor["Critical Rate"] += rnd.triangular(0,1,cnt+.1)*cnt
    Armor["Physical Resistance"] = rnd.triangular(0,1,cnt)*cnt
    if True in [bool(k in name) for k in IceAdj]:
        Armor["Ice Damage"] = [round(rnd.normalvariate(point,point*.1),2),round(rnd.normalvariate(point*1.2,point*.1),3)]
        Armor["Ice Damage"].sort()
        Armor["Ice Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in FireAdj]:
        Armor["Fire Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Armor["Fire Damage"].sort()
        Armor["Fire Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in EarthAdj]:
        Armor["Earth Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Armor["Earth Damage"].sort()
        Armor["Earth Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
    if True in [bool(k in name) for k in SpclAdj]:
        Armor["Fire Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Armor["Fire Damage"].sort()
        Armor["Ice Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Armor["Ice Damage"].sort()
        Armor["Earth Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.01)]
        Armor["Earth Damage"].sort()
        Armor["Physical Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.5,point*.02)]
        Armor["Physical Damage"].sort()
        Armor["Lightning Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Armor["Lightning Damage"].sort()
        Armor["Fire Resisistance"] = abs(rnd.traingular(0,1,cnt))*cnt
        Armor["Earth Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt
        Armor["Lightning Resistance"] = abs(rnd.traingular(0,1,cnt))*cnt
        Armor["Ice Resistance"] = abs(rnd.triangular(0,1,cnt))*cnt

    if Armor["Critical Rate"] > 1:
        Armor["Critical Rate"] = .95

    if Armor["Hit Rate"] > 1:
        Armor["Hit Rate"] = .95

    if Armor["Physical Resistance"] > 1:
        Armor["Physical Resistance"] = .95    

    if Armor["Fire Resistance"] > 1:
        Armor["Fire Resistance"] = .95

    if Armor["Ice Resistance"] > 1:
        Armor["Ice Resistance"] = .95

    if Armor["Earth Resistance"] > 1:
        Armor["Earth Resistance"] = .95

    if Armor["Lightning Resistance"] > 1:
        Armor["Lightning Resistance"] = .95

    for J in Armor.keys():
        Armor[J] = Standardize(Armor[J],3)
    
    return Armor

def GenerateWeapon(level):
    point = math.ceil(rnd.triangular(1,level*1.3,level*.8))
    nameOpts = ["Knife","Shank","Claw","Dagger","Sword","Saber","Wand","Staff","Axe","Cudgel","Mace","Greater Maul", "Great Axe","Bastard Sword","Whip","Bow","LongBow","Scmitar","GreatSword","LongSword"]
    nameAdjA = ["Legenary","Super","Rare","Uncommon","Common"]
    EarthAdj = ["Earthy","Muddy","Dearth","Cragged"]
    FireAdj = ["Burning","Blazing","Explosive","Burnt","Charred","Firey"]
    IceAdj = ["Freezing","Blizzard","Icy","Icicle Laden"]
    LghtAdj = ["Shocking","Storming","Electrifying","Blinding"]
    SpecialAdj = ["Elemental","Nuclear","Hyper-Chromatic"]
    nameAdj = FireAdj+IceAdj+LghtAdj+SpecialAdj+EarthAdj
    Adj = rnd.choices(nameAdjA,[.01,.04,.15,.35,.45],k=1)[0]+" "+rnd.choice(nameAdj)+" "+rnd.choice(nameAdj)
    TyP = rnd.choice(nameOpts)
    name = "(+"+str(point)+") "+Adj+" "+TyP
    minP = point*rnd.triangular(.6,1.5,.9)+10
    maxP = point*rnd.triangular(.8,1.8,1.3)+10
    Weapon = clts.OrderedDict([("Name", name),("Gems",[]),("Hit Rate", 0),("Critical Rate", 0),("Critical Multiplier", 0),("Physical Damage", [minP,maxP]),("Fire Damage", [0,0]),("Ice Damage", [0,0]),("Earth Damage", [0,0]),("Lightning Damage", [0,0]),("Hands Required", 1),("Type",TyP)])
    if True in [bool(k in name) for k in ["Bow","LongBow","Cudgel","Great Axe","Staff","Maul","Greater Mace","GreatSword","LongSword"]]:
        Weapon["Hands Required"] = 2
    Weapon["Hit Rate"] += rnd.uniform(.4,.9)
    Weapon["Sockets"] = rnd.choice(range(5))
    Weapon["Gems"] = rnd.sample([GenerateGem(point,themes=rnd.choices(["","fire","ice","lightning","earth","random","special"],k=3))]*10,k=rnd.choice(range(Weapon["Sockets"]+1)))
    Weapon["Critical Multiplier"] += 1 + rnd.normalvariate(.5,.05)
    Weapon["Critical Rate"] += abs(.01 + rnd.normalvariate(.02,.02))
    if "Legenary" in name:
        Weapon["Critical Rate"] += abs(.5 + rnd.normalvariate(.2,.05))
    if "Mythical" in name:
        Weapon["Critical Rate"] += abs(.35 + rnd.normalvariate(.2,.05))
    if "Rare" in name:
        Weapon["Critical Rate"] += abs(.2 + rnd.normalvariate(.2,.05))    
    if "Uncommon" in name:
        Weapon["Critical Rate"] += abs(.05 + rnd.normalvariate(.05,.01))
    if "Common" in name:
        Weapon["Critical Rate"] += abs(.01 + rnd.normalvariate(.03,.01))
    Weapon["Physical Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point+point*1.75,point*1.1)]
    Weapon["Physical Damage"].sort()
    if True in [bool(k in name) for k in IceAdj]:
        Weapon["Ice Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Weapon["Ice Damage"].sort()
    if True in [bool(k in name) for k in FireAdj]:
        Weapon["Fire Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Weapon["Fire Damage"].sort()
    if True in [bool(k in name) for k in LghtAdj]:
        Weapon["Lightning Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Weapon["Lightning Damage"].sort()
    if True in [bool(k in name) for k in EarthAdj]:
        Weapon["Earth Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Weapon["Earth Damage"].sort()
    if True in [bool(k in name) for k in SpecialAdj]:
        Weapon["Fire Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Weapon["Fire Damage"].sort()
        Weapon["Ice Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Weapon["Ice Damage"].sort()
        Weapon["Earth Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Weapon["Earth Damage"].sort()
        Weapon["Physical Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.3)]
        Weapon["Physical Damage"].sort()
        Weapon["Lightning Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.2,point*.1)]
        Weapon["Lightning Damage"].sort()

    for J in Weapon.keys():
        Weapon[J] = Standardize(Weapon[J],3)

    return Weapon

def GenerateCreature(level,themes=[],typ="Normal"):
    cnt = .2
    if typ == "Normal":
        pass
    if typ == "Large":
        cnt += .15
    if typ == "Small":
        cnt -= .15
    if typ == "Midboss":
        cnt += .3
    if typ == "Boss":
        cnt += .5
    point = 1+math.floor(rnd.triangular(.2,1.1,.7)*level)
    colors = ["Red","Orange","Yellow","Green","Blue","Cyan","Teal","Violet","Purple","Indigo","Grey","Ivory","Red-Orange","Orange-Yellow","Yellow-Green","Green-Blue","Blue-Green","Orange-Red","Yellow-Orange","Green-Yellow"]
    colorAdj = ["Dark","Light","Shimmering","Glowing","Shining","Basic","Fancy"]
    nameAdj1 = ["Horrifying","Brutal","Strange","Exotic","Chromatic","Elemental","Skittish","Rusty","Metallic","Unstable","Scary"]+[i+" "+j for i,j in zip(colorAdj,colors)]
    SzAdj = ["Huge","Large","Medium","Regular","Small","Tiny"]
    EarthAdj = ["Nuclear","Muddy","Mud","Leaf","Leafy","Weathery"]
    FireAdj = ["Explosive","Blazing","Burning","Firey","Flame","Flaming"]
    IceAdj = ["Watery","Drowning","Icy","Freezing","Freeze","Frozen","Blizzard"]
    LghtAdj = ["Shocking","Stroming","Electrifying","Winding","Blinding"]
    GeneralNames = ["Brown-Bear","Black-Bear","Eagle","Zebra","Koala","Dog","Cat","Mouse","Bat","Tiger","Deer","Spider","Bug",str(point)+"-legged Arachnid","Scorpion","Ant","Devil","Angel","Horse","Lion",str(point)+"-eyed Beast",str(point)+"-tentacled Abomination","Abomination","Golem","Living Statue","Statue"]
    nameComm = ["Mythical","Legendary","Super Rare","Rare","Uncommon","Common"]
    if "earth" in themes:
        nameAdj1 += EarthAdj
    if "fire" in themes:
        nameAdj1 += FireAdj
    if "ice/water" in themes:
        nameAdj1 += IceAdj
        GeneralNames += ["Polar Bear", "Penguin","Seal","Sealion","Moose"]
    if "lightning" in themes:
        nameAdj1 += LghtAdj
    if "random" in themes:
        nameAdj1 += EarthAdj+FireAdj+IceAdj+LghtAdj
    AdjA = [rnd.choice(nameAdj1),rnd.choice(nameAdj1)]
    K = AdjA[0]+" and "+AdjA[1]
    if AdjA[0]==AdjA[1]:
        K = "Very "+AdjA[0]
    name = "Level "+str(level)+" "+rnd.choices(nameComm,[.01,.02,.02,.15,.3,.5],k=1)[0]+" "+K+" "+rnd.choices(SzAdj,[.05,.05,.1,.15,.3,.35],k=1)[0]+" "+rnd.choice(GeneralNames)
    HP = 1+math.ceil(point*rnd.triangular(.8,3.5,1))
    GoldVal = point*rnd.triangular(0,1,cnt)
    Creature = clts.OrderedDict()
    Creature["Name"] = name
    Creature["Current HP"] = HP
    Creature["Maximum HP"] = HP
    Creature["Experience Value"] = 0
    Creature["Gold Value"] = 0
    Creature["Experience Value"] += math.ceil(GoldVal*rnd.triangular(.3,3,cnt+.4))
    Creature["Gold Value"] += math.ceil(GoldVal*rnd.triangular(.5,5,cnt+.8))
    Creature["Defense"] = 0
    Creature["Hit Rate"] = 0
    Creature["Critical Multiplier"] = 0
    Creature["Critical Rate"] = 0
    Creature["Physical Damage"] = [0,0]
    Creature["Fire Damage"] = [0,0]
    Creature["Ice Damage"] = [0,0]
    Creature["Earth Damage"] = [0,0]
    Creature["Lightning Damage"] = [0,0]
    Creature["Physical Resistance"] = 0
    Creature["Fire Resistance"] = 0
    Creature["Ice Resistance"] = 0
    Creature["Earth Resistance"] = 0
    Creature["Lightning Resistance"] = 0
    Creature["Defense"] += math.ceil(abs(rnd.triangular(1,(point+1)*(cnt+.5+1),(point+1)*(cnt*.2+1))))
    Creature["Hit Rate"] = rnd.triangular(0,1,.45)
    Creature["Critical Multiplier"] += rnd.triangular(0,5,cnt)
    Creature["Critical Rate"] += rnd.triangular(0,1,.05)
    Creature["Physical Resistance"] += rnd.triangular(0,1,cnt)*cnt
    if True in [bool(k in name) for k in ["Legendary","Mythical","Super Rare"]]:
        Creature["Critical Rate"] = abs(.5 + rnd.triangular(0,.5,.15))
    if "Rare" in name:
        Creature["Critical Rate"] = abs(.35 + rnd.triangular(0,.25,.1))
    if "Uncommon" in name:
        Creature["Critical Rate"] = abs(.2 + rnd.triangular(0,.1,.03))    
    if "Common" in name:
        Creature["Critical Rate"] = abs(.05 + rnd.triangular(0,.03,.001))
    if True in [bool(k in name) for k in IceAdj]:
        Creature["Ice Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Creature["Ice Damage"].sort()
        Creature["Ice Resistance"] += abs(rnd.triangular(0,1,cnt))
    if True in [bool(k in name) for k in FireAdj]:
        Creature["Fire Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Creature["Fire Damage"].sort()
        Creature["Fire Resistance"] += abs(rnd.triangular(0,1,cnt))
    if True in [bool(k in name) for k in EarthAdj]:
        Creature["Earth Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Creature["Earth Damage"].sort()
        Creature["Earth Resistance"] += abs(rnd.triangular(0,1,cnt))
    if True in [bool(k in name) for k in ["Chromatic","Elemental"]]:
        Creature["Fire Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Creature["Fire Damage"].sort()
        Creature["Ice Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Creature["Ice Damage"].sort()
        Creature["Earth Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Creature["Earth Damage"].sort()
        Creature["Physical Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75+point*.9,point*.2)]
        Creature["Physical Damage"].sort()
        Creature["Lightning Damage"] = [rnd.normalvariate(point,point*.1),rnd.normalvariate(point*1.75,point*.1)]
        Creature["Lightning Damage"].sort()
        Creature["Physical Resistance"] += abs(rnd.triangular(0,1,cnt))
        Creature["Fire Resistance"] += abs(rnd.triangular(0,1,cnt))
        Creature["Earth Resistance"] += abs(rnd.triangular(0,1,cnt))
        Creature["Lightning Resistance"] += abs(rnd.triangular(0,1,cnt))
        Creature["Ice Resistance"] += abs(rnd.triangular(0,1,cnt))

    if Creature["Critical Rate"] > 1:
        Creature["Critical Rate"] = .95

    if Creature["Hit Rate"] > 1:
        Creature["Hit Rate"] = .95

    if Creature["Fire Resistance"] > 1:
        Creature["Fire Resistance"] = .95

    if Creature["Ice Resistance"] > 1:
        Creature["Ice Resistance"] = .95

    if Creature["Earth Resistance"] > 1:
        Creature["Earth Resistance"] = .95

    if Creature["Lightning Resistance"] > 1:
        Creature["Lightning Resistance"] = .95

    for J in Creature.keys():
        Creature[J] = Standardize(Creature[J],3)

    return Creature

def GenerateLoot(player,number, modif):
    loot = []
    for i in range(number):
        armors = [GenerateArmor(player["Level"]*(1+rnd.choice(range(10))*.3+modif),typ=rnd.choice(["Helm","Legs","Chest","Wrists","Feet","Arms","Ring"]))]*10
        weapons = [GenerateWeapon(player["Level"]*(1+rnd.choice(range(10))*.3+modif))]*10
        gems = [GenerateGem(player["Level"]*(1+rnd.choice(range(10))*.3+modif),themes=rnd.choices(["","","","","fire","fire","fire","ice","lightning","lightning","ice","random","special",""],k=2))]*10
        loot.append(rnd.choice(armors+weapons+gems))

    return loot
