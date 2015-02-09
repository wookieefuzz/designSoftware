from dataVariable import dataVariable
from scraper import scraper

dv = dataVariable('AR',8,'N/A')
dv.printInfo()

S = scraper()

S.updateDataFile(dv)

dv.value = 9;

S.updateDataFile(dv)
