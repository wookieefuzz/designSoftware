# just a simple test case to make sure the motor model is providing the right numbers
from motorModel import motorModel

Kv = 1820
Rm = .075
I0 = 2

m = motorModel(Kv,Rm,I0)

outputA = m.simulateAtRPM(8.4,13200.0)
# output = [Torque, RPM, PowerOut,PowerIn,etaM,Iin,vin]
print outputA

outputB = m.simulateAtCurrent(8.4,outputA[5])
print outputB
