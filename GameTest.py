import random as r
from random import randint

hp = 0
coins = 0
damage = 0

def printParameters():
    print("")
    print("Sul on {0} elu, {1} luumurd(u) ja {2} money.".format(hp, damage, coins))

def printHp():
    print("")
    print("Sul on", hp, "elu.")

def printCoins():
    print("")
    print("Sul on", coins, "money.")

def printDamage():
    print("")
    print("Sul on", damage, "luumurd(u).")

def meetShop():
    global hp
    global damage
    global coins

    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print("")
        print("Sul pole raha, mine muretse juurde")
        return False

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5) * weaponLvl
    weapons = ["Saatana sarv", "Kalevipoja nui", "Kivi (Saab visata)", "Ragulka", "Lestakala"]
    weaponRarities = ["Roostes", "Haruldane", "Legendaarne"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponCost = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)

    oneHpCost = 5
    threeHpCost = 12
    print("")
    print("Teel kohtasite kaupmeest!")
    printParameters()
    
    while input("Kas tahad midagi osta või lahkuda? (O/L): ").upper() == "O":
        print("")
        print("1) Üks HP -", oneHpCost, "money;")
        print("2) Kolm HP -", threeHpCost, "money;")
        print("3) {0} {1} - {2} money".format(weaponRarity, weapon, weaponCost))

        choice = input("Mida tahad osta: ")
        if choice == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
        elif choice == "2":
            if buy(threeHpCost):
                hp += 3
                printHp()
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        else:
            print("")
            print("Ma ei müü seda.")

def meetMonster():
    global hp
    global coins

    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Kanged mehed Turjamaalt", "Härjapõlvlane", "Kratt", "Küla joodik", "Lumivalguke", "Saatana käsilane"]

    monster = r.choice(monsters)
    print("")
    print("Sa kohtasid vastast - {0}, Tal on {1} level, {2} elu ja {3} luumurd(u).".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()

    while monsterHp > 0:
        print("")
        choice = input("Mida sa teed ründa/jookse (R/J): ").lower()

        if choice == "r":
            monsterHp -= damage
            print("")
            print("Sa ründasid vastast ja tal on alles", monsterHp, "elu.")
        elif choice == "j":
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print("")
                print("Sul õnnestus lahinguväljalt põgeneda!")
                break
            else:
                print("")
                print("Vastane oli liiga tugev ja jõudis sulle järele...")
        else:
            continue

        if monsterHp > 0:
            hp -= monsterDmg
            print("")
            print("Vastane ründas ja te kaotasite", monsterDmg, "elu.")
            print("Teil on alles", hp, "elu.")
        
        if hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl*2
        coins += loot
        print("")
        print("Teil õnnestus Vastane võita, mille eest saite", loot, "money.")
        printCoins()
    
def initGame(initHp, initCoins, initDamage):
    global hp
    global coins
    global damage

    hp = initHp
    coins = initCoins
    damage = initDamage
    print("")
    print("Tere tulemast, siit algab sinu seiklus!")
    printParameters()

def gameLoop():
    situation = r.randint(0, 10)

    if situation == 0:
        meetShop()
    elif situation >= 8:
        meetMonster()
    else:
        input("Kõnnid mööda tänavat...")

def print_menuu():    
    print (30 * "-" , "MENÜÜ" , 30 * "-")
    print ("[1] Uus mäng")
    print ("[2] Salvesta mäng")
    print ("[3] Lae mäng")
    print ("[4] Credits")
    print ("[5] Välju mängust")
    print (67 * "-")
    global valik
    valik = int(input("Valik [1-5]: "))

loop=True      
  

def salvestamine():
    nimi = input("Sisestage oma nimi: ")

    with open('readme.txt', 'w') as f:
        f.write('readme')





        
while loop:   
    print_menuu()   

    if valik==1:
        print ("Tere tulemast uude mängu!")
        loop = False
        initGame(randint(1, 1),randint(4, 8),randint(1, 1))
    elif valik==2:
        print ("Salvestasid mängu")
        
    elif valik==3:
        print ("Laadisid mängu")
        
    elif valik==4:
        print("")
        print ("Martin Pettai, Jass Õunapuu, Artjom Vinogradov")
        print("")
    elif valik==5:
        loop = False
        exit()
    else:
        print("Vale valik, oled kindel, et vajutasid õiget klahvi?")



while True:
    gameLoop()

    if hp <= 0:
        if input("Kas tahad menüüsse tagasi minna? (jah/ei): ").lower() == "jah":
            print_menuu()
        else:
            break