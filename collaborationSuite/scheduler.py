import time
from scraper import scraper
from dataVariable import dataVariable

key = '1ajTeTYzpvzRVa51Jtoc9_mnrx1Nmu_9UvZ6YnRlkLjE'
sheetName = 'Aircraft Parameters'
botID = '8c74b68834ee6321b461634b8b'

S = scraper(key)

interval = 10

while True:
    time.sleep(interval)
    dvList = S.getDataFromSheet(key,sheetName)

    # check for changes
    S.checkForChanges(key,sheetName,botID)

    # update files
    S.updateAllFiles(key,sheetName)
    