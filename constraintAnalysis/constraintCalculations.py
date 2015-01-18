class constraintCalculations:
    
    def __init__(self,design):
        self.d = design
        
    def handLaunchConstraint(self):
        
        wl = .5 * d.rho * d.ClMax * (d.vHL/1.2)^2
        
        return wl