import os
from datetime import datetime


class scraper:
    def __init__(self,key):
        self.key = key
        
        
        
    def checkForChanges(self):
        # check 
        return 1
        
    def makeAnnouncement(self):
        return 1
        
   
        
        
    def updateDataFile(self,dataVariable):
        file = open(dataVariable.name,'a')
        time = datetime.now()
        timeStr = time.isoformat()
        output = timeStr + "," + str(dataVariable.value) + "," + dataVariable.units + "\n"
        file.write(output)
        file.close()
        
    
        
    
    
    