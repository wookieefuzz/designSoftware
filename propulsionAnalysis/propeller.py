import math

class propeller:
    
    def __init__(self,pitch,dia,station,chord,twist,B):
        self.pitch = pitch
        self.dia = dia
        self.station = station
        self.chord = chord
        self.twist = twist
        self.numBlades = B
        
    def goldstein(self,prop,RPM,Vfps,rho,aoldeg,beta0deg,a,Cd0,k,beta1deg):
        D = self.dia / 12.0 # diameter in feet
        R = D / 2.0 # radius in feet
        n = RPM / 60.0 # angular speed in Hz
        omega = 2.0 * math.pi * n # rad/sec
        Vt = omega * R # tip speed
        Lambda = V / Vt # ratio of forward speed to tip speed
        r2d = 180.0 / math.pi # radians to degrees
        J = V / (n * D) # advance ratio
        
        
        
        beta = (beta1deg + aoldeg) / r2d
        
        sigma = self.numBlades / 