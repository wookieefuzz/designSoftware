import sys
import time
sys.path.append('/home/pi/')
sys.path.append('/home/pi/designSoftware/pythonExamples/')
from credentials import credentials
from dataVariable import dataVariable
from sendGroupMe import sendGroupMe

import gspread

bot_id = "8c74b68834ee6321b461634b8b"

gm = sendGroupMe(bot_id)

# pull in credentials for twitter and gmail
c = credentials()

gc = gspread.login(c.EMAIL,c.PW)

ConstantsKEY = '1558HRJTmtVGqbOFc510BUpCCwPe-yfDhaXQtEGXr8-w'

wksTmp = gc.open_by_key(ConstantsKEY)
wks = wksTmp.get_worksheet(1)

dvList = []

for i in range(1,11):
	name = wks.cell(i,1).value
	value = wks.cell(i,2).value
	units = wks.cell(i,3).value
	msg = str(name + "," + value + "," + units)
	print(msg)
	gm.sendText(msg)
	time.sleep(5)
	dvTemp = dataVariable(name,value,units)
	dvTemp.printCurrentValue()
	dvList.append(dvTemp)





