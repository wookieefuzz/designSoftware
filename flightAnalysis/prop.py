import csv
import re

class prop:
    def __init__(self):
        print 'prop intialized'
         
    def getData(self):
        Din = 11.0
        aoldeg = -2.7
        x = [.15,.2,.25,.3,.35,.4,.45,.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1.0]
        cR = [0.131,    0.145,   0.161,  0.176,   0.185,  0.189,   0.1890,   0.185,   0.177,   0.167,   0.154,   0.14,  0.125,  0.11,   0.095,   0.081,   0.062,   0.043]
        beta = [41.81,    45.76,    41.73,    36.13,    31.59,    28.07,    25.32,    23.02,    21.04,    19.62,    18.47,    17.38,   16.28,    15.33,    14.58,    13.77,    13.05,   12.34]
        output = [Din,x,cR,beta,aoldeg]
        return output
        
    def getDataFromFile(self,fileName):
        x=[]
        cR=[]
        beta=[]
        lol = list(csv.reader(open(fileName, 'rb'), delimiter='\t'))
            
        numRows = len(lol)
        
        for i in range(1,numRows):
            lst = lol[i]
            print lst[0]
            str2prs = lst[0]
            out = str2prs.split()
            print out
            x.append(float(out[0]))
            cR.append(float(out[1]))
            beta.append(float(out[2]))
            
        output = [x,cR,beta]
        return output

    