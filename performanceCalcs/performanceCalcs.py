import math

Cd0
WS
rho
e
AR
ClMax
vTurn
n

vMinSink =  (4.0 * math.sqrt(2.0)*math.pow(Cd0, .25)) * math.sqrt(WS / rho)
vBestGlideRange = (math.sqrt(2.0) / math.pow(math.pi*e*AR*Cd0,.25))*math.sqrt(WS / rho)
vMin = math.sqrt(2.0/ClMax) * math.sqrt(WS / rho)
rTurn = (vTurn**2) / (g*math.sqrt(n**2 - 1.0)) # if you know v and n
# given a radius and a speed, solve for load factor
n = math.sqrt(((vTurn**2 / (rTurn * g))**2)+1)

