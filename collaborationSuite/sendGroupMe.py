import os
import string

class sendGroupMe:

    def __init__(self,id):
        self.bot_id = id

    def sendText(self,text):
        #data = "text:" + text + ",bot_id:" + self.bot_id
        #cmd = ['curl','-d',data,'https://api.groupme.com/v3/bots/post']
        text = string.replace(text,' ','%20')
        text = text + '"'
        cmd = "curl -X POST " + '"https://api.groupme.com/v3/bots/post?bot_id=' +self.bot_id+"&text=" + text
        print(cmd)
        #curl -d '{"text" : "Your message here", "bot_id" : "8c74b68834ee6321b461634b8b"}' https://api.groupme.com/v3/bots/post
        #subprocess.Popen(cmd)
        os.system(cmd)