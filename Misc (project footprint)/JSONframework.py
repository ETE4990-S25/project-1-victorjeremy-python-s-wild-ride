# Open JSON Function:
# 
import json
def openJSON (JSON1):
    
    """Writing JSON contents for game save"""

    with open(JSON1,'w') as f:

        #-----Write code here-----



        json.dumps(JSON1,f)

    

def readJSON(json_save):

    """Reading Saved JSON data; starting game based on save"""
    with open(json_save,'r') as f:
        #----Game Start----


        json.load(json_save,f)

    

        
        


