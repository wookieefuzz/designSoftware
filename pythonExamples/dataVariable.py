import datetime

class dataVariable:

	# initialize, take a name, a value, and a units string
	def __init__(self,name,value,units):
		self.name = name;
		self.value = value;
		self.units = units;
		self.timeStamps = datetime.datetime.now().isoformat() 

	# add a value as well as the time it was added
	def addValue(self,value):
		self.value.append(value)
		self.timeStamps.append(datetime.datetime.now().isoformat)

	# check for changes
	def checkForChanges(self):
		n = len(self.value)
		if n>1:
			diff = self.value[n] - self.value[n-1] 
			if diff == 0:
				return False
			else:
				return True
		else:
			return False;



