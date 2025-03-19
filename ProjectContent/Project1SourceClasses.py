#classes

#start of Entity class
class Entity:
    def __init__(self, name, description, inventory_limit, team, hitpoints,):
        #Entities are characters/creatures that exist in the game
        #all entities have hitpoints and 'die' if it reaches zero
        """establish all the parameters of an entity, playable or not"""
        self.name = name # entity name
        self.description = description # entity description
        self.inventorylimit = inventory_limit
        self.inventory = {} # entity inventory, in dictionary form
        self.team = team # team number, in integer form
        self.hitpoints = hitpoints # amount of damage the Entity can take before death, in integer form
        self.livingstate = True # state of alive or dead, in boolean form

    
    def checklivingstate(self):
        #boolean return meant to be used in other methods
        #this method is for preventing someone from doing something if they are dead
        """checks if the entity is alive"""
        return self.livingstate

        
    def hurt(self, damage):
        #damages the entity, damage comes from an external source preferably the Item class or associated subclasses
        """receives damage, check if hitpoints are less than zero and declares false if true: requires argument 'damage' """ 
        self.hitpoints -= damage
        if self.hitpoints < 0:
            self.livingstate = False # false = dead

            
    def checkteam(self, target):
        #takes the team integer from the entity and compares it
        #this method is for preventing hurting someone on the same team
        """returns false if team numbers are the same, returns true otherwise: requires argument 'target' """
        if self.team == target.team:
            return False # false = they are not on the same team
        else:
            return True # true = they are on the same team

            
    def checkinventorylimit(self):
        #takes the inventory of the entity and checks it using the limit
        """checks if inventory space available is less than inventory limit """
        counter = 0 # temporary variable
        for index in self.inventory: # for every element in the inventory
            counter += 1
        if counter < self.inventorylimit: # if number of elements in the inventory is less than the inventory limit 
            return True  #returns true if true, inventory is not full
        else:
            return False # returns false if inventory is full

            
    def additem (self, itemkey, itemvalue):
        """adds an item to the entity's inventory: requires argument 'itemkey' and 'itemvalue' """
        if self.checkinventorylimit() == True: #checks if there is space in the inventory
            try:
                self.inventory.update({itemkey:itemvalue}) #updates the inventory dictionary with given arguments
            except:
                print('error with item key or item value')
        else:
            print('inventory is full, items can no longer be added')

            
    def removeitem (self, item):
        """removes an item from the entity's inventory: requires argument 'item' """
        try:
            self.inventory.pop(item) #removes the item argument from the inventory
        except:
            print('error with item name')
        
# end of Entity class

#start of Player subclass
class Player(Entity):
    #inherits from the class entity
    def __init__(self, name, description, inventory_limit, team, hitpoints, playertype):
        super().__init__(name, description, inventory_limit, team, hitpoints)
        self.playertype = playertype # category that player selects to be their character

#end of Player subclass

#start of Item class
class Item:
    def __init__(self, name, desc, uses):
        """create name, description, uses for an item"""
        self.name = name # name of the item
        self.desc = desc # item description
        self.uses = uses # how many times the item can be used

        
    def consume(self):
        """takes 1 use from the item"""
        print(f"{self.name} is used!")
        if self.uses > 0:
            self.uses -= 1 #subtracts one use from the item if it isnt zero already
            return True
            
        else:
            print('use failed!')
            return False

            
    def checkconsume(self):
        #method used to check if an item still has uses
        """checks if item can be consumed"""
        if self.uses > 0:
            return True
        else:
            return False

            
    def inspect(self):
        """returns the description of the item"""
#end of Item class

#start of Weapon subclass

class Weapon(Item, Entity):
    # inherits from classes Item and Entity
    # entity is only used for damage in the attack method
    def __init__(self, name, desc, uses, damage):
        """child of item, introduces damage"""
        super().__init__(name, desc, uses)
    
        self.damage = damage

        
    def attack(self, user, target):
        #this method uses methods from two different classes :skull:
        """attacks with the weapon: requires arguments 'user' and 'target' """
        print(f"{user.name} attacks {target.name} with {self.name}!")
        if self.checkconsume() & target.state & user.checkteam(target) == True:
        #self.checkconsume() - method in the Item class. returns bool checking if an item can be consumed
        #target.state() - method in the Entity class. returns bool. False = dead, True = alive
        #user.checkteam(target) - method in the Entity class. returns true if target is not on the same team
        # if all([self.checkconsume(),target.state(),user.checkteam(target)]) == True:
            try:
                self.consume()
                target.hurt(self.damage)
                if target.state == False:
                    print(f'{target.name} is dead')
                else:
                    print(f'{target.name} takes {self.damage} damage.')
                #self.consume() - method in the Item class. 
                #target.hurt(argument) - method in the Entity class. subtracts argument from hitpoints
                #self.damage() - parameter in the Weapon class - damage of the weapon
                # in this code block:
                # before attacking, check if item can be consumed, target is alive, and target is on another team
                # consume 1 item use and apply damagw
            except:
                print("erm")
        else:
            print("impossible")
            
#end of Weapon subclass

#start of menu class
class Menu(Entity):
    #inherits from the class entity
    def __init__(self, name, description, inventory_limit, team, hitpoints):
        super().__init__(name, description, inventory_limit, team, hitpoints)
    def initialize():
        global characterdict
        #establishing a global for one method in this class :skull:
        characterdict = {
            "magic": [
                {"wizard": ['wizard', 'tbd', 5, 1, 120]},
                {"sorcerer": ['sorcerer', 'tbd', 5, 1, 120]},
                {"necromancer": ['necromancer', 'tbd', 5, 1, 120]}
            ],
            "brawler": [
                {"barbarian": ['barbarian', 'tbd', 5, 1, 120]},
                {"giant": ['giant', 'tbd', 5, 1, 120]},
                {"gladiator": ['gladiator', 'tbd', 5, 1, 120]}
            ],
            "swordsman": [
                {"samurai": ['samurai', 'tbd', 5, 1, 120]},
                {"crusader": ['crusader', 'tbd', 5, 1, 120]},
                {"buster": ['buster', 'tbd', 5, 1, 120]}
            ],
            "stealth": [
                {"druid": ['druid', 'tbd', 5, 1, 120]},
                {"ninja": ['ninja', 'tbd', 5, 1, 120]},
                {"rogue": ['rogue', 'tbd', 5, 1, 120]}
            ],
            "healer": [
                {"cleric": ['cleric', 'tbd', 5, 1, 120]},
                {"sage": ['sage', 'tbd', 5, 1, 120]},
                {"shaman": ['shaman', 'tbd', 5, 1, 120]}
            ]
            }
        
    def playerselect(inputdict):
        """player selects class to play as"""
        temp = input("select a class\n")
        choice = temp.lower()
        player = 0
        index = 0
        #this loop is designed to iterate through the heirarchy: dict/list/dict
        if choice == "help":
            print("here is what you can choose from\n")
            for i in inputdict:
                #print(i)
                for j in inputdict[i]:
                    # print(j)
                    # print(index)
                    for k in inputdict[i][index]:
                        print(inputdict[i][index][k][0])
                    index += 1
                index = 0
            return Menu.playerselect(inputdict)
        for i in inputdict:
            # print(i)
            for j in inputdict[i]:
                # print(j)
                # print(index)
                for k in inputdict[i][index]:
                    # print(characterdict[i][index][k][0])
                    if choice == inputdict[i][index][k][0]:
                        # for p in range(4):
                        #     print(inputdict[i][index][k][p])
                        player = Entity(inputdict[i][index][k][0],
                                         inputdict[i][index][k][1],
                                          inputdict[i][index][k][2],
                                           inputdict[i][index][k][3],
                                            inputdict[i][index][k][4])
                index += 1
            index = 0
            
        # print(player)    
        if player != 0:
            return player
        else:
            print("class does not exist")
            return Menu.playerselect(inputdict)
            # return 0
            # if Menu.retryinput() == True:
            #     Menu.playerselect(inputdict)
            # return player
            

    def playercreate(inputdict):
        """user creates a character"""
        #open json file function, writable
        #temp = playerselect()
        global playercharacter
        playercharacter = Menu.playerselect(inputdict)
        return playercharacter
        #write temp to player data json

    def gamestart():
        """initiates game"""
        #local choice
        choice = 0
        Menu.initialize()
        #resets globals
        global enemylist
        enemylist = []
        global playercharacter
        playercharacter = 0
        #import jsons and assign accordingly
        #global characterdict
        #characterdict = loadjson(characters)
        
        print("welcome\n would you like to mindlessly press 1")
        choice = int(input())
        if choice == 1:
            print("let us begin")
            Menu.gamenewgame()
        else:
            print("guess not")
        
    def gamenewgame():
        global characterdict
        """tells the player to choose between creating a new game or loading a save"""
        print("would you like to: \n 1: start a new game \n 2: load a save \n")
        choice = int(input())
        if choice == 1:
            print("creating a new character...")
            #creates a new character and starter item
            global playercharacter
            playercharacter = Menu.playercreate(characterdict)
            #print(playercharacter)
            starteritem = Menu.starteritemselect()
            playercharacter.additem(starteritem.name, starteritem)
            MainGame.playcycle()


        elif choice == 2:
            print("loading savefiles...(this doesnt work yet)")
            #try:
            # load json function
            #except:
            # "those files do not exist"
        else:
            print("invalid input")
            if Menu.retryinput() == True:
                return Menu.gamenewgame()
            
    def retryinput():
        """prompts the user to retry an input"""
        #this method can destroy some things
        print("invalid input,\n retry input?\n 1: yes\n 2: no\n")
        choice = int(input())
        if choice == 1:
            print("sending you back...")
            return True
        elif choice == 2:
            print("exiting...")
            return 0
        else:
            print("guess not")
            return 0
            
    def starteritemselect():
        starterweapons = [Weapon("club", "blunt stick, quite durable", 25, 15),
                        Weapon("strange robot bird pile", "each one says it delivers a warm hug", 7, 9999),
                        Weapon("brittle sword", "made with too high of a hardness, seems brittle", 12, 45)
                        ]
        #temporary list to store item names
        tempnums = []
        print("select an item to start your journey\n")
        index = 0
        choice = 0
        for i in starterweapons:
            print(f"{index + 1}. {starterweapons[index].name}")
            tempnums.append(index + 1)
            index += 1
            #print(index)
        try:
            choice = int(input())
        except:
            print("input was not a number")
        if choice in tempnums:
            return starterweapons[choice-1]
        else:
            print("invalid choice, try again")
            return Menu.starteritemselect()

class MainGame:
    def __init__():
        """empty"""
        
    def initialize():
        global score
        score = 0
        global pullenemydict 
        pullenemydict = {"minions": [{"goblin": ["goblin", "tbd", 1, 2, 65]}, 
                                    {"skeleton": ["skeleton", "tbd", 1, 2, 55]}, 
                                    {"locust": ["locust", "tbd", 1, 2, 35]}]}

    def playcycle():
        MainGame.initialize()
        global playercharacter
        while playercharacter.checklivingstate() == True:
            MainGame.rest()
            MainGame.combat()
        Maingame.endgame()
    
    def rest():
        global playercharacter
        """rest phase"""
        print("we are now in rest phase!\n")
        choice = int(input("what would you like to do?\n1. Check inventory\n 2. save\n 3. leave\n"))
        if choice == 1:
            MainGame.inspect(playercharacter)
            return MainGame.rest()
        elif choice == 2:
            MainGame.savegame()
            return MainGame.rest()
        elif choice == 3:
            return 0
        else:
            return MainGame.rest()
            
    
    def combat():
        global playercharacter
        
        """combat phase"""
        while playercharacter.checklivingstate() == True:
            enemylist = []
            enemylist.append(Entity(pullenemydict["minions"][2]["locust"][0],
                                    pullenemydict["minions"][2]["locust"][1],
                                    pullenemydict["minions"][2]["locust"][2],
                                    pullenemydict["minions"][2]["locust"][3],
                                    pullenemydict["minions"][2]["locust"][4]))
            enemylist[0].additem("loiter", Weapon('loiter', 'delivers warm hugs', 4, 9999))
                             
            print("we are now in combat phase!\n")
            choice = int(input("enemy ahead!\n what would you like to do?\n1. attack\n\n"))
            if choice == 1:
                tempnums = []
                index = 0
                choice = int(input("choose an enemy to attack"))
                for i in enemylist:
                    print(f"{index + 1}. {enemylist[index].name}")
                    tempnums.append(index + 1)
                    index += 1
                if choice in tempnums:
                    for i in playercharacter.inventory:
                        playercharacter.inventory[i].attack(playercharacter, enemylist[choice - 1])
                index = 0
                for i in enemylist:
                    enemylist[index].inventory['loiter'].attack(enemylist[index], playercharacter)
        
        
            
            
            
        

    # def rest_actions():
    #     """displays the actions the player can take during rest"""

    # def combat_actions():
    #     """displays the actions player can take during combat"""

    def inspect(entity):
        """tbd"""
        print(f"you have {entity.hitpoints} hit points remaining")
        for i in entity.inventory:
            print(entity.inventory[i].name)
            print(entity.inventory[i].desc)
            print(f"{entity.inventory[i].uses} uses until broken")
            print(f"{entity.inventory[i].damage} damage points")
        
    
    def endgame():
        global score
        print("game over!\n")
        print(f"you scored {score} points\n")
        print("Thanks for Playing!!! \n \n ======Credits======= \n \n Head Game Developer: Jeremy Esperanza \n Assistant Developer: Victor Flores")

    def savegame():
        """Saving Game Progress"""
        import json

        with open('last_save.json','w') as f:
            json.dumps(Entity,f)
            print("your game is now saved.")
        

            
        
    
        
        
            

        