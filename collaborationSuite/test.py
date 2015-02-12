from scraper import scraper
from sendGroupMe import sendGroupMe


key = '1DEkQzDp5QOPuIJvyEOe1Bt-G68UG7BCOlrNDIM2-_j8'
sheetName = 'Sheet1'

botID = '8c74b68834ee6321b461634b8b'

S = scraper(key)

# pull in all variables
dvList = S.getDataFromSheet(key,sheetName)

# check for changes
S.checkForChanges(key,sheetName,botID)

# update files
S.updateAllFiles(key,sheetName)

