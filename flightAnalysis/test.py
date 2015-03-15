from aircraft import aircraft
from flightAnalysis import flightAnalysis
from fullFlightAnalysis import fullFlightAnalysis
import math

a = aircraft()
 
a.rho = 1.22
a.S = .792
a.W = 38.04
a.etaM = .85
a.etaP = .6
a.Cd0 = .05
a.AR = 6.6
a.e = .8

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

pitch = 7.0
dia = 9.0
rpm = 21.0e3

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

climbPrintBool = True
printBool = True
stepPrintBoolHL = False
stepPrintBoolIHL = False
stallPrintBool = True
approachPrintBool = True
thrustPrintBool = True
turnPrintBool = True

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