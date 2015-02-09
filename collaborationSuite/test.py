from dataVariable import dataVariable
from scraper import scraper

key = '1DEkQzDp5QOPuIJvyEOe1Bt-G68UG7BCOlrNDIM2-_j8'

S = scraper(key) # replace 'key' with actual key

dvList = S.getDataFromSheet(key,'Sheet1')


for i in range(0,len(dvList)):
    dv = dvList[i]
    S.updateDataFile(dv)

S.checkForChanges(key,'Sheet1')
