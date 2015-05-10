class groupMeUser:
    
    def __init__(self,name):
        self.name = name
        self.count = 0
        self.messagesPerDay = [0]*730
        
    def addMessage(self):
        self.count += 1
        
    def printInfo(self):
        print('user: ' + self.name + ' has sent ' + str(self.count) + ' messages')
        
    def printMessagesPerDay(self):
        print self.messagesPerDay