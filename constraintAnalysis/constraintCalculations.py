class constraintCalculations:
    
    def __init__(self,design):
        self.d = design
        
    def handLaunchConstraint(self):
        
        wl = .5 * self.d.rho * self.d.ClMax * (self.d.vHL/1.2)**2
        
        return wl