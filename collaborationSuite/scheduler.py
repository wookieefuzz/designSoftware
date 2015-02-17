import time
from scraper import scraper
from dataVariable import dataVariable

key = '1ajTeTYzpvzRVa51Jtoc9_mnrx1Nmu_9UvZ6YnRlkLjE' # key to doc
sheetName = 'Aircraft Parameters'
#botID = '8c74b68834ee6321b461634b8b' # test group
botID = '9643f965e64f584aabb71af780'  # ag uav group

S = scraper(key)

interval = 3600

while True:
    time.sleep(interval)
    dvList = S.getDataFromSheet(key,sheetName)

    # check for changes
    S.checkForChanges(key,sheetName,botID)

    # update files
    S.updateAllFiles(key,sheetName)
    