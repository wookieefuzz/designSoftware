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

fa = fullFlightAnalysis()

alphaReqd = fa.climbAnalysis(rho,S,k,W,vc,v,Cl0,Cd0)

# specific hand launch variables
v0 = 10.0 # m/s
Clmax = 1.0
Tstatic = 50.0 #2.0*9.81
height = 20.0
tMax = 10.0
printBool = True
stepPrintBool = True

print '----------------------------------------------------'
fa.handLaunchAnalysis(S,W,rho,v0,Cl0,Cd0,Clmax,k,height,Tstatic,tMax,printBool,stepPrintBool)