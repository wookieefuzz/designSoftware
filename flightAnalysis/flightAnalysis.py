import math
class flightAnalysis:
    
    def __init__(self,name):
        self.name = name
        
    def steadyLevelFlight(self,v,aircraft):
        
        # solve for lift coefficient
        Cl = (2.0 * W) / (rho * v * v * S)
        
        # look up AoA
        # don't really need
        
        # calculate or look up Cd
        k = math.pi * e * AR
        Cd = Cd0 + (Cl * Cl)/k
        
        # solve for thrust
        T = .5 * rho * v * v * Cd * S
        
        # solve for power
        P = T * v
        
        
    
        