from flightAnalysis import flightAnalysis
from fullFlightAnalysis import fullFlightAnalysis
from motorModel import motorModel
from prop import prop
from propulsionModel import propulsionModel
import math

# fa = flightAnalysis('first analysis')
# 
# v = 12.04
# 
# fa.steadyLevelFlight(v,a,True)

AR = 6
e = .7

S = .3524 # 1 sq m of wing area
rho = 1.22
k = 1.0 / (math.pi * e * AR)
W = 9.81 * 4.55
Cl0 = .05
Cd0 = .04
v = 25.0
vc = 5.0

vCruise = 25.0

pitch = 7.0
dia = 11.0
rpm = 15000

fa = fullFlightAnalysis()

# turn variables
phi = 30.0 / (180.0/math.pi)
R = 100.0

# specific hand launch variables
theta = 30.0 / (180.0 / math.pi)
thetaFinal = 0.0
pushOverTime = 5.0
v0 = 6.7 # m/s
Clmax = 0.7
Tstatic = 50.0 
height = 2.0
tMax = 7.0
zeroThrustSpeed = 75.0
fitType = 'linear'

# Motor Model Inputs
# based on Axi 2808/24
Kv = 660.0
I0 = 2.0
rm = .041
mm = motorModel(Kv,rm,I0)
RPM = 10500.0
vin = 4.2 * 4.0

climbPrintBool = True
printBool = True
stepPrintBoolHL = False
stepPrintBoolIHL = False
stallPrintBool = True
approachPrintBool = True
thrustPrintBool = True
turnPrintBool = True
motorPrintBool = True
levelFlightPrintBool = True

alphaReqd = fa.climbAnalysis(rho,S,k,W,vc,v,Cl0,Cd0,climbPrintBool)
print '----------------------------------------------------'
fa.handLaunchAnalysis(S,W,rho,v0,Cl0,Cd0,Clmax,k,height,Tstatic,tMax,printBool,stepPrintBoolHL)
print '----------------------------------------------------'
fa.inclinedHandLaunchAnalysis(S,W,rho,v0,Cl0,Cd0,Clmax,k,height,Tstatic,tMax,printBool,stepPrintBoolIHL,theta,zeroThrustSpeed,fitType,thetaFinal,pushOverTime)
print '----------------------------------------------------'
fa.solveForStallSpeed(W,S,Clmax,rho,stallPrintBool)
print '----------------------------------------------------'
fa.solveForApproachSpeed(W,S,Clmax,rho,approachPrintBool)
print '----------------------------------------------------'
fa.solveForStaticThrust(pitch,dia,rpm,thrustPrintBool)
print '----------------------------------------------------'
fa.turnAnalysisPhi(S,W,rho,v,phi,Clmax,k,Cd0,turnPrintBool)
print '----------------------------------------------------'
fa.turnAnalysisR(S,W,rho,v,R,Clmax,k,Cd0,turnPrintBool)
print '----------------------------------------------------'
mm.simulateAtRPM(vin,RPM,printBool)
print '----------------------------------------------------'
p = prop()
pm = propulsionModel(p,mm)
pm.operateAtAirspeedWithThrust(25.0,15.0,10000,18000,0.0)
print '----------------------------------------------------'
print k
TlevelFlight = fa.steadyLevelFlight(W,S,vCruise,rho,k,Cd0,levelFlightPrintBool)
#output = [Ct, Cp, eta,T,Pwatt,torqueNM,RPM]
output = pm.operateAtAirspeedWithThrust(25.0,TlevelFlight,10000,17000,0.0)
print output


