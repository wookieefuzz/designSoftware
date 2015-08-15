# this will run the constraint analysis when data is pulled from Drive

# add desktop to path
import sys
import math

# requires gspread, credentials (stored out of git repo), sys
import gspread
#from credentials import credentials
from design import design
from constraintCalculations import constraintCalculations
import time

import json
from oauth2client.client import SignedJwtAssertionCredentials


# need the key to access the spreadsheet
key = '1zwxKF8RdbRgxticcIvfVJWEMampetnJd4rP4IvgjLmw' # demo sheet
json_key = json.load(open('EliO.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)
#shts = gc.open_by_key(key)

# pull down the sheets document
file = gc.open_by_key(key)

# open up the two needed sheets
designSheet = file.worksheet("Design")
#designSheet = file.worksheet("ElectricAirplane")

dataSheet = file.worksheet("Data")

# now go through and find the needed data
cell = designSheet.find("AR")
AR = designSheet.cell(cell.row,2).value
print AR

cell = designSheet.find("e")
e = designSheet.cell(cell.row,2).value
print e

cell = designSheet.find("rho")
rho = designSheet.cell(cell.row,2).value
print rho   

cell = designSheet.find("etaP")
etaP = designSheet.cell(cell.row,2).value
print etaP

cell = designSheet.find("etaM")
etaM = designSheet.cell(cell.row,2).value
print etaM  

cell = designSheet.find("LoDMax")
LoDMax = designSheet.cell(cell.row,2).value
print LoDMax

cell = designSheet.find("RofC")
RofC = designSheet.cell(cell.row,2).value
print RofC

cell = designSheet.find("vCruise")
vCruise = designSheet.cell(cell.row,2).value
print vCruise

cell = designSheet.find("cd0")
cd0 = designSheet.cell(cell.row,2).value
print cd0

cell = designSheet.find("N")
N = designSheet.cell(cell.row,2).value
print N

cell = designSheet.find("vHL")
vHL = designSheet.cell(cell.row,2).value
print vHL

cell = designSheet.find("vMax")
vMax = designSheet.cell(cell.row,2).value
print vMax

cell = designSheet.find("ClMax")
ClMax = designSheet.cell(cell.row,2).value
print ClMax

cell = designSheet.find("maxWS")
maxWS = float(designSheet.cell(cell.row,2).value)
print maxWS

cell = designSheet.find("stallSpeed")
stallSpeed = float(designSheet.cell(cell.row,2).value)
print stallSpeed

#----------------------------------------------------------------------

# create the design
d = design(AR,e,rho,etaP,etaM,LoDMax,RofC,vCruise,cd0,N,vHL,vMax,ClMax)

# now actually create the constraints
# we will be using hand launch, max speed, turn, and rate of climb

cons = constraintCalculations(d)
wlHL = cons.handLaunchConstraint()
wlStall = cons.stallConstraint(stallSpeed)
print wlHL
plMS = []
plTU = []
plRoC = []
wlList = []
plHL = []

stepSize = maxWS / 100.0

WL = stepSize

cellList = dataSheet.range('A2:E100')

print 'started processing at:'
print time.strftime("%H:%M:%S")

maxVal = 0.0

#----------------------------------------------------------------------


while (WL < maxWS):

    wlList.append(WL)
    plMS.append(cons.maxSpeedConstraint(WL))
    plTU.append(cons.turnConstraint(WL))
    plRoC.append(cons.rateOfClimbConstraint(WL))
    maxVal = max([maxVal, cons.maxSpeedConstraint(WL), cons.turnConstraint(WL), cons.rateOfClimbConstraint(WL)])
    WL += stepSize
 
WL = stepSize
while (WL < maxWS):
    if (WL<wlStall):
        plHL.append(0.0)
    else:
        plHL.append(maxVal)
    WL += stepSize
    
    
for cell in cellList:
    print cell.row
    print cell.col
    if cell.col == 1:
        cell.value = wlList[cell.row-2]
    elif cell.col == 2:
        cell.value = plMS[cell.row-2]
    elif cell.col == 3:
        cell.value = plTU[cell.row-2]
    elif cell.col == 4:
        cell.value = plRoC[cell.row-2]
    elif cell.col == 5: 
        cell.value = plHL[cell.row-2]

print 'finished processing at:'
print time.strftime("%H:%M:%S")

print 'started upload at:'
print time.strftime("%H:%M:%S")
dataSheet.update_cells(cellList)
print 'finished upload at:'
print time.strftime("%H:%M:%S")