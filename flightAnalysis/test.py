from aircraft import aircraft
from flightAnalysis import flightAnalysis

a = aircraft()

a.rho = 1.22
a.S = .792
a.W = 38.04
a.etaM = .85
a.etaP = .6
a.Cd0 = .05
a.AR = 6.6
a.e = .8

fa = flightAnalysis('first analysis')

v = 12.04

fa.steadyLevelFlight(v,a,True)