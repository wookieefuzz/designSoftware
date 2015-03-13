import math

class gold:
    
    
    def __init__(self):
        print 'goldstein method initialized'
        
    def run(self,V,Din,RPM,x,cR,beta1Deg,aoldeg,altitude):
        
        output = [0.0, 0.0, 0.0]
        
        Cd0 = .03
        
        a = 2.0 * math.pi
        
        densities = self.altitudeToDensity(altitude, 'm')
        rho = densities[1] 
        
        aolDeg = self.scalarMultiply(self.listOfOnes(len(beta1Deg)),aoldeg)
        
        k = self.inducedDragFactor(cR)
        
        V = 3.28084 * V # speed in feet per second
        # DO UNIT CONVERSIONS
        
        D=Din/12.0;     # Diameter in feet
        R=D/2.0;        # Radius in feet
        n=RPM/60.0;     # propeller frequency (rev/sec) or (hz)
        omega=2.0*math.pi*n; # frequency of revolution of the propeller (rad/sec)
        lmbda=V/(omega*R);
        r2d=180.0/math.pi;
        Vt=omega*R;   # tip velocity (ft/sec)
        J=V/(n*D);    # advance ratio
        
        c=self.scalarMultiply(cR, R);    # chord in feet
        cin=self.scalarMultiply(c, 12.0);  # chord in inches
        beta = self.scalarMultiply(self.elementWiseAdd(beta1Deg,aolDeg), 1.0/r2d)
       
     
        sigma = self.scalarMultiply(c, 2.0/(math.pi * R)) # solidity? output is 1 x num(r)
        r = self.scalarMultiply(x, R) # actual local radius locations
        tmp = self.addScalarToList(self.elementWiseMultiply(x, x),lmbda**2.0)
#         Vr = Vt * self.elementWiseSqrt(tmp)
        Vr = self.scalarMultiply(self.elementWiseSqrt(tmp), Vt)
        tmp = self.invertList(x)
        phi = self.elementWiseAtan(self.scalarMultiply(tmp, lmbda))
    
        tmp = self.listOfOnes(len(c))
        WtVt = self.scalarMultiply(tmp, 0.02)
        nr = len(c)
        nr1 = nr - 1
        aiold = self.listOfZeros(nr)
        ai = self.listOfZeros(nr)
        WaVt = self.listOfZeros(nr)
        Cl = self.listOfZeros(nr)
        VeVt = self.listOfZeros(nr)
        gamma = self.listOfZeros(nr)
        sinphialp = self.listOfZeros(nr)
        kappa = self.listOfZeros(nr)
        Zp = self.listOfZeros(nr)
        Zt = self.listOfZeros(nr)
        dCtdx = self.listOfZeros(nr)
        dCpdx = self.listOfZeros(nr)
        Cd = self.listOfZeros(nr)
    
        # calc values at all but the last station
        for ii in range(1,50):
            
            for i in range(0,nr1):
                tmp = lmbda**2.0 + 4.0*WtVt[i]*(x[i]-WtVt[i])
                if tmp < 0:
                    print 'solution became imaginary. quitting'
                    return output
                WaVt[i] = .5 * (-lmbda + math.sqrt(tmp))
                ai[i] = math.atan(WtVt[i]/WaVt[i]) - phi[i]
            
            e = abs(sum(ai) - sum(aiold))
            
#             print 'loop = ' + str(ii) + ', error = ' + str(e)
            
            if e<.0001:
                break
            
            # THIS IS THE WEIRDEST BUG! SEEMED TO BE PASSING BY REFERENCE, NOT VALUE
            itr = -1
            for elem in ai:
                itr += 1
                aiold[itr] = elem
           
            
            
            for i in range(0,nr1):
                Cl[i] = a*(beta[i]-ai[i]-phi[i])
                tmp = (lmbda + WaVt[i])**2.0 + (x[i]-WtVt[i])**2.0
                if tmp < 0:
                    print 'solution became imaginary. quitting'
                    return output
                VeVt[i] = math.sqrt(tmp)
                gamma[i] = 0.5 * c[i]*Cl[i]*VeVt[i]*Vt
                sinphialp[i] = math.sin(phi[i]+ai[i])
                kappa[i] = self.kappa2(x[i],sinphialp[i])
                WtVt[i] = 2.0*gamma[i]/(4.0*math.pi*Vt*r[i]*kappa[i])
            
        # calc values at last radial station
        Cl[nr1] = 0.0;
        ai[nr1] = beta[nr1] - phi[nr1]
        VrVt = math.sqrt(lmbda**2.0 + 1.0)
        WaVt[nr1] = VrVt*math.sin(ai[nr1])*math.cos(ai[nr1]+phi[nr1])
        WtVt[nr1] = VrVt*math.sin(ai[nr1])*math.sin(ai[nr1]+phi[nr1])
        tmp = (lmbda + WaVt[nr1])**2.0 + (x[nr1]-WtVt[nr1])**2.0
        if tmp < 0:
            print 'solution became imaginary. quitting'
            return output
        VeVt[nr1] = math.sqrt(tmp)
        kappa[nr1] = 0.0
        
        for i in range(0,nr):
            Cd[i] = Cd0 + k*Cl[i]*Cl[i]
            Zt[i] = (math.pi / 8.0) * (J**2.0 + math.pi**2.0 * x[i]**2.0) * sigma[i]
            Zp[i] = math.pi*Zt[i]*x[i]
            dCtdx[i] = Zt[i] * (Cl[i] * math.cos(phi[i]+ai[i])-Cd[i]*math.sin(phi[i]+ai[i]))
            dCpdx[i] = Zp[i] * (Cl[i] * math.sin(phi[i]+ai[i])+Cd[i]*math.cos(phi[i]+ai[i]))
        
        Ct = self.trapz(x, dCtdx)
        Cp = self.trapz(x,dCpdx)
        eta = Ct * J / Cp
        
        
        output = [Ct, Cp, eta]
        
        if eta<0.0 or eta>1.0:
            output = [0.0,0.0,0.0]
        
        return output
    
    def altitudeToDensity(self,h,units):
        output = [ 0.0 , 0.0]
        
        if units=='ft':
            h = .3048 * h
            
        p0 = 101.325 * 1e3; # pressure at sea level, pascals
        T0 = 288.15; # temp at sea level, kelvin
        g = 9.80665; # accel due to gravity, m/s^2
        L = .0065; # temp lapse rate, deg K / m
        R = 8.31447; # ideal gas constant, j/mol*k
        M = 0.0289644; # molar mass of dry air

        T = T0 - L*h; # temp at altitude

        p = p0 * math.pow((1.0 - ((L*h)/T0)),(g*M/(R*L)))
        rho = p*M/(R*T);

        densityMetric = rho;

        densityImperial = rho*0.00194032033; # convert to slugs
        
        output[0] = densityMetric
        output[1]= densityImperial
        return output
        
    def inducedDragFactor(self,cR):
        eff = .95
        AR = 1.0 / (sum(cR)/float(len(cR)))
        k = 1.0 / (math.pi * AR * eff)
        return k
    
    def elementWiseAdd(self,l1,l2):
        output = []
        i = -1
        for elem in l1:
            i += 1
            output.append(elem + l2[i])
        return output
            
    def listOfZeros(self,length):
        output = []
        for i in range(0,length):
            output.append(0.0)
        return output
    
    def listOfOnes(self,length):
        output = []
        for i in range(0,length):
            output.append(1.0)
        return output
    
    def scalarMultiply(self,l,a):
        output = []
        for v in l:
            output.append(float(v*a))
        return output
    
    def addScalarToList(self,l,a):
        output = []
        for elem in l:
            output.append(elem + a)
        return output
    
    def elementWiseMultiply(self,a,b):
        output = []
        i = -1
        for elem in a:
            i += 1
            output.append(float(elem * b[i]))
        return output
        
    def elementWiseDivide(self,a,b):
        output = []
        i = -1
        for elem in a:
            i += 1
            output.append(float(elem / b[i]))
        return output
    
    def invertList(self,l):
        output = []
        for elem in l:
            output.append(1.0/elem)
        return output
        
    def elementWiseSqrt(self,a):
        output = []
        for elem in a:
            output.append(math.sqrt(elem))
        return output
    
    def elementWiseAtan(self,a):
        output = []
        for elem in a:
            output.append(math.atan(elem))
        return output
    
    def trapz(self,x,y):
        integral = 0.0
        numPts = len(x)
        numTraps = numPts - 1
        for i in range(1,numTraps+1): 
            dx = x[i] - x[i-1]
            integral += ((y[i]+y[i-1])/2.0)*dx
        return integral       
    
    def kappa2(self,x,sinphialp):
        kappa = (2.0 / math.pi) * math.acos(math.exp((x-1.0)/sinphialp))
        return kappa