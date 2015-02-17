import math
class flightAnalysis:
    
    def __init__(self,name):
        self.name = name
        
    def steadyLevelFlight(self,v,aircraft,printBool):
        
        a = aircraft
        
        # solve for lift coefficient
        Cl = (2.0 * a.W) / (a.rho * v * v * a.S)
        
        # look up AoA
        # don't really need, make an approximation that thrust and drag are opposite eachother
        
        # calculate or look up Cd
        k = math.pi * a.e * a.AR
        Cd = a.Cd0 + (Cl * Cl)/k
        
        # solve for thrust
        T = .5 * a.rho * v * v * Cd * a.S
        
        # solve for power
        P = T * v
        
        Pprop = P / (a.etaM * a.etaP)
        
        if printBool:
            print 'required level flight Cl = ' + str(Cl) 
            print 'required thrust in level flight = ' + str(T) + ' N'
            print 'required power in level flight = ' + str(P) + ' W'
            print 'given provided efficiencies, power input to propulsion system = ' + str(Pprop) + ' W'
            print 'ability will be added to run propulsion analysis to get more accurate efficiencies'
            
        
    
        