import math

class constraintCalculations:
    
    def __init__(self,design):
        self.d = design
        
    def stallConstraint(self,vStall):
        wl = .5 * self.d.rho * vStall * vStall * self.d.ClMax
        return wl
        
    def handLaunchConstraint(self):
        print self.d.rho
        print self.d.ClMax
        print self.d.vHL
        wl = .5 * self.d.rho * self.d.ClMax * (self.d.vHL/1.2)**2
        
        return wl
    
    def maxSpeedConstraint(self,wl):
        k = 1.0 / (math.pi * self.d.AR * self.d.e)
        q = .5 * self.d.rho * self.d.vMax**2
        pl = (self.d.vMax /(self.d.etaP * self.d.etaM) * (q*self.d.cd0/wl + (k*wl)/q))
        return pl
    
    def turnConstraint(self,wl):
        k = 1.0 / (math.pi * self.d.AR * self.d.e)
        q = .5 * self.d.rho * self.d.vCruise**2
        pl = (self.d.vCruise / (self.d.etaP * self.d.etaM)) * (q*self.d.cd0/wl + self.d.N*self.d.N*(k*wl)/q)
        return pl
    
    def rateOfClimbConstraint(self,wl):
        cl = math.sqrt(3*self.d.cd0 * math.pi * self.d.AR * self.d.e)
        vMinPower = math.sqrt(2*wl/(self.d.rho * cl))
        pl = (1/(self.d.etaP*self.d.etaM)) * (self.d.RofC + vMinPower/(.866*self.d.LoDMax));
        return pl
    
    