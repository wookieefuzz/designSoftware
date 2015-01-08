import sys
sys.path.append('/home/pi/')
sys.path.append('/home/pi/designSoftware/pythonExamples/')
from credentials import credentials
from dataVariable import dataVariable

import gspread

# pull in credentials for twitter and gmail
c = credentials()

gc = gspread.login(c.EMAIL,c.PW)

ConstantsKEY = '1558HRJTmtVGqbOFc510BUpCCwPe-yfDhaXQtEGXr8-w'

wksTmp = gc.open_by_key(ConstantsKEY)
wks = wksTmp.get_worksheet(1)

dvList = []

for i in range(1,10):
	name = wks.cell(i,1)
	value = wks.cell(i,2)
	units = wks.cell(i,3)
	dvTemp = dataVariable(name,value,units)
	dvTemp.printCurrentValue()
	dvList.append(dvTemp)





