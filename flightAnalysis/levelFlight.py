from missionLeg import missionLeg

class levelFlight(missionLeg):
    
    def __init__(self,name,distance,speed,density):
        self.name = name
        self.distance = distance
        self.speed = speed
        self.density = density 
        self.time = distance / speed