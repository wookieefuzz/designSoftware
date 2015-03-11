from gold import gold
# test all basic functionality of the gold code

g = gold()

lzeros = g.listOfZeros(5)
print 'list of 5 zeros'
print lzeros
print '----------------------------------------------------'
lones = g.listOfOnes(5)
print 'list of 5 ones'
print lones
print '----------------------------------------------------'
mult = g.scalarMultiply(lones,5.0)
print 'list of 5 ones times scalar (5.0)'
print mult
print '----------------------------------------------------'
scaAdd = g.addScalarToList(lones,5.0)
print 'list of 5 ones plus scalar (5.0)'
print scaAdd
print '----------------------------------------------------'
l1 = [1.0, 2.0, 3.0]
l2 = [4.0,5.0,6.0]
elemMult = g.elementWiseMultiply(l1,l2)
print 'two lists multiplied element-wise'
print elemMult
print '----------------------------------------------------'
elemDiv = g.elementWiseDivide(l1,l2)
print 'two lists divided element-wise'
print elemDiv
print '----------------------------------------------------'
invrt = g.invertList(l1)
print 'inverted list'
print invrt
print '----------------------------------------------------'
sqrtList = g.elementWiseSqrt(l1)
print 'sqrt of list'
print sqrtList
print '----------------------------------------------------'
atanList = g.elementWiseAtan(l1)
print 'atan() of list'
print atanList
print '----------------------------------------------------'
x = [0.0,1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
y = [0.0,1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
integral = g.trapz(x,y)
print 'integral of x^2 from 0 to 9 using trapz = ' + str(integral)
print '----------------------------------------------------'
kappa = g.kappa2(.5,.7)
print 'kappa for x = .5, sinphi = .7 is ' + str(kappa)
print '----------------------------------------------------'
V = 9.14
Din = 11.0
RPM = 5.0
aoldeg = -2.7
altitude = 0.0
x = [.15,.2,.25,.3,.35,.4,.45,.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1.0]
cR = [0.131,    0.145,   0.161,  0.176,   0.185,  0.189,   0.1890,   0.185,   0.177,   0.167,   0.154,   0.14,  0.125,  0.11,   0.095,   0.081,   0.062,   0.043]
beta = [41.81,    45.76,    41.73,    36.13,    31.59,    28.07,    25.32,    23.02,    21.04,    19.62,    18.47,    17.38,   16.28,    15.33,    14.58,    13.77,    13.05,   12.34]

output = g.run(V,Din,RPM,x,cR,beta,aoldeg,altitude)
cT = output[0]
cP = output[1]
eta = output[2]
print 'cT = ' + str(cT)
print 'cP = ' + str(cP)
print 'eta = ' + str(eta)
print '----------------------------------------------------'

