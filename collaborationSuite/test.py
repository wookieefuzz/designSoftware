from dataVariable import dataVariable
from scraper import scraper
from sendGroupMe import sendGroupMe

key = '1DEkQzDp5QOPuIJvyEOe1Bt-G68UG7BCOlrNDIM2-_j8'
sheetName = 'Sheet1'

botID = '8c74b68834ee6321b461634b8b'

gm = sendGroupMe(botID)
gm.sendText('hi! this is a test message')

S = scraper(key)

# pull in all variables
dvList = S.getDataFromSheet(key,sheetName)

# check for changes
S.checkForChanges(key,sheetName,botID)

# update files
S.updateAllFiles(key,sheetName)

