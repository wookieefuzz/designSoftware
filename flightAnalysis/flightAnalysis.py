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
        ampDraw = Pprop / ((11.1 + 12.6) / 2)
        
        if printBool:
            print 'required level flight Cl = ' + str(round(Cl,2)) 
            print 'required thrust in level flight = ' + str(round(T,2)) + ' N'
            print 'required power in level flight = ' + str(round(P,2)) + ' W'
            print 'given provided efficiencies, power input to propulsion system = ' + str(round(Pprop,2)) + ' W'
            print 'for an average 3S battery pack, current draw would be ' + str(round(ampDraw,2)) + ' A' 
            print 'ability will be added to run propulsion analysis to get more accurate efficiencies'
            
        
    
    