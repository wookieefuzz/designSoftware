# just a simple test case to make sure the motor model is providing the right numbers
from motorModel import motorModel

Kv = 370.0
Rm = .023
I0 = 1.4

m = motorModel(Kv,Rm,I0)

outputA = m.simulateAtRPM(12.0,1000.0)
# output = [Torque, RPM, PowerOut,PowerIn,etaM,Iin,vin]
print outputA

outputB = m.simulateAtCurrent(12.0,outputA[5])
print outputB
