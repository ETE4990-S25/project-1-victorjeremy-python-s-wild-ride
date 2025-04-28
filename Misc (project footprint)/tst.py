import json

class gamestates:
    #gamestates include combat, noncombat
    def gamecycle(gamestate):
        state = gamestate
        if state == 0: #menu
            print("==== Start Menu ====")

            try:
                print("Loading previous game...")
                
            except:
                print("problem with menu")
        if state == 1: #noncombat phase
            try:
                print("nc")
            except:
                print("problem with noncombat phase")
        if state == 2: #combat phase
            try:
                print("c")
            except:
                print("problem with combat phase")



class json_save_n_load (gamestates):
    """Establishing game persistence"""
    super.gamecycle(gamestate)

    def __init__(self,game_file):
        self.game_file = game_file
        

    def SaveGame(self,gamedata):
        with open(self.game_file,'w') as f:
            json.dump(gamedata,f)
            print (f"saved to {self.game_file}. Thanks for Playing!!")
    def LoadGame(self):
        try:
            with open(self.game_file,'r') as f:
                persistence = json.load(f)
            print (f"loading {self.game_file}...")
            return persistence
        except FileNotFoundError:
            print ("No File Found :(")
            return None