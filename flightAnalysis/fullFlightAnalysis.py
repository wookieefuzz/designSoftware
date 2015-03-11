import math
from math import acos

class fullFlightAnalysis:
    
    def __init__(self):
        print 'done initializing'
        
    def takeOffAnalysis(self):
        return 0.0
    
    def handLaunchAnalysis(self,S,W,rho,v0,Cl0,Cd0,Clmax,k,height,Tstatic,tMax,printBool,stepPrintBool):
        
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
        
    def climbAnalysis(self,rho,S,k,W,vc,v,Cl0,Cd0):
        
        print 'rho = ' +str(rho)
        print 'S = ' + str(S)
        print 'k = ' + str(k)
        print 'W = ' + str(W)
        print 'vc = ' + str(vc)
        print 'v = ' + str(v)
        print 'Cl0 = ' + str(Cl0)
        print 'Cd0 = ' + str(Cd0)
        
        q = .5 * rho * v**2.0
        
        tol = .000001
        
        gamma = math.asin(vc/v)
        
        print 'climb angle is ' + str(gamma) + ' rad'
        
        alpha = self.solveForAlphaInClimbBisection(gamma,q,rho,S,k,W,vc,v,Cl0,Cd0, tol)
        cl = Cl0 + 2.0* math.pi * alpha
        thrust = (W * math.cos(gamma) - q*S*cl) / math.sin(alpha)

        alphaReqdDeg = alpha * 57.2957795

        print 'AoA required is ' + str(alphaReqdDeg) + ' deg'
        #print 'angle of attack required for climb is ' + str(alpha) + ' rad'
        print 'lift coefficient required for climb is ' + str(cl) 
        print 'thrust required for climb is ' + str(thrust) + ' Newtons'
        thrustToWeight = thrust/W
        
        print 'which is ' + str(thrustToWeight*100) + ' % of the weight'
        
        return alpha
    
    def steadyLevelFlight(self,v,aircraft,printBool):
        
        a = aircraft
        
        # solve for lift coefficient
        Cl = (2.0 * a.W) / (a.rho * v * v * a.S)
        
        # look up AoA
        # don't really need, make an approximation that thrust and drag are opposite eachother
        
        # calculate or look up Cd
        k = math.pi * a.e * a.AR
        Cd = a.Cd0 + (Cl * Cl)/k
        
        # solve for thrust
        T = .5 * a.rho * v * v * Cd * a.S
        
        # solve for power
        P = T * v
        
        Pprop = P / (a.etaM * a.etaP)
        ampDraw = Pprop / ((11.1 + 12.6) / 2)
        
        if printBool:
            print 'required level flight Cl = ' + str(round(Cl,2)) 
            print 'required thrust in level flight = ' + str(round(T,2)) + ' N'
            print 'required power in level flight = ' + str(round(P,2)) + ' W'
            print 'given provided efficiencies, power input to propulsion system = ' + str(round(Pprop,2)) + ' W'
            print 'for an average 3S battery pack, current draw would be ' + str(round(ampDraw,2)) + ' A' 
            print 'ability will be added to run propulsion analysis to get more accurate efficiencies'
    
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
#             print 'alpha lower is ' + str(alphaLower)
#             print 'alpha upper is ' + str(alphaUpper)
#             print 'alpha test is ' + str(alphaTest)
            
            
            fxLower =  q*S*Cd0 + W*math.sin(gamma) + q*S*k*(Cl0+2.0*math.pi*alphaLower)**2.0 - W*math.cos(gamma)/math.tan(alphaLower) + (q*S*(Cl0+2.0*math.pi*alphaLower))/math.tan(alphaLower)
            fxUpper =  q*S*Cd0 + W*math.sin(gamma) + q*S*k*(Cl0+2.0*math.pi*alphaUpper)**2.0 - W*math.cos(gamma)/math.tan(alphaUpper) + (q*S*(Cl0+2.0*math.pi*alphaUpper))/math.tan(alphaUpper)
            fxTest =  q*S*Cd0 + W*math.sin(gamma) + q*S*k*(Cl0+2.0*math.pi*alphaTest)**2.0 - W*math.cos(gamma)/math.tan(alphaTest) + (q*S*(Cl0+2.0*math.pi*alphaTest))/math.tan(alphaTest)
            
#             print 'upper value is ' + str(fxUpper)
#             print ' lower value is ' + str(fxLower)
#             print ' test value is ' + str(fxTest)
            
            if (self.sameSign(fxLower,fxTest)):
#                 print 'test and lower values have same sign'
                llim = alphaTest
            else:
#                 print 'test and lower values have opposite sign'
                ulim = alphaTest
            
        print 'converged after ' + str(itr) + ' iterations'
        
        return alphaTest
     
    # check to see if two numbers have the same sign, used in the bisection
    
    def sameSign(self,a,b):
        #print 'testing ' + str(a) + ' and ' + str(b)    
        mult = a*b
        #print 'multiplied together are equal to ' + str(mult)
        
        answer = True
        
        if(mult<0):
            answer = False
            
        return answer
        