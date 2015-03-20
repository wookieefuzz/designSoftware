import math
from dataVariable import dataVariable
import gspread
from propulsionModel import propulsionModel
from math import acos

class fullFlightAnalysis2:
    
    def __init__(self):
        self.pmInit = False
        print 'done initializing'
    
    def addPropulsionModelOld(self,p,mm):
        self.pm = propulsionModel(p,mm)
        self.pmInit = True
        
    def addPropulsionModel(self,pm):
        self.pm = pm
        self.pmInit = True
      
    def takeOffAnalysis(self):
        return 0.0
        
    def cruiseForDistance(self,di,printBool):
        rhos = self.altitudeToDensity(di.cruiseAlt, 'm')
        rho = rhos[0]
        
        output = [0.0,0.0,0.0]
        
        if self.pmInit:
            Treqd = self.steadyLevelFlight(di.W,di.S,di.vCruise,rho,di.k,di.Cd0,False)
            output = self.pm.operateAtAirspeedWithThrust(di.vCruise,Treqd,5000.0,20000.0,di.cruiseAlt)
            etaTotal = output[9]
            time = di.cruiseDist  / di.vCruise
            energyReqd = output[5] * time # output is joules
            if printBool:
                print 'cruising a distance of ' + str(round(di.cruiseDist/1000.0)) + ' km will take ' + str(round(time)) + ' sec'
                print 'energy required to fly this distance is ' + str(round(energyReqd)) + ' Joules'
                print 'total system efficiency in cruise is ' + str(round(etaTotal*100)) + ' %'
            output = [energyReqd,time,etaTotal]
        else:
            print 'propulsion model not yet initialized'
        
        return output
            
    def turnAnalysisR2(self,di,printBool):
        
        if printBool:
            print 'running turn analysis given a turn radius'
        
        rhos = self.altitudeToDensity(di.cruiseAlt, 'm')
        rho = rhos[0]
        
         # calculate gamma
        
        q = .5 * rho * di.vTurn**2
        # assume gamma = 0, solve for phi based on R
        phi = math.atan(di.vTurn**2 / (9.81 * di.turnRadius))
        #gamma = math.acos((R*9.81*math.tan(phi) / V**2.0)) # this is dumb... 
        gamma = 0.0
        L = di.W*math.cos(gamma) / math.cos(di.bankAngle)
        Cl = L / (q * di.S)
        
        T = q*di.Cd0 + di.k * (1.0 / (q))*(Cl**2) + di.W*math.sin(gamma)
        
        if printBool:
            print 'phi = '+str(phi*(180.0/math.pi)) +' deg, gamma = ' + str(gamma / (180.0/math.pi)) + ' deg, Cl = ' + str(Cl) + ', thrust reqd = ' + str(T) + ' N' 
        
        output = self.pm.operateAtAirspeedWithThrust(di.vTurn,T,5000.0,20000.0,di.turnAlt)
        etaTotal = output[9]
        pwrIn = output[2]
        
        distFlown = 2.0 * math.pi * di.turnRadius * (di.turnAngle / (2.0*math.pi)) * di.numTurns
        timeFlown = distFlown / di.vTurn 
        
        energyUsed = pwrIn * timeFlown
        
        if printBool:
            print 'energy used while making turns was ' + str(round(energyUsed)) + ' J, time taken was ' + str(round(timeFlown)) + ' sec, and system efficiency was ' + str(round(etaTotal*100.0))+ ' %'
        
        output = [energyUsed,timeFlown,etaTotal]
        return output
        
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
        
    def inclinedHandLaunchAnalysis(self,di,printBool,stepPrintBool):
        
        rhoTemp = self.altitudeToDensity(di.altHL, 'm')
        rho = rhoTemp[0]
        
        if printBool:
            print 'running hand launch analysis for an inclined throw'
        W = di.m * 9.81
        t = 0.0;
        dt = .01
        endConditions = False
        
        alpha = 0.0
        
        X = 0.0
        Y = di.height
        
        Vx = di.throwSpeed * math.cos(di.theta)
        Vy = di.throwSpeed * math.sin(di.theta)
        
        q = 0.5 * rho * di.throwSpeed**2
        
        v = di.throwSpeed
        
        while(endConditions == False):
            
            if (di.pushOverTime != 0.0) and (t<di.pushOverTime):
                Theta = di.theta - (t/di.pushOverTime)*(di.theta - di.thetaFinal)
            elif (di.pushOverTime == 0.0):
                Theta = theta
            elif (di.pushOverTime != 0.0) and (t>=di.pushOverTime):
                Theta = di.thetaFinal
                
            v = math.sqrt(Vx**2 + Vy**2)
            q = 0.5 * rho * v**2
            
            if di.thrustCurveFitType == 'linear':
                T = di.staticThrust - di.staticThrust * (v/di.zeroThrustSpeed)
            
            phi = math.atan(Vy/Vx)
            
            Cl = di.Cl0 + 2*math.pi*alpha
            
            if Cl>di.ClMax:
                Cl = di.ClMax
            
            t = t + dt
            L = q * di.S * Cl
            D = q * di.S * (di.Cd0 + di.k*Cl*Cl)
            Fx = T*math.cos(Theta) + (q * di.S * (di.Cd0 + di.k*Cl**2))*math.cos(phi+math.pi) + (q * di.S * Cl)*math.cos(phi+.5*math.pi)
            Fy = T*math.sin(Theta) + (q * di.S * (di.Cd0 + di.k*Cl**2))*math.sin(phi+math.pi) + (q * di.S * Cl)*math.sin(phi+.5*math.pi) - W
            ax = Fx / di.m
            ay = Fy / di.m
            Vx = Vx + ax * dt
            Vy = Vy + ay * dt
            X = X + Vx * dt
            Y = Y + Vy * dt
            
            alpha = Theta - math.atan(Vy/Vx)
            
            if stepPrintBool:
                print str(X) + ',' + str(Y) + ',' + str(Cl)+','+str(L)+','+str(D)+','+str(L/D)+','+str(Vx)+','+str(Vy)+','+str(Theta)+','+str(t)
            
            if Y < 0:
                endConditions = True
            elif t > di.simTime:
                endConditions = True
                
        if printBool:
            print 'after ' + str(t) + ' sec, aircraft is at an altitude of ' + str(Y) + ' m, and is ' + str(X) + ' m downrange'
            print 'x velocity = ' + str(Vx) + ', y velocity = ' + str(Vy) + ' and total velocity = ' + str(v)
            print 'Cl = ' + str(Cl)
        return 0.0
        
    def climbAnalysis(self,rho,S,k,W,vc,v,Cl0,Cd0,printBool):
        # need di.vertRate, di.vClimb, di.startAlt, di.endAlt
        
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
    
    def climbAnalysisAdvanced(self,di,pm,printBool):
        #rho,S,k,W,vc,v,Cl0,Cd0,
        # need di.vertRate, di.vClimb, di.startAlt, di.endAlt
        
        dAlt = di.endAlt - di.startAlt # altitude to climb
        timeToClimb = dAlt / di.vertRate # time to climb (seconds)
        dt = 0.5
        t = -dt
        
        energy = 0.0
        
        numIters = 0.0
        etaTotal = 0.0
        
        while (t<timeToClimb):
            
            numIters += 1.0
            
            t = t + dt
            
            alt = di.startAlt + (t / timeToClimb) * dAlt
            
            rhos = self.altitudeToDensity(alt, 'm')
            
            rho = rhos[0]
        
            q = .5 * rho * di.vClimb**2.0
            
            tol = .000001
            
            gamma = math.asin(di.vertRate/di.vClimb)
            
            alpha = self.solveForAlphaInClimbBisection(gamma,q,rho,di.S,di.k,di.W,di.vertRate,di.vClimb,di.Cl0,di.Cd0, tol)
            cl = di.Cl0 + 2.0* math.pi * alpha
            thrust = (di.W * math.cos(gamma) - q*di.S*cl) / math.sin(alpha)
            
            output = pm.operateAtAirspeedWithThrust(di.vClimb,thrust,5000.0,20000.0,alt)
            #print output[9]
            etaTotal += output[9]*100.0
            # Output = [rpmForThrust, eta, powerIn, torqueNM,motorOutput[2],motorOutput[3],motorOutput[4],motorOutput[5],motorOutput[6],etaM*eta]
            pwrReqd = output[2]
            
            alphaReqdDeg = alpha * 57.2957795
            
            energy = energy + pwrReqd * dt
         
        etaClimb = etaTotal / numIters   
        if printBool:
        
           print 'aircraft will climb from ' + str(round(di.startAlt)) + ' to ' + str(round(di.endAlt)) + ' m in ' + str(round(timeToClimb)) + ' sec'
           print 'energy required for this climb is ' + str(energy) + ' J'
           print 'average efficiency in climb is ' + str(round(etaClimb)) + ' %'
        
        output = [energy,timeToClimb,etaClimb]
        return output
    
    def analyzeEfficiencyVsAirspeed(self,di,alt,minSpeed,maxSpeed,step,printBool):
        rhos = self.altitudeToDensity(alt, 'm')
        rho = rhos[0]
        
        OUTPUT = []
        
        speed = minSpeed - step
        
        while(speed<maxSpeed):
            speed += step
        
            
            if self.pmInit:
                Treqd = self.steadyLevelFlight(di.W,di.S,speed,rho,di.k,di.Cd0,False)
                print Treqd
                output = self.pm.operateAtAirspeedWithThrust(speed,Treqd,5000.0,25000.0,alt)
                etaTotal = output[9]
                OUTPUT.append(speed)
                OUTPUT.append(etaTotal)
                if printBool:
                    print 'total system efficiency in cruise is ' + str(round(etaTotal*100)) + ' %'
            else:
                print 'propulsion model not yet initialized'
                
        return OUTPUT
    
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
    
    def solveForStallSpeed(self,di,printBool):
        rhoTemp = self.altitudeToDensity(di.altHL, 'm')
        rho = rhoTemp[0]
        
        # L = .5 * rho * Clmax * S * v**2
        # 2.0 * W / (rho * clmax * S) = v**2
        vStall = math.sqrt(2.0 * di.W / (rho * di.ClMax * di.S))
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
            
        #print 'converged after ' + str(itr) + ' iterations'
        
        return alphaTest
     
    # check to see if two numbers have the same sign, used in the bisection
    
    def sameSign(self,a,b):
        
        mult = a*b

        answer = True
        
        if(mult<0):
            answer = False
            
        return answer
    
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