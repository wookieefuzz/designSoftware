# this will run the constraint analysis when data is pulled from Drive

# add desktop to path
import sys
sys.path.append('/home/pi/')


# requires gspread, credentials (stored out of git repo), sys
import gspread
from credentials import credentials


# need the key to access the spreadsheet
key = '1zwxKF8RdbRgxticcIvfVJWEMampetnJd4rP4IvgjLmw'
c = credentials()

# log in the doc
gc = gspread.login(c.EMAIL,c.PW)

# pull down the sheets document
file = gc.open_by_key(key)

# open up the two needed sheets
designSheet = file.worksheet("Design")
dataSheet = file.worksheet("Data")

# now go through and find the needed data
cell = designSheet.find("AR")
AR = designSheet.cell(cell.row,2).value

cell = designSheet.find("e")
e = designSheet.cell(cell.row,2).value

cell = designSheet.find("rho")
rho = designSheet.cell(cell.row,2).value

cell = designSheet.find("etaP")
etaP = designSheet.cell(cell.row,2).value

cell = designSheet.find("etaM")
etaM = designSheet.cell(cell.row,2).value

cell = designSheet.find("LoDMax")
LoDMax = designSheet.cell(cell.row,2).value

cell = designSheet.find("RofC")
RofC = designSheet.cell(cell.row,2).value

cell = designSheet.find("vCruise")
vCruise = designSheet.cell(cell.row,2).value

cell = designSheet.find("cd0")
cd0 = designSheet.cell(cell.row,2).value

cell = designSheet.find("N")
N = designSheet.cell(cell.row,2).value

cell = designSheet.find("vHL")
vHL = designSheet.cell(cell.row,2).value

cell = designSheet.find("vMax")
vMax = designSheet.cell(cell.row,2).value

cell = designSheet.find("ClMax")
ClMax = designSheet.cell(cell.row,2).value

# create the design
d = design(AR,e,rho,etaP,etaM,LoDMax,RofC,vCruise,cd0,N,vHL,vMax,ClMax)











