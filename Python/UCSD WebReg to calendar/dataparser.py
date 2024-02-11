import re
from gcsa.recurrence import *

class ClassInfo:
    def __init__(self, startLine, endLine):
        self.eventInfo = [] # Data structure that holds EVERYTHING pertaining to one particular class    
        self.className = ""   
        self.startLine = startLine
        self.endLine = endLine
        
    def getData(self):
        lines =  open("UCSD WebReg to calendar/Classes.txt", "r")
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
   
    def fixDays(self, text):
        days = []
        targets = [["M", "Tu", "W", "Th", "F"], [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY]]
        for i in range(5):
            if text.find(targets[0][i]) != -1:
                days.append(targets[1][i])
        return days
        
            
    def extractLine(self, line):
        matches = []
        lastIndex = 0
        while (lastIndex != -1):
            curIndex = line.find("\t", lastIndex + 1)
            matches.append(line[lastIndex:curIndex].strip())
            lastIndex = curIndex
        # print(matches)
        if line.find("LE") != -1:
            self.className = matches[0]
        type = matches[3]
        if line.find("FI") != -1:
            days = re.findall("\d+/\d+/\d+$" ,matches[7])
        else:
            days = self.fixDays(matches[7])
        startTime = self.convertTo24hr(matches[8][:matches[8].find("-")])
        endTime = self.convertTo24hr(matches[8][matches[8].find("-")+1:])
        location = matches[9] + " " + matches[10]
        
        self.eventInfo.append({"className": self.className, "type":type, "days":days, "startTime":startTime, "endTime":endTime, "location":location})
    
# test = ClassInfo(0,2)
# test.getData()
# print(test.eventInfo[2]["days"])