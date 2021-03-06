from designInformation import designInformation
from fullFlightAnalysis2 import fullFlightAnalysis2
from propulsionModel import propulsionModel
from motorModel import motorModel
from prop import prop

# get data from google sheets

# initialize the designInformation object
di = designInformation()

# this is the key to your google sheet with the design
key = '1VaA3NzB4G4Do0NKiGFiy7A_qtOEaNFX0gv_YeLks5cA'

# pull in each sheet required for what you want to work on
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

sheetName = 'Propulsion'
di.setLocalDataFromGoogleDrive(key,sheetName)

print '--------------------------------------------------------------------------------------------'

# Initialize Flight Analysis Class
# this also reads the config file to get the user name
fa = fullFlightAnalysis2()
fa.setGLkey('1Uxwy5lQZTLX-NRVn94INgPx9dlkMYfFr_SZ_be7Sovw')

# perform the hand launch analysis
fa.inclinedHandLaunchAnalysis(di,True,False)

print '--------------------------------------------------------------------------------------------'

# create the prop
propName = 'apce_14x12_geom.txt'
prop2 = prop()
prop2.setDinAolDeg(14,0.0)
prop2.getDataFromFile(propName)
print '--------------------------------------------------------------------------------------------'

# Motor Model Inputs
mm = motorModel(di.motorKv,di.motorRm,di.motorI0)

# create the propulsion model
pm = propulsionModel(prop2,mm)
fa.addPropulsionModel(pm)

# print basic performance figures
print '--------------------------------------------------------------------------------------------'
fa.printBasicPerformanceNumbers(di)
print '--------------------------------------------------------------------------------------------'

# perform the climb analysis
output1 = fa.climbAnalysisAdvanced(di,pm,True)

print '--------------------------------------------------------------------------------------------'

output2 = fa.cruiseForDistance(di,True)

print '--------------------------------------------------------------------------------------------'

output3 = fa.turnAnalysisR2(di,True)

print '--------------------------------------------------------------------------------------------'

totalEnergy = output1[0] + output2[0] + output3[0] 

print 'total energy consumed is ' +str(round(totalEnergy)) + ' J'
print 'aircraft capacity is ' +str(round(di.energyCapacity)) + ' J'

print '--------------------------------------------------------------------------------------------'
