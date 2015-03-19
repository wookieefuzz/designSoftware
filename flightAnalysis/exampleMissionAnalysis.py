from designInformation import designInformation
from fullFlightAnalysis2 import fullFlightAnalysis2
from propulsionModel import propulsionModel
from motorModel import motorModel
from prop import prop

# get dat from google sheets
di = designInformation()
key = '1VaA3NzB4G4Do0NKiGFiy7A_qtOEaNFX0gv_YeLks5cA'

sheetName = 'BasicAircraftProperties'
di.setLocalDataFromGoogleDrive(key,sheetName)

sheetName = 'HandLaunch'
di.setLocalDataFromGoogleDrive(key,sheetName)

sheetName = 'Climb'
di.setLocalDataFromGoogleDrive(key,sheetName)

sheetName = 'Cruise'
di.setLocalDataFromGoogleDrive(key,sheetName)

sheetName = 'Turns'
di.setLocalDataFromGoogleDrive(key,sheetName)

print '--------------------------------------------------------------------------------------------'

# Initialize Flight Analysis Class
fa = fullFlightAnalysis2()

# perform the hand launch analysis
fa.inclinedHandLaunchAnalysis(di,True,False)

print '--------------------------------------------------------------------------------------------'

# create the prop
propName = 'apce_11x10_geom.txt'
prop2 = prop()
prop2.setDinAolDeg(11.0,-2.7)
[Din,x,cR,beta,aoldeg] = prop2.getDataFromFile(propName)

# Motor Model Inputs
# Kv = 660.0
# I0 = 2.0
# rm = .041
Kv = 380.0
I0 = .5
rm = .225
mm = motorModel(Kv,rm,I0)

# create the propulsion model
pm = propulsionModel(prop2,mm)
fa.addPropulsionModel(pm)
# perform the climb analysis
fa.climbAnalysisAdvanced(di,pm,True)

print '--------------------------------------------------------------------------------------------'

fa.cruiseForDistance(di,True)

print '--------------------------------------------------------------------------------------------'
