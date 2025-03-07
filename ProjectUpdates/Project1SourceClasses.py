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
        #boolean return meant to be used in other functions
        #this function is for preventing someone from doing something if they are dead
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
        #this function is for preventing hurting someone on the same team
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
        #function used to check if an item still has uses
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
    def __init__(self, name, desc, uses, damage):
        """child of item, introduces damage"""
        super().__init__(name, desc, uses)
    
        self.damage = damage

        
    def attack(self, user, target):
        #this function uses functions from two different clases :skull:
        """attacks with the weapon: requires arguments 'user' and 'target' """
        print(f"{user.name} attacks {target.name} with {self.name}!")
        if self.checkconsume() & target.state & user.checkteam(target) == True:
        #self.checkconsume() - function in the Item class. returns bool checking if an item can be consumed
        #target.state() - function in the Entity class. returns bool. False = dead, True = alive
        #user.checkteam(target) - function in the Entity class. returns true if target is not on the same team
        # if all([self.checkconsume(),target.state(),user.checkteam(target)]) == True:
            try:
                self.consume()
                target.hurt(self.damage)
                if target.state == False:
                    print(f'{target.name} is dead')
                else:
                    print(f'{target.name} takes {self.damage} damage.')
                #self.consume() - function in the Item class. 
                #target.hurt(argument) - function in the Entity class. subtracts argument from hitpoints
                #self.damage() - parameter in the Weapon class - damage of the weapon
                # in this code block:
                # before attacking, check if item can be consumed, target is alive, and target is on another team
                # consume 1 item use and apply damagw
            except:
                print("erm")
        else:
            print("impossible")
            
#end of Weapon subclass
        