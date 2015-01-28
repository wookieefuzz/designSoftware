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
#     New Inputs
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


# Derived Metrics
k = 1.0 / (math.pi * e * AR)
LDmax = .5 * sqrt(pi * e * AR/cd0)
vBR = ((2.0 * WS)/rho)*sqrt(k/cd0)
q = .5 * rho * vBR * vBR
LDc = WS / (cd0 * q + (k*WS*WS)/q) # Best L/D for cruise
t = t * 60 # convert to seconds
LDl = .866 * LDmax
vL2 =  math.sqrt((2*WS / rho)* sqrt(k/(3.0*cd0)))


# Calculate Weight Fractions per leg
wf_loiter = loiterCalc(vL,t,etaM,etaP,kBatt,LD)
wf_cruise = cruiseCalc(xBR, etaM, etaP, kBatt, LDc)
wf_turn = turnCalc(WS, rho, clmax, k, PW, etaM, etaP, cd0, turns, kBatt)

weightSheet.update_acell('H7',wf_loiter)
weightSheet.update_acell('H8',wf_cruise)
weightSheet.update_acell('H9',wf_turn)

wfT = wf_cruise + wf_loiter + wf_turn

W0 = Wpl / (1.0 - We - wfT)

W0kg = W0 / 9.81
W0lbs = W0kg * 2.2

weightSheet.update_acell('H4',W0kg)
weightSheet.update_acell('H5',W0lbs)



def loiterCalc(vL,t,etaM,etaP,kBatt,LD):
    weightFraction = (vL * t) / (etaM * etaP * kBatt * LD);
    return weightFraction

def cruiseCalc(range,etaM,etaP,kBatt,LDc):
    weightFraction = range / (etaM * etaP * kBatt * LDc);
    return weightFraction

def turnCalc(WS,rho,clmax,k,PW,etaM,etaP,cd0,theta,kBatt):
    g = 9.81;

    vT = 1.2 * sqrt(2.0 * WS / (rho * clmax));

    q = .5 * rho * vT^2.0;

    t1 = q / (k*WS);
    t2 = (PW * etaM * etaP) / vT;
    t3 = q*cd0/WS;

    n = sqrt(t1*(t2 -t3));

    weightFraction = (2 * math.pi * turns * PW * vT) / (kBatt * g * sqrt(n^2.0 - 1.0));