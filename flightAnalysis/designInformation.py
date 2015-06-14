import gspread
from dataVariable import dataVariable

import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


class designInformation:
    
    def __init__(self):
        
        print 'design initialized'
        
        self.S = 0.0
        self.AR = 0.0
        self.b = 0.0
        self.e = 0.0
        self.k = 0.0
        self.m = 0.0
        self.ClMax = 0.0
        self.Cl0 = 0.0
        self.Cd0 = 0.0
        self.W = 0.0
        
        self.vClimb = 0.0
        self.vertRate = 0.0
        self.startAlt = 0.0
        self.endAlt = 0.0
        
        self.vCruise = 0.0
        self.cruiseDist = 0.0
        self.cruiseAlt = 0.0
        
        self.bankAngle = 0.0
        self.turnRadius = 0.0
        self.turnAlt = 0.0
        self.vTurn = 0.0
        self.turnAngle = 0.0
        self.numTurns = 0.0
        
        self.altHL = 0.0
        self.theta = 0.0
        self.thetaFinal = 0.0
        self.pushOverTime = 0.0
        self.throwSpeed = 0.0
        self.simTime = 0.0
        self.height = 0.0
        self.thrustCurveFitType = 'linear'
        
        self.staticThrust = 0.0
        self.zeroThrustSpeed = 0.0
        
        self.batteryWeight = 0.0
        self.batteryKvalue = 0.0
        self.motorKv = 0.0
        self.motorI0 = 0.0
        self.motorRm = 0.0
        self.energyCapacity = 0.0
        
        # bools for print statements
        self.climbPrintBool = False
        self.printBool = False
        self.stepPrintBoolHL = False
        self.stepPrintBoolIHL = False
        self.stallPrintBool = False
        self.approachPrintBool = False
        self.thrustPrintBool = False
        self.turnPrintBool = False
        self.motorPrintBool = False
        self.levelFlightPrintBool = False
        
#         d = vars(self)
#         
#         print d
#         
#         for key in d:
#             print key, 'corresponds to', d[key]
        
    def getDataFromSheet(self,key,sheetName):
        # need the key to access the spreadsheet
            
        # log in to the doc
        #gc = gspread.login('designBuildFlyBot@gmail.com','designBuildFly')
        
        json_key = json.load(open('CollaborativeDesignTools-e8338927dc2b.json'))
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
        gc = gspread.authorize(credentials)
        
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
        
        self.designVariables = dataVariableList
        
        return dataVariableList
    
    def setLocalDataFromGoogleDrive(self,key,sheetName):
        # loop through the dataVariable List
        # loop through the keys in the dict
        
        designVariables = self.getDataFromSheet(key, sheetName)
        
        d = vars(self)
                
        for dv in self.designVariables:
            for key in d:
                if key == dv.name:
                    #print 'we have a match!'
                    print 'key was ' + key 
                    print 'data variable was ' + dv.name
                    if dv.units == 'string':
                        d[key] = dv.value
                    else:
                        d[key] = float(dv.value)
                    print 'value has been set to ' + str(d[key])
                   
                    
                    
                    
                
                    