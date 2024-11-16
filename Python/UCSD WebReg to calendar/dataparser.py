import re
from gcsa.recurrence import *

class ClassInfo:
    def __init__(self, startLine, endLine):
        self.eventInfo = [] # Data structure that holds EVERYTHING pertaining to one particular class    
        self.className = ""   
        self.startLine = startLine
        self.endLine = endLine
        
    def getData(self):
        lines =  open("Classes.txt", "r")
        lineNum = 0
        for line in lines:
            if lineNum in range(self.startLine, self.endLine+1):
                self.extractLine(line) 
            lineNum = lineNum + 1 
    
    def convertTo24hr(self, Time):
       hour = Time[:Time.find(":")]
       minutes = Time[Time.find(":")+1:len(Time)-1]
       if Time[len(Time)-1] == "p" and int(hour) != 12:
           hour = str(int(hour) + 12)
       return f"{hour}:{minutes}"
            
    def extractLine(self, line):
        matches = []
        lastIndex = 0
        if not line.strip() or line.find("Expand:") != -1: # Skip if line doesnt contain any characters or has a stupid expand button
            return
        while (lastIndex != -1): # This will pick out all the words in between '\t'
            curIndex = line.find("\t", lastIndex + 1)
            matches.append(line[lastIndex:curIndex].strip())
            lastIndex = curIndex
        print(matches)
        # if line.find("LE") != -1:
        if (line[0] != ' '):
            self.className = matches[0].replace("   ", " ")
        type = matches[3]
        if line.find("FI") != -1:
            days = re.findall("\d+/\d+/\d+$" ,matches[7])[0]
        else:
            days = matches[7]
        startTime = self.convertTo24hr(matches[8][:matches[8].find("-")])
        endTime = self.convertTo24hr(matches[8][matches[8].find("-")+1:])
        location = matches[9] + " " + matches[10]
        
        self.eventInfo.append({"className": self.className, "type":type, "days":days, "startTime":startTime, "endTime":endTime, "location":location})
    