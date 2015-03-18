from designInformation import designInformation
from fullFlightAnalysis2 import fullFlightAnalysis2

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

