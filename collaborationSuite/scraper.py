import os
import csv
import StringIO
from datetime import datetime
import gspread
from dataVariable import dataVariable
from sendGroupMe import sendGroupMe
import re
from time import sleep

class scraper:
    def __init__(self,key):
        self.key = key
        
    def checkForChanges(self,key,sheetName, botID):
        gm = sendGroupMe(botID)
        print 'checking for changes'
        # get all data from the sheet
        dataVariables = self.getDataFromSheet(key, sheetName)
        
        for i in range(2,len(dataVariables)):
            sleep(.5)
            fname = dataVariables[i].name 
            #print fname
            isFile = os.path.isfile(fname)
            #print isFile
            #dataVariables[i].printInfo()
            
            if isFile:
                oldVal = self.getMostRecentValue(fname)
                #print oldVal
                newVal = dataVariables[i].value
                #print newVal
                
                if type(oldVal) == float:
                    newVal = float(newVal)
                    percentDifference = round(((newVal - oldVal) / oldVal) * 100.0,2)
                    print 'value ' + dataVariables[i].name + ' has changed by ' + str(percentDifference) + ' percent'
                    buf = 'value ' + dataVariables[i].name + ' has changed by ' + str(percentDifference) + ' percent'
                    if abs(percentDifference)>.01:
                        gm.sendText(buf)
                else:
                    print 'string detected'
                    if oldVal != newVal:
                         print 'value ' + dataVariables[i].name + ' has changed to ' + newVal
                         buf = 'value ' + dataVariables[i].name + ' has changed to ' + newVal
                         gm.sendText(buf)
            else:
                print 'variable ' + dataVariables[i].name + ' is new'
                
        return 1
        
    def makeAnnouncement(self):
        return 1
        
    def updateAllFiles(self,key,sheetName):
        dvList = self.getDataFromSheet(key, sheetName)
        for i in range(2,len(dvList)):
            dv = dvList[i]
            self.updateDataFile(dv)
        return 1
    
    def getMostRecentValue(self,name):
        value = self.readFile(name) 
        return value
        
    def readFile(self,name):
        file = open(name,'a+') # open for reading and writing
        content = file.readlines() # reads in all the content
        # print content
        #print len(content)
        lastLine = content[len(content)-1]
        value = self.parseDataFileLine(lastLine)
        
        m = re.search('[a-zA-Z]',value)
        
        file.close()
          
        if str(m) == 'None':
           return float(value)
        else:
            return value
        
        #print value
        #print lastLine
      
        
        
        
    def updateDataFile(self,dataVariable):
        file = open(dataVariable.name,'a')
        time = datetime.now()
        timeStr = time.isoformat()
        output = timeStr + "," + str(dataVariable.value) + "," + dataVariable.units + "\n"
        file.write(output)
        file.close()
        
    def parseDataFileLine(self,lineStr):
        data = lineStr.split(',')
        units = str(data[2])
        return data[1]
#         if units != 'string':
#             value = float(data[1])
#             return value
#         else:
#             print 'string detected'
#             return -10000.0
#         
        # print data
        # print value
        
    def getDataFromSheet(self,key,sheetName):
        # need the key to access the spreadsheet
        
        # log in the doc
        gc = gspread.login('designBuildFlyBot@gmail.com','designBuildFly')

        # pull down the sheets document
        file = gc.open_by_key(key)

        # open up the needed sheet
        sheet = file.worksheet(sheetName)
        
        allValues = sheet.get_all_values()
        
        numVariables = len(allValues)
        
        dataVariableList = []
        
        for i in range(0,numVariables):
            line = allValues[i]
            name = line[0]
            value = line[1]
            units = line[2]
            dvTemp = dataVariable(name,value,units)
            #dvTemp.printInfo()
            dataVariableList.append(dvTemp)
        
        return dataVariableList
        
            
        
        
        
    
        
    
    
    