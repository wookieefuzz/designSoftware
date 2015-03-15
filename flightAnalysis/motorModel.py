class motorModel:
    
    def __init__(self,Kv,Rm,I0):
        self.kv = Kv
        self.rm = Rm
        self.i0 = I0
        self.kt = 1355.0 / Kv
    
    def simulateAtOperatingPoint(self,RPM,torqueReqd):
        #Torque = self.kt * (Iin - self.i0) * 0.00706155183333
        Iin = torqueReqd / (self.kt * 0.00706155183333) + self.i0
        #  Iin = (vin - (RPM/self.kv))/self.rm # 
        vin = Iin * self.rm + (RPM / self.kv)
        PowerOut = (Iin - self.i0) * (vin - Iin*self.rm)
        PowerIn = vin * Iin
        etaM = PowerOut/PowerIn
        output = [torqueReqd, RPM, PowerOut,PowerIn,etaM,Iin,vin]
        print output
        return output
    
    def simulateAtRPM(self,vin,RPM,printBool):
        
        Iin = (vin - (RPM/self.kv))/self.rm # 
         
        Torque = self.kt * (Iin - self.i0) * 0.00706155183333
        PowerOut = (Iin - self.i0) * (vin - Iin*self.rm)
        PowerIn = vin * Iin
        etaM = PowerOut/PowerIn
        
        if etaM<0.0 or etaM>1.0:
            #[Torque, RPM, PowerOut,PowerIn,etaM,Iin,vin]
            print 'motor inoperable at this condition'
            Torque = 0.0
            RPM = 0.0
            PowerOut = 0.0
            PowerIn = 0.0
            etaM = 0.0
            Iin = 0.0
            vin = 0.0
        
        if printBool:
            print 'Torque = '+ str(Torque) + ', RPM = ' + str(RPM) + ', Power Out = ' + str(PowerOut) +', Power in = ' +str(PowerIn) + ', eta = ' + str(etaM)+', current = '+ str(Iin) +', voltage = ' + str(vin)
        output = [Torque, RPM, PowerOut,PowerIn,etaM,Iin,vin]
        return output
        
    def simulateAtCurrent(self,vin,Iin):
        Torque = self.kt * (Iin - self.i0) * 0.00706155183333
        RPM = self.kv * (vin - Iin*self.rm)
        PowerOut = (Iin - self.i0) * (vin - Iin*self.rm)
        PowerIn = vin * Iin
        etaM = PowerOut/PowerIn
        output = [Torque, RPM, PowerOut,PowerIn,etaM,Iin,vin]
        return output
    