from aircraft import aircraft
from flightAnalysis import flightAnalysis
from fullFlightAnalysis import fullFlightAnalysis
import math

# a = aircraft()
# 
# a.rho = 1.22
# a.S = .792
# a.W = 38.04
# a.etaM = .85
# a.etaP = .6
# a.Cd0 = .05
# a.AR = 6.6
# a.e = .8
# 
# fa = flightAnalysis('first analysis')
# 
# v = 12.04
# 
# fa.steadyLevelFlight(v,a,True)

AR = 6.0
e = .85

S = 1.0 # 1 sq m of wing area
rho = 1.22
k = 1.0 / (math.pi * e * AR)
W = 9.81 * 8
Cl0 = .1
Cd0 = .05
v = 25.0
vc = 3.0

fa = fullFlightAnalysis()

alphaReqd = fa.climbAnalysis(rho,S,k,W,vc,v,Cl0,Cd0)

