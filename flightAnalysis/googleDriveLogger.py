import gspread
from time import gmtime,strftime

class googleDriveLogger:
    
    def __init__(self,key):
        self.key = key
        
    
    def appendToLog(self,textString):
        timeStr = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print timeStr
        print textString
    
        # log in to the doc
        gc = gspread.login('designBuildFlyBot@gmail.com','designBuildFly')

        # pull down the sheets document
        file = gc.open_by_key(self.key)

        # open up the needed sheet
        sheet = file.sheet1
        
        # find how many entries there are
        allValues = sheet.get_all_values()
        numVariables = len(allValues)
        
        row = numVariables + 1
        
        sheet.update_cell(row,1,timeStr)
        sheet.update_cell(row,2,textString) 
       
       
    def appendUserAnalysisMessage(self,userName,analysisString):
        textString = userName + ' has just run ' + analysisString
        self.appendToLog(textString)
        