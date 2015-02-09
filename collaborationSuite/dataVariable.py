class dataVariable:
    
    def __init__(self,name,value,units):
        self.name = name
        self.value = value
        self.units = units
        
    def printInfo(self):
        output = 'The variable ' + self.name + ' has the value ' + str(self.value) + ' ' + self.units
        print output