


import sys
from math import floor
reload(sys)
sys.setdefaultencoding('utf-8')
from groupMeUser import groupMeUser


import json
import datetime

class transcriptAnalysis2:
    
    def __init__(self):
        self.name = 'transcriptAnalysis'
        self.userList = []
        
        
    def printTranscript(self,messages):
        
        messagesPerDay = [0] * 730 # two years worth of days
        """Prints a readable "transcript" from the given list of messages.
    
        Assumes the input list is sorted."""
    
        firstMessage = True
        
        for message in messages:
            name = message[u'name']
            
            self.addPersonToList(name)
                
            if firstMessage:
                zeroTime = float(message[u'created_at'])
                print('first message was sent at ' + str(zeroTime))
                firstMessage = False
            
            currentTime = float(message[u'created_at'])
            elapsedTime = currentTime - zeroTime
            days = elapsedTime / 86400.0
            day = int(floor(days))
            messagesPerDay[day] += 1
            
            person = self.find_person(name)
            person.messagesPerDay[day] += 1
            
            time = datetime.datetime.fromtimestamp(message[u'created_at']).strftime('%Y-%m-%d %H:%M')
            
            #print time
            # text is None for a photo message
            if message[u'text'] is not None:
                text = message[u'text']
            else:
                text = "(no text)"
    
            if message[u'system'] is True:
                system_padded = '(SYS) '
            else:
                system_padded = ''
    
            
    
            #print(text)
            #print(name)
            #print(system_padded + name + ' (' + time + ')'  ': ' + text)
        self.printAllUserInfo()
        print '-----------------------------------------------------------------'
        print messagesPerDay
        print '-----------------------------------------------------------------'
        for person in self.userList:
            person.printInfo()
            person.printMessagesPerDay()
            
    
    def jsonToText(self,fileName):
        transcriptFile = open(fileName)
        transcript = json.load(transcriptFile)
        transcriptFile.close()
        self.printTranscript(transcript)


    def addPersonToList(self,name):
        if self.isInUserList(name):
            person = self.find_person(name)
            person.count +=1
        else:
            self.userList.append(groupMeUser(name))
            person = self.find_person(name)
            person.count +=1
        


    def find_person(self, name):
       for person in self.userList:
           if person.name == name:
               return person
           
        
    
    def isInUserList(self,name):
        
        answer = False
        
        for groupeMeUser in self.userList:
            if groupeMeUser.name == name:
                answer = True
                break
            
        return answer
    
    
    
    def printAllUserInfo(self):
        for person in self.userList:
            person.printInfo()