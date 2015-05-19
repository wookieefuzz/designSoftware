class user:
    
    def __init__(self):
        self.name = 'no name specified'
        
    
    def setNameFromConfig(self):
        f = open('userInfo.txt','r')
        for line in f:
            str = line.split('=')
            #print str
            if str[0].lower() == 'name':
                self.name = str[1].rstrip()
                print 'set user name to ' + self.name + ' from config file'
                