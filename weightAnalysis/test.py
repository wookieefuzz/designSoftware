import math

e = .8
AR = 8
WS = 70
PW = 10
Cd0 = .04
etaM = .85
etaP = .52
cruiseDist = 15000
kBatt = 47716
rho = 1.22

k = 1 / (math.pi * e * AR)

# Cruise calculations
#vBestRange = (2.0 * WS / rho) * math.sqrt(k/Cd0) WRONG
vBestRange = math.sqrt((2*WS)/(rho*math.sqrt(Cd0/k)))
q = 0.5 * rho * vBestRange * vBestRange
LDc = WS / ((Cd0 * q)+(k*WS*WS)/q)
wfCruise = cruiseDist / (etaM*etaP*kBatt*LDc)

print "best range cruise speed is %g m/s" % (vBestRange)
print "best range L/D is %g" % (LDc)
print "weight fraction for cruise is %g percent" % (wfCruise*100.0)
