# this will run the constraint analysis when data is pulled from Drive

# add desktop to path
import sys
import math
sys.path.append('/home/pi/')


# requires gspread, credentials (stored out of git repo), sys
import gspread
from credentials import credentials
#from design import design
#from constraintCalculations import constraintCalculations
import time


# need the key to access the spreadsheet
key = '1zwxKF8RdbRgxticcIvfVJWEMampetnJd4rP4IvgjLmw'
c = credentials()

# log in the doc
gc = gspread.login(c.EMAIL,c.PW)

# pull down the sheets document
file = gc.open_by_key(key)

# open up the needed sheet
weightSheet = file.worksheet("WeightAnalysis")

# now go through and find the needed data
cell = weightSheet.find("AR")
print cell
AR = weightSheet.cell(cell.row,2).value
print AR

cell = weightSheet.find("e")
print cell
e = weightSheet.cell(cell.row,2).value
print e

cell = weightSheet.find("rho")
print cell
rho = weightSheet.cell(cell.row,2).value
print rho   

cell = weightSheet.find("etaP")
etaP = weightSheet.cell(cell.row,2).value
print etaP

cell = weightSheet.find("etaM")
etaM = weightSheet.cell(cell.row,2).value
print etaM  

cell = weightSheet.find("LoDMax")
LoDMax = weightSheet.cell(cell.row,2).value
print LoDMax

cell = weightSheet.find("RofC")
RofC = weightSheet.cell(cell.row,2).value
print RofC

cell = weightSheet.find("vCruise")
vCruise = weightSheet.cell(cell.row,2).value
print vCruise

cell = weightSheet.find("cd0")
cd0 = weightSheet.cell(cell.row,2).value
print cd0

cell = weightSheet.find("N")
N = weightSheet.cell(cell.row,2).value
print N

cell = weightSheet.find("vHL")
vHL = weightSheet.cell(cell.row,2).value
print vHL

cell = weightSheet.find("vMax")
vMax = weightSheet.cell(cell.row,2).value
print vMax

cell = weightSheet.find("ClMax")
ClMax = weightSheet.cell(cell.row,2).value
print ClMax

#-------------------------------------------


cell = weightSheet.find("turns")
turns = weightSheet.cell(cell.row,2).value
print turns  

cell = weightSheet.find("W/S")
WS = weightSheet.cell(cell.row,2).value
print WS

cell = weightSheet.find("P/W")
PW = weightSheet.cell(cell.row,2).value
print PW 

cell = weightSheet.find("WeW0")
WeW0 = weightSheet.cell(cell.row,2).value
print WeW0

cell = weightSheet.find("Wpl")
Wpl = weightSheet.cell(cell.row,2).value
print Wpl

cell = weightSheet.find("kBatt")
kBatt = weightSheet.cell(cell.row,2).value
print kBatt

cell = weightSheet.find("cruiseRange")
xBR = weightSheet.cell(cell.row,2).value
print xBR

cell = weightSheet.find("loiterTime")
t = weightSheet.cell(cell.row,2).value
print t

cell = weightSheet.find("loiterSpeed")
vL = weightSheet.cell(cell.row,2).value
print vL


# create the design
#d = design(AR,e,rho,etaP,etaM,LoDMax,RofC,vCruise,cd0,N,vHL,vMax,ClMax)
