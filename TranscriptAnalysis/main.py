import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from transcriptAnalysis2 import transcriptAnalysis2
from groupMeUser import groupMeUser

fName1 = "airheartTranscript.json"
fName2 = "agTranscript.json"
fName3 = "motoTranscript.json"
fName4 = "guardianTranscript.json"

print(sys.getdefaultencoding())

ta = transcriptAnalysis2()
ta.jsonToText(fName1)

ta.collaborationAnalysis()
print('all done')