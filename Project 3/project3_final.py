import random

class item:
    def __init__(self, name, desc, uses):
        """create name, description, uses for an item"""
        self.name = name # name of the item
        self.desc = desc # item description
        self.uses = uses # how many times the item can be used

        
    def checkuses(self):
        """verifies that the item can be used"""
        try:
            #print(f"{self.name} is used!")
            if self.uses > 0:
                return True

            else:
                return False
        except:
            print("problem in consume, item class")

    def inspect(self):
        print(f"{self.desc} \nit appears to have {self.uses} uses left")
#end item class

class weapon(item):
    def __init__(self, name, desc, uses, damage):
        super().__init__(name, desc, uses)
        self.damage = damage

    def use(self):
        try:
            if self.checkuses() == True:
                print(f"{self.name} is used to strike")
                self.uses -= 1
                if self.checkuses() == False:
                    print(f"{self.name} has broken from the attack")
                return self.damage
                
            else:
                print(f"{self.name} is no longer usable")
                return 0
        except:
            print("problem in use, weapon class")
#end weapon class

class inventory:
    def __init__(self):
        """establish inventory and limits for weapons and items"""
        self.weaponlimit = 3
        self.itemlimit = 5
        self.weapons = {}
        self.items = {}
        
    def addweapon(self, weapon):
        """adds weapon to inventory"""
        try:
            if len(self.weapons) <= self.weaponlimit:
                self.weapons.update({weapon.name:weapon})
                print(f"{weapon.name} added to inventory")
        except:
            print("problem in addweapon, inventory class")
            
    def removeweapon(self, weapon):
        """removes weapon from inventory"""
        try:
            if weapon in self.weapons:
                self.weapons.pop(weapon)
                print(f"{weapon.name} removed from inventory")
            else:
                print("weapon does not exist")
            

        except:
            print("problem in removeweapon, inventory class")
#end inventory class


class entity:
    """baseline for all 'living' things in the game, name and hitpoint args"""
    def __init__(self, name, hitpoints):
        self.name = name
        self.hitpoints = hitpoints
        self.modifiers = []

    def hurt(self,source):
        try:
            if self.hitpoints >= 1:
                self.hitpoints -= source
                print(f"{source} damage dealt to {self.name}\n")
        except:
            print("problem in hurt, entity class")

    def checkdeath(self):
        if self.hitpoints <= 0:
            
            print(f"{self.name} has been eliminated!\n")
            return 1
#end entity class
            
class player(entity):
    """creates player entity"""
    def __init__(self, name, hitpoints):
        super().__init__(name, hitpoints)
        self.inventory = inventory()

    def useweapon(self):
        try:
            for i in self.inventory.weapons:
                print (i)
            flag = 1
            while flag == 1:
                select = input("select weapon to use").lower()
                for i in self.inventory.weapons:
                    if select == i.lower():
                        flag = 0
                        return self.inventory.weapons[i].use()
                    else:
                        print("invalid input, try again")

        except:
            print("problem in useweapon, player class")
#end player class

class enemyent(entity):
    """creates enemy entity"""
    def __init__(self, name, hitpoints):
        super().__init__(name, hitpoints)
    def damage(self):
        return random.randint(30,50)
#end enemyent class
            
class menu(player):
    def createplayer():
        #class layout: {'name' : [hp, weapon name, weapon description, weapon damage, weapon uses] }
        classdict = {"warrior" : 
                     [120, "broadsword", "sharp slab of metal", 45, 15],
                     "mage" :
                     [70, "fireball", "lethal thrown fire", 60, 10],
                     "paladin" :
                     [220, "shield", "blunt short-ranged metal slab", 15, 40]
                    }
        for i in classdict:
            print (i)
        flag = 1
        while flag == 1:
            temp = input("select a class to play\n").lower()
            if temp in classdict:
                #print("true")
                global playerteam
                playerteam = []
                #create player
                playerteam.append(player(temp, classdict[temp][0]))
                #add starting weapon to inventory
                playerteam[0].inventory.weapons.update({classdict[temp][1]:
                                                        #create an object from weapons class with name, description, damage, uses
                                                weapon(classdict[temp][1], classdict[temp][2],classdict[temp][4],classdict[temp][3])
                                               })
                flag = 0
                break
            else: 
                print("invalid input, try again")
#end menu class

# =================================COMBAT=======================================
class combat:
    def initialize():
        global enemyteam
        enemyteam = []
        #print("1a")

    def combatcycle(combatstate):
        state = combatstate
        if state == 0: #combat start
            #print("a") #indicate that combat has started
            #teams should be initialized
            combat.initialize()
            combat.addenemy()
            
        if state == 1: #player turn
            #print("b") 
            #player can take action
            try:
                #print("b1")
                if (len(enemyteam) > 0) and (len(playerteam) > 0):
                    print("enemies on the field:\n")
                    enemyindex = 0
                    for enemy in enemyteam:
                        print(f"at position {enemyindex}, {enemy.name} with {enemy.hitpoints} hitpoints")
                        enemyindex += 1
                    flag = 1
                    while flag == 1:
                        #breaks if someone puts a string :(
                        select = int(input("choose an enemy position to attack"))
                        if select in range(enemyindex):
                            enemyteam[select].hurt(playerteam[0].useweapon() + random.randint(0,40))
                            #print (enemyteam[select])
                            if enemyteam[select].checkdeath() == 1:
                                global score
                                score += 1
                                print(f"{score} score")
                                #print(select)
                                del enemyteam[select]
                            flag = 0
                            break
                        else:
                            print("invalid input, try again")
                if len(enemyteam) == 0:
                    print("there are no enemies to fight")
                elif len(playerteam) == 0:
                    print("player no longer exists")
                
            except:
                print("problem during player turn")
            
            
        if state == 2: #enemy turn
            #print("c") #enemy chooses the last item in the playerteam to attack
            try:
                if len(playerteam) == 0:
                    print("all allies have been eliminated")
                elif playerteam[-1].hitpoints > 0:
                    #print("ec")
                    for enemy in enemyteam:
                        print(f"{enemy.name} attacks")
                        playerteam[-1].hurt(enemy.damage())
                        if playerteam[-1].checkdeath() == 1:
                            #print ("at")
                            del playerteam[-1]
                
            except:
                print("problem during enemy turn")
                    
            
        if state == 3: #intermission
            #print("d") #displays health of every entity that remains
            try:
                if len(playerteam) > 0:
                    for ally in playerteam:
                        print(f"{ally.name} has {ally.hitpoints} hitpoints remaining")
                if len(enemyteam) > 0:
                    for enemy in enemyteam:
                        print(f"{enemy.name} has {enemy.hitpoints} hitpoints remaining")
                
            except:
                print("problem during intermission")

        if state == 4: #end combat cycle
            #print("e")
            try:
                if len(playerteam) == 0:
                    print("game over")
                    print(f"final score is {score}")
                elif len(enemyteam) == 0:
                    print("combat over")
            except:
                print("problem during end combat")
                
    def addenemy():
        global enemyteam
        enemyteam.append(enemyent("rat", random.randint(20, 80)))
                
    def combatloop():
        flag = 1
        combat.combatcycle(0)
        while flag == 1:
            for i in range(3):
                combat.combatcycle(i+1)
                if (len(playerteam) == 0) or (len(enemyteam) == 0):
                    combat.combatcycle(4)
                    flag = 0
                    break
            

#========================GAMESTATES==============================
class gamestates:
    #gamestates include combat, noncombat
    def gamecycle(gamestate):
        state = gamestate
        if state == 0: #menu
            try:
                menu.createplayer()
            except:
                print("problem with menu state")
        if state == 1: #noncombat phase
            try:
                print("save\n")
            except:
                print("problem with noncombat phase")
        if state == 2: #combat phase
            try:
                print("combat begins\n")
                combat.combatloop()
            except:
                print("problem with combat phase")
                
    def gameloop():
        global playerteam
        global score
        score = 0
        gamestates.gamecycle(0)
        while len(playerteam) > 0:
            gamestates.gamecycle(1)
            gamestates.gamecycle(2)
        
#end of gamestates class

#==========================END OF CLASSES==============================

gamestates.gameloop()