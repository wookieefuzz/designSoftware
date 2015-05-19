class groupMeUser:
    
    def __init__(self,name):
        self.name = name
        self.count = 0
        self.messagesPerDay = [0]*730
        self.timeList = []
        
    def addTime(self,time):
        self.timeList.append(time)
        
    def addMessage(self):
        self.count += 1
        
    def printInfo(self):
        print('user: ' + self.name + ' has sent ' + str(self.count) + ' messages')
        
    def printMessagesPerDay(self):
        print self.messagesPerDay
        
    def writeDataToFile(self):
        fName = self.name + '.txt'
        f = open(fName,'w')
        for t in self.timeList:
            f.write(str(t) + '\n')
        f.close()