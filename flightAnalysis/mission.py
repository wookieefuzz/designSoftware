class mission:
    
    def __init__(self):
        legList = []
        numLegs = 0
        
    def addTakeOff(self):
        self.numLegs += 1
        # requires density,runway length
        return 0.0
        
    def addHandLaunch(self,v0,height,density,tStatic):
        self.numLegs += 1
        return 0.0
    
    def addClimb(self,dToClimb,climbRate,climbSpeed):
        self.numLegs += 1
        return 0.0
        
    def addLevelFlight(self,v,rho):
        self.numLegs += 1
        return 0.0
        
    def addTurn(self):
        self.numLegs += 1
        return 0.0
        
        