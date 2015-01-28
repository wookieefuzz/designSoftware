class motorModel:
    
    def __init__(self,Kv,Rm,I0):
        self.kv = Kv
        self.rm = Rm
        self.i0 = I0
        self.kt = 1355.0 / Kv
        
    
    def simulateAtRPM(self,vin,RPM):
        
        Iin = (vin - (RPM/self.kv))/self.rm # 
         
        Torque = self.kt * (Iin - self.i0) * 0.00706155183333
        PowerOut = (Iin - self.i0) * (vin - Iin*self.rm)
        PowerIn = vin * Iin
        etaM = PowerOut/PowerIn
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
    