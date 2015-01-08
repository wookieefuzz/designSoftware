# gspread provides pushing and pulling to google sheets
import gspread

# Login with your Google account
gc = gspread.login('designBuildFlyBot@gmail.com', 'designBuildFly')

# Open a worksheet from spreadsheet with one shot
wks = gc.open("sheetExample").sheet1


wks.update_acell('A1', "raspberry")
wks.update_acell('B1', "pi")

