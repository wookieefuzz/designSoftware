# this will run the constraint analysis when data is pulled from Drive

# add desktop to path
import sys
import math
sys.path.append('/home/pi/')


# requires gspread, credentials (stored out of git repo), sys
import gspread
from credentials import credentials
from design import design
from constraintCalculations import constraintCalculations


# need the key to access the spreadsheet
key = '1zwxKF8RdbRgxticcIvfVJWEMampetnJd4rP4IvgjLmw'
c = credentials()

# log in the doc
gc = gspread.login(c.EMAIL,c.PW)

# pull down the sheets document
file = gc.open_by_key(key)

# open up the two needed sheets
designSheet = file.worksheet("Design")
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

# create the design
d = design(AR,e,rho,etaP,etaM,LoDMax,RofC,vCruise,cd0,N,vHL,vMax,ClMax)

# now actually create the constraints
# we will be using hand launch, max speed, turn, and rate of climb

cons = constraintCalculations(d)
wlHL = cons.handLaunchConstraint()
print wlHL
plMS = []
plTU = []
plRoC = []

WL = 0

# calculate all constraint curves (takeoff constraint = s0.0)
for iter in range(1,int(math.floor(wlHL))):
    WL += 1
    
    dataSheet.update_cell(iter+1,1,WL)
    dataSheet.update_cell(iter+1,1,WL)
    plMS.append(cons.maxSpeedConstraint(WL))
    dataSheet.update_cell(iter+1,2,cons.maxSpeedConstraint(WL))
    dataSheet.update_cell(iter+1,2,cons.maxSpeedConstraint(WL))
    plTU.append(cons.turnConstraint(WL))
    dataSheet.update_cell(iter+1,3,cons.turnConstraint(WL))
    dataSheet.update_cell(iter+1,3,cons.turnConstraint(WL))
    plRoC.append(cons.rateOfClimbConstraint(WL))
    dataSheet.update_cell(iter+1,4,cons.rateOfClimbConstraint(WL))
    dataSheet.update_cell(iter+1,4,cons.rateOfClimbConstraint(WL))
    dataSheet.update_cell(iter+1,5,0.0)



# set WL to wlHL
iter = int(math.floor(wlHL)) + 1
WL = wlHL
dataSheet.update_cell(iter+1,1,WL)
dataSheet.update_cell(iter+1,1,WL)
plMS.append(cons.maxSpeedConstraint(WL))
dataSheet.update_cell(iter+1,2,cons.maxSpeedConstraint(WL))
dataSheet.update_cell(iter+1,2,cons.maxSpeedConstraint(WL))
plTU.append(cons.turnConstraint(WL))
dataSheet.update_cell(iter+1,3,cons.turnConstraint(WL))
dataSheet.update_cell(iter+1,3,cons.turnConstraint(WL))
plRoC.append(cons.rateOfClimbConstraint(WL))
dataSheet.update_cell(iter+1,4,cons.rateOfClimbConstraint(WL))
dataSheet.update_cell(iter+1,4,cons.rateOfClimbConstraint(WL))
dataSheet.update_cell(iter+1,5,0.0)

# set WL to wlHL + .001
iter = int(math.floor(wlHL)) + 2
WL = wlHL+.001
dataSheet.update_cell(iter+1,1,WL)
dataSheet.update_cell(iter+1,1,WL)
plMS.append(cons.maxSpeedConstraint(WL))
dataSheet.update_cell(iter+1,2,cons.maxSpeedConstraint(WL))
dataSheet.update_cell(iter+1,2,cons.maxSpeedConstraint(WL))
plTU.append(cons.turnConstraint(WL))
dataSheet.update_cell(iter+1,3,cons.turnConstraint(WL))
dataSheet.update_cell(iter+1,3,cons.turnConstraint(WL))
plRoC.append(cons.rateOfClimbConstraint(WL))
dataSheet.update_cell(iter+1,4,cons.rateOfClimbConstraint(WL))
dataSheet.update_cell(iter+1,4,cons.rateOfClimbConstraint(WL))
dataSheet.update_cell(iter+1,5,40.0)

# calculate all constraint curves (setting hand launch to 40)
WL = math.floor(wlHL)
for iter in range(int(math.floor(wlHL))+3,101):
    WL += 1
    
    dataSheet.update_cell(iter+1,1,WL)
    dataSheet.update_cell(iter+1,1,WL)
    plMS.append(cons.maxSpeedConstraint(WL))
    dataSheet.update_cell(iter+1,2,cons.maxSpeedConstraint(WL))
    dataSheet.update_cell(iter+1,2,cons.maxSpeedConstraint(WL))
    plTU.append(cons.turnConstraint(WL))
    dataSheet.update_cell(iter+1,3,cons.turnConstraint(WL))
    dataSheet.update_cell(iter+1,3,cons.turnConstraint(WL))
    plRoC.append(cons.rateOfClimbConstraint(WL))
    dataSheet.update_cell(iter+1,4,cons.rateOfClimbConstraint(WL))
    dataSheet.update_cell(iter+1,4,cons.rateOfClimbConstraint(WL))
    dataSheet.update_cell(iter+1,5,40.0)
        