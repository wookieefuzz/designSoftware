import os
import string

class sendGroupMe:

    def __init__(self,id):
        self.bot_id = id

    def sendText(self,text):
        text = string.replace(text,' ','%20')
        text = text + '"'
        cmd = "curl -X POST " + '"https://api.groupme.com/v3/bots/post?bot_id=' +self.bot_id+"&text=" + text
        print(cmd)
        os.system(cmd)