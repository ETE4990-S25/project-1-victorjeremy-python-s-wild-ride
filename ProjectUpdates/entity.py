class Entity:
    def __init__(self, name, description, inventory, team, hitpoints,):
        """establish all the parameters of an entity, playable or not"""
        self.name = name
        self.description = description
        self.inventory = inventory
        self.team = team
        self.hitpoints = hitpoints

    def Create():
        """create an entity with user input"""
        name = input("add name")
        description = input("add description")
        inventory = {}
        team = int(input("set team number"))
        hitpoints = int(input("set hitpoints"))
        return entity(name, description, inventory, team, hitpoints)

    def addItem (item):
        """empty"""