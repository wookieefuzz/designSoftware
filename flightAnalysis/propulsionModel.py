from gold import gold
from motorModel import motorModel
import math

class propulsionModel:
    def __init__(self,prop):
        self.g = gold()
        #self.motor = motor
        self.prop = prop
        print 'propulsion model initialized'
        
    def operateAtAirspeedWithThrust(self,V,T,minRPM,maxRPM,altitude):
        # sweep up from low rpm until the thrust has juuuust exceeded the required thrust
        Tout = -1000.0
        rpm = minRPM
        
        [Din,x,cR,beta1Deg,aoldeg] = self.prop.getData()
        
        
        while (Tout<T) and (rpm<maxRPM):
            
            output = self.g.run(V,Din,rpm,x,cR,beta1Deg,aoldeg,altitude)
            Tout = output[3]
            if Tout<T:
                lowerBound = rpm
            else:
                upperBound = rpm
            rpm = rpm + 100.0
           
        Tout = -1000.0
        rpm = lowerBound
        
        while (Tout<T) and (rpm<upperBound):
            
            output = self.g.run(V,Din,rpm,x,cR,beta1Deg,aoldeg,altitude)
            Tout = output[3]
            if Tout<T:
                lowerBound = rpm
            else:
                upperBound = rpm
            rpm = rpm + 1.0
           
        rpmForThrust = (lowerBound + upperBound)/2.0
        
        print 'rpm required to produce that amount of thrust is ' + str(rpmForThrust)