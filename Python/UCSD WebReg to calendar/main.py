import dataparser as dataparser
import calendarhelper as ch

"""
Configuring Google Calendar AUTH 
1) Go here: https://console.cloud.google.com/apis/credentials?project=ucsd-web-reg-2
2) Download Web Client 1's credentials.json file and put in project directory 
3) DELETE token.pickle file!!! SO WEB BROWSER REAUTHENTICATES
4) (If not already done) Add "http://localhost:8080/" to Authorized redirect URIs
"""

# Copy and paste directly from webreg list into Classes.txt
first_day_of_classes = "01/06/2025"
last_day_of_classes = "03/14/2025"
    
mycalendar = ch.calendarHelper(first_day_of_classes, last_day_of_classes) 

def formatRawClassData():
    lines = open("TextFiles/RawClasses.txt", "r")
    classLines = [] # An array of tuples that give the line numbers pertaining to each class
    curLine = 0
    lastLine = 0
    foundFirstLine = False
    
    for line in lines:
        if foundFirstLine == False: # Make sure we find the first line (account for new lines before the first class)
            if (line[0] == '\n'): 
                lastLine = curLine = curLine + 1
                continue
            else: # Its not a newline, its actually something!
                foundFirstLine = True
                curLine = curLine + 1
                continue
        
        if line[0] != ' ' and line.find("Expand:")== -1: # This is true if we find the NEXT class
            classLines.append((lastLine, curLine-1))
            lastLine = curLine
        curLine = curLine + 1

    classLines.append((lastLine, curLine-1))
    print(classLines)
    
    lines = open("TextFiles/Events.txt", "a")
    for i in range(0,len(classLines)):
        currentClass = dataparser.ClassInfo(classLines[i][0], classLines[i][1])
        currentClass.getData()
        for eventCharacteristic in currentClass.eventInfo:
            lines.write(f"{eventCharacteristic['className']}, {eventCharacteristic['type']}, {eventCharacteristic['startTime']}, {eventCharacteristic['endTime']}, {eventCharacteristic['days']}, {eventCharacteristic['location']}\n")
    lines.write("# ----------------------Custom Definitions Below------------------------\n")

def addClassesToCalendar():
    lines = open("TextFiles/Events.txt", "r")
    for line in lines:
        if line[0] == '#': # Skip if there's a #
            continue 
        lastIndex = 0
        info = []
        while (lastIndex != -1):
            curIndex = line.find(",", lastIndex + 1)
            info.append(line[lastIndex:curIndex].strip())
            if curIndex != -1:
                lastIndex = curIndex+1
            else:
                lastIndex = curIndex
        mycalendar.addEvent(info[0], info[1], info[2], info[3], info[4], info[5])

# formatRawClassData()
# mycalendar.deleteEventsInCalendar("Classes")
addClassesToCalendar()

