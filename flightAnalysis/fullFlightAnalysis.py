import math
from dataVariable import dataVariable
import gspread
from propulsionModel import propulsionModel
from math import acos

class fullFlightAnalysis:
    
    def __init__(self):
        self.pmInit = False
        print 'done initializing'
    
    def addPropulsionModel(self,p,mm):
        self.pm = propulsionModel(p,mm)
        self.pmInit = True
      
    def takeOffAnalysis(self):
        return 0.0
        
    def cruiseForDistance(self,W,S,v,rho,k,Cd0,dist,minRPM,maxRPM,altitude):
        if self.pmInit:
            Treqd = self.steadyLevelFlight(W,S,v,rho,k,Cd0,False)
            output = self.pm.operateAtAirspeedWithThrust(v,Treqd,minRPM,maxRPM,altitude)
            time = dist  / v
            pwrReqd = output[5] * time # output is joules
            print 'energy required to fly this distance is ' + str(round(pwrReqd)) + ' Joules'
        else:
            print 'propulsion model not yet initialized'
            
    def turnAnalysisR(self,S,W,rho,V,R,Clmax,k,Cd0,printBool):
        if printBool:
            print 'running turn analysis given a turn radius'
        
         # calculate gamma
        
        q = .5 * rho * V**2
        # assume gamma = 0, solve for phi based on R
        phi = math.atan(V**2 / (9.81 * R))
        #gamma = math.acos((R*9.81*math.tan(phi) / V**2.0)) # this is dumb... 
        gamma = 0.0
        L = W*math.cos(gamma) / math.cos(phi)
        Cl = L / (q * S)
        
        T = q*Cd0 + k * (1.0 / (q))*(Cl**2) + W*math.sin(gamma)
        
        if printBool:
            print 'phi = '+str(phi*(180.0/math.pi)) +' deg, gamma = ' + str(gamma / (180.0/math.pi)) + ' deg, Cl = ' + str(Cl) + ', thrust reqd = ' + str(T) + ' N' 
        
        output = [T,Cl,gamma]
        return output
        
    def turnAnalysisPhi(self,S,W,rho,V,phi,Clmax,k,Cd0,printBool):
        if printBool:
            print 'running turn analysis given a bank angle'
        # calculate gamma
        
        q = .5 * rho * V**2
        # assume gamma = 0, solve for R
        R = (V**2)/(9.81 * math.tan(phi))
        #gamma = math.acos((R*9.81*math.tan(phi) / V**2.0)) # this is dumb... 
        gamma = 0.0
        L = W*math.cos(gamma) / math.cos(phi)
        Cl = L / (q * S)
        
        T = q*Cd0 + k * (1.0 / (q))*(Cl**2) + W*math.sin(gamma)
        
        if printBool:
            print 'R = '+str(R) +' m, gamma = ' + str(gamma / (180.0/math.pi)) + ' deg, Cl = ' + str(Cl) + ', thrust reqd = ' + str(T) + ' N' 
        
        output = [T,Cl,gamma]
        return output
    
    def handLaunchAnalysis(self,S,W,rho,v0,Cl0,Cd0,Clmax,k,height,Tstatic,tMax,printBool,stepPrintBool):
        if printBool:
            print 'running hand launch analysis for a level throw'
        
        m = W / 9.81
        t = 0.0;
        dt = .01
        endConditions = False
        
        alpha = 0.0
        
        X = 0.0
        Y = height
        Vx = v0
        Vy = 0.0
        
        q = 0.5 * rho * v0**2
        
        T = Tstatic
        
        while(endConditions == False):
            
            Cl = Cl0 + 2*math.pi*alpha
            
            if Cl>Clmax:
                Cl = Clmax
            
            t = t + dt
            Fx = T - q * S * (Cd0 + k*Cl)
            Fy = q*S*Cl - W
            ax = Fx / m
            ay = Fy / m
            Vx = Vx + ax * dt
            Vy = Vy + ay * dt
            X = X + Vx * dt
            Y = Y + Vy * dt
            v = math.sqrt(Vx**2 + Vy**2)
            q = 0.5 * rho * v**2
            
            alpha = math.atan(-Vy/Vx)
            
            if stepPrintBool:
                print str(X) + ',' + str(Y)
            
            if Y < 0:
                endConditions = True
            elif t > tMax:
                endConditions = True
                
        if printBool:
            print 'after ' + str(t) + ' sec, aircraft is at an altitude of ' + str(Y) + ' m, and is ' + str(X) + ' m downrange'
            print 'x velocity = ' + str(Vx) + ', y velocity = ' + str(Vy) + ' and total velocity = ' + str(v)
            print 'Cl = ' + str(Cl)
        return 0.0
        
    def inclinedHandLaunchAnalysis(self,S,W,rho,v0,Cl0,Cd0,Clmax,k,height,Tstatic,tMax,printBool,stepPrintBool,theta,zeroThrustSpeed,fitType,thetaFinal,pushOverTime):
        if printBool:
            print 'running hand launch analysis for an inclined throw'
        m = W / 9.81
        t = 0.0;
        dt = .01
        endConditions = False
        
        alpha = 0.0
        
        X = 0.0
        Y = height
        
        Vx = v0 * math.cos(theta)
        Vy = v0 * math.sin(theta)
        
        q = 0.5 * rho * v0**2
        
        v = v0
        
        while(endConditions == False):
            
            if (pushOverTime != 0.0) and (t<pushOverTime):
                Theta = theta - (t/pushOverTime)*(theta - thetaFinal)
            elif (pushOverTime == 0.0):
                Theta = theta
            elif (pushOverTime != 0.0) and (t>=pushOverTime):
                Theta = thetaFinal
                
            v = math.sqrt(Vx**2 + Vy**2)
            q = 0.5 * rho * v**2
            
            if fitType == 'linear':
                T = Tstatic - Tstatic * (v/zeroThrustSpeed)
            
            phi = math.atan(Vy/Vx)
            
            Cl = Cl0 + 2*math.pi*alpha
            
            if Cl>Clmax:
                Cl = Clmax
            
            t = t + dt
            L = q * S * Cl
            D = q * S * (Cd0 + k*Cl*Cl)
            Fx = T*math.cos(Theta) + (q * S * (Cd0 + k*Cl**2))*math.cos(phi+math.pi) + (q * S * Cl)*math.cos(phi+.5*math.pi)
            Fy = T*math.sin(Theta) + (q * S * (Cd0 + k*Cl**2))*math.sin(phi+math.pi) + (q * S * Cl)*math.sin(phi+.5*math.pi) - W
            ax = Fx / m
            ay = Fy / m
            Vx = Vx + ax * dt
            Vy = Vy + ay * dt
            X = X + Vx * dt
            Y = Y + Vy * dt
            
            alpha = Theta - math.atan(Vy/Vx)
            
            if stepPrintBool:
                print str(X) + ',' + str(Y) + ',' + str(Cl)+','+str(L)+','+str(D)+','+str(L/D)+','+str(Vx)+','+str(Vy)+','+str(Theta)+','+str(t)
            
            if Y < 0:
                endConditions = True
            elif t > tMax:
                endConditions = True
                
        if printBool:
            print 'after ' + str(t) + ' sec, aircraft is at an altitude of ' + str(Y) + ' m, and is ' + str(X) + ' m downrange'
            print 'x velocity = ' + str(Vx) + ', y velocity = ' + str(Vy) + ' and total velocity = ' + str(v)
            print 'Cl = ' + str(Cl)
        return 0.0
        
    def climbAnalysis(self,rho,S,k,W,vc,v,Cl0,Cd0,printBool):
        
        q = .5 * rho * v**2.0
        
        tol = .000001
        
        gamma = math.asin(vc/v)
        
        alpha = self.solveForAlphaInClimbBisection(gamma,q,rho,S,k,W,vc,v,Cl0,Cd0, tol)
        cl = Cl0 + 2.0* math.pi * alpha
        thrust = (W * math.cos(gamma) - q*S*cl) / math.sin(alpha)

        alphaReqdDeg = alpha * 57.2957795
        
        if printBool:
            print 'peforming a climb analysis'
            print 'climb angle is ' + str(gamma*(180.0/math.pi)) + ' deg'
            print 'AoA required is ' + str(alphaReqdDeg) + ' deg'
            #print 'angle of attack required for climb is ' + str(alpha) + ' rad'
            print 'lift coefficient required for climb is ' + str(cl) 
            print 'thrust required for climb is ' + str(thrust) + ' Newtons'
            thrustToWeight = thrust/W
            
            print 'which is ' + str(thrustToWeight*100) + ' % of the weight'
        
        return alpha
    
    def steadyLevelFlight(self,W,S,v,rho,k,Cd0,printBool):
        
        # solve for lift coefficient
        Cl = (2.0 * W) / (rho * v * v * S)
        
        # look up AoA
        # don't really need, make an approximation that thrust and drag are opposite each other
        
        # calculate or look up Cd
        
        Cd = Cd0 + (Cl * Cl)*k
    
        # solve for thrust
        T = .5 * rho * v * v * Cd * S
        
        if printBool:
            print 'required level flight Cl = ' + str(round(Cl,2)) 
            print 'required thrust in level flight = ' + str(round(T,2)) + ' N'
         
        return T
    
    def solveForStaticThrust(self,pitch,dia,rpm,printBool):
        T = (4.392399e-8) * rpm * (math.pow(dia,3.5) / math.sqrt(pitch)) * (4.233333e-4 * rpm * pitch)
        if printBool:
            print 'Static thrust is ' + str(T) + ' N'
        return T
    
    def solveForStallSpeed(self,weight,S,Clmax,rho,printBool):
        # L = .5 * rho * Clmax * S * v**2
        # 2.0 * W / (rho * clmax * S) = v**2
        vStall = math.sqrt(2.0 * weight / (rho * Clmax * S))
        if printBool:
            print 'stall speed is ' + str(vStall) + ' m/s'
        return vStall
        
    def solveForApproachSpeed(self,weight,S,Clmax,rho,printBool):
        vStall = self.solveForStallSpeed(weight,S,Clmax,rho,'False')
        vApproach = 1.2 * vStall
        if printBool:
            print 'approach speed is ' + str(vApproach) + ' m/s'
        return vApproach
        
    def solveForAlphaInClimbBisection(self,gamma,q,rho,S,k,W,vc,v,Cl0,Cd0,tol):
        # solve for the required alpha by bisection with thin airfoil theory
    
        itr = 0
        llim = .01
        ulim = 1.0
        
        while(abs(llim-ulim)>tol):
            
            itr = itr + 1
            
            alphaLower = llim
            alphaUpper = ulim
            alphaTest = ( llim + ulim ) / 2.0
            
            fxLower =  q*S*Cd0 + W*math.sin(gamma) + q*S*k*(Cl0+2.0*math.pi*alphaLower)**2.0 - W*math.cos(gamma)/math.tan(alphaLower) + (q*S*(Cl0+2.0*math.pi*alphaLower))/math.tan(alphaLower)
            fxUpper =  q*S*Cd0 + W*math.sin(gamma) + q*S*k*(Cl0+2.0*math.pi*alphaUpper)**2.0 - W*math.cos(gamma)/math.tan(alphaUpper) + (q*S*(Cl0+2.0*math.pi*alphaUpper))/math.tan(alphaUpper)
            fxTest =  q*S*Cd0 + W*math.sin(gamma) + q*S*k*(Cl0+2.0*math.pi*alphaTest)**2.0 - W*math.cos(gamma)/math.tan(alphaTest) + (q*S*(Cl0+2.0*math.pi*alphaTest))/math.tan(alphaTest)
            
            if (self.sameSign(fxLower,fxTest)):
                llim = alphaTest
            else:
                ulim = alphaTest
            
        print 'converged after ' + str(itr) + ' iterations'
        
        return alphaTest
     
    # check to see if two numbers have the same sign, used in the bisection
    
    def sameSign(self,a,b):
        
        mult = a*b

        answer = True
        
        if(mult<0):
            answer = False
            
        return answer
    
    