import os
import csv
import StringIO
from datetime import datetime
import gspread
from dataVariable import dataVariable

class scraper:
    def __init__(self,key):
        self.key = key
        
    def checkForChanges(self,key,sheetName):
        print 'checking for changes'
        # get all data from the sheet
        dataVariables = self.getDataFromSheet(key, sheetName)
        
        for i in range(0,len(dataVariables)):
            fname = dataVariables[i].name 
            #print fname
            isFile = os.path.isfile(fname)
            #print isFile
            #dataVariables[i].printInfo()
            
            if isFile:
                oldVal = self.getMostRecentValue(fname)
                #print oldVal
                newVal = float(dataVariables[i].value)
                #print newVal
                percentDifference = ((newVal - oldVal) / oldVal) * 100.0
                print 'value of ' + dataVariables[i].name + ' has changed by ' + str(percentDifference) + '%'
            else:
                print 'variable is new'
        
        # check for existence of variable
        
        
        # get most recently stored variable
        # get value from file
        # calculate percent change
        return 1
        
    def makeAnnouncement(self):
        return 1
        
        
    def getMostRecentValue(self,name):
        value = self.readFile(name) 
        return float(value)
        
    def readFile(self,name):
        file = open(name,'a+') # open for reading and writing
        content = file.readlines() # reads in all the content
        # print content
        #print len(content)
        lastLine = content[len(content)-1]
        value = self.parseDataFileLine(lastLine)
        #print value
        #print lastLine
        file.close()
        return float(value)
        
        
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
        if units != 'string':
            value = float(data[1])
            return value
        else:
            print 'string detected'
            return -10000.0
        
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
        
            
        
        
        
    
        
    
    
    