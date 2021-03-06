# this will run the constraint analysis when data is pulled from Drive

sheetName = 'WeightAnalysisElectricAirplane'
#sheetName = 'WeightAnalysis'

# add desktop to path
import math

# requires gspread, credentials (stored out of git repo), sys
import gspread
#from design import design
#from constraintCalculations import constraintCalculations
import time

import json
from oauth2client.client import SignedJwtAssertionCredentials


# need the key to access the spreadsheet
key = '1zwxKF8RdbRgxticcIvfVJWEMampetnJd4rP4IvgjLmw'
json_key = json.load(open('EliO.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

def loiterCalc(vL,t,etaM,etaP,kBatt,LD):
    weightFraction = (vL * t) / (etaM * etaP * kBatt * LD)
    return weightFraction

def cruiseCalc(range,etaM,etaP,kBatt,LDc):
    weightFraction = range / (etaM * etaP * kBatt * LDc)
    return weightFraction

def turnCalc(WS,rho,clmax,k,PW,etaM,etaP,cd0,turns,kBatt):
    g = 9.81

    vT = 1.2 * math.sqrt(2.0 * WS / (rho * clmax))

    q = .5 * rho * vT * vT

    t1 = q / (k*WS)
    t2 = (PW * etaM * etaP) / vT
    t3 = q*cd0/WS

    n = math.sqrt(t1*(t2 -t3))

    weightFraction = (2 * math.pi * turns * PW * vT) / (kBatt * g * math.sqrt(n * n - 1.0))
    return weightFraction



# pull down the sheets document
file = gc.open_by_key(key)

# open up the needed sheet
weightSheet = file.worksheet(sheetName)


valList = weightSheet.col_values(2)
AR = float(valList[1])
e = float(valList[2])
rho = float(valList[3])
etaP = float(valList[4])
etaM =float(valList[5])
LoDMax = float(valList[6])
RofC = float(valList[7])
vCruise = float(valList[8])
cd0 = float(valList[9])
N = float(valList[10])
vHL = float(valList[11])
vMax = float(valList[12])
ClMax = float(valList[13])
#-------------------------------------------
#     New Inputs
#-------------------------------------------
turns = float(valList[14])
WS = float(valList[15])
PW = float(valList[16])
WeW0 = float(valList[17])
Wpl = float(valList[18])
kBatt = float(valList[19])
xBR = float(valList[20])
t = float(valList[21])

# Derived Metrics
k = 1.0 / (math.pi * e * AR)
LDmax = .5 * math.sqrt(math.pi * e * AR/cd0)
# vBR = ((2.0 * WS)/rho)*math.sqrt(k/cd0) #THIS IS WRONG!
vBR = math.sqrt((2*WS)/(rho*math.sqrt(cd0/k)))
cruiseTime = (xBR / vBR)/60.0
q = .5 * rho * vBR * vBR
LDc = WS / (cd0 * q + (k*WS*WS)/q) # Best L/D for cruise
t = t * 60 # convert to seconds
LDl = .866 * LDmax
vL2 =  math.sqrt((2*WS / rho)* math.sqrt(k/(3.0*cd0)))

buff = "Best range cruise speed is %g\n" %vBR
print buff
buff = "Best range L/D is %g\n" %LDc
print buff
buff = "Best loiter speed is %g\n" %vL2
print buff



# Calculate Weight Fractions per leg
wf_loiter = loiterCalc(vL2,t,etaM,etaP,kBatt,LDl)
print wf_loiter
wf_cruise = cruiseCalc(xBR, etaM, etaP, kBatt, LDc)
print wf_cruise
wf_turn = turnCalc(WS, rho, ClMax, k, PW, etaM, etaP, cd0, turns, kBatt)
print wf_turn

weightSheet.update_acell('H7',wf_loiter)
weightSheet.update_acell('H8',wf_cruise)
weightSheet.update_acell('H9',wf_turn)

wfT = wf_cruise + wf_loiter + wf_turn

W0 = (Wpl * 9.81) / (1.0 - WeW0 - wfT)

W0kg = W0 / 9.81
W0lbs = W0kg * 2.2

weightSheet.update_acell('H4',W0kg)
weightSheet.update_acell('H5',W0lbs)

emptyWeightKg = WeW0 * W0kg
battWeightKg = wfT * W0kg
payloadWeightKg = Wpl

emptyWeightLbs = emptyWeightKg * 2.2
battWeightLbs = battWeightKg * 2.2
payloadWeightLbs = payloadWeightKg * 2.2

weightSheet.update_acell('H11',emptyWeightKg)
weightSheet.update_acell('H12',battWeightKg)
weightSheet.update_acell('H13',payloadWeightKg)

weightSheet.update_acell('H15',emptyWeightLbs)
weightSheet.update_acell('H16',battWeightLbs)
weightSheet.update_acell('H17',payloadWeightLbs)

weightSheet.update_acell('H19',cruiseTime)

