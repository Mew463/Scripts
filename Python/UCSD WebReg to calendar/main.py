from gcsa.event import Event
from gcsa.calendar import Calendar
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import *

from beautiful_date import *
import dataparser as dataparser
from datetime import timedelta
D = MDY()

# Copy and paste directly from webreg list into Classes.txt
first_day_of_classes = "01/08/2024"
last_day_of_classes = "03/15/2024"

gc = GoogleCalendar(credentials_path="credentials.json")

def getCalendarId(name):
    for calendar in gc.get_calendar_list():
        if calendar.summary == name:
            return calendar.id

def addTestCalendar():
    calendar = Calendar("test calendar", description = "used for testing")
    calendar = gc.add_calendar(calendar)

def deleteEventsInCalendar(calendarname): # Present day -> One year forward; Only delete Events made by bot
    for event in gc.get_events(calendar_id=getCalendarId(calendarname)):
        if event.description == "Created by Python!":
            print(f"deleting {event.summary}")
            gc.delete_event(event, calendar_id=getCalendarId(calendarname))
        
def addEvent(name,type,startTime,endTime,days,location): 
    if type != "FI":
        # adjusted_first_day_of_classes = int(re.findall("/\d\d/", first_day_of_classes)[0])
        start = datetime.strptime(f"{first_day_of_classes} {startTime}", "%m/%d/%Y %H:%M")
        end = datetime.strptime(f"{first_day_of_classes} {endTime}", "%m/%d/%Y %H:%M")
        
        start = start + timedelta(days = [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY].index(days[0]))
        end = end + timedelta(days = [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY].index(days[0]))
        
        until = datetime.strptime(last_day_of_classes, "%m/%d/%Y") + timedelta(days = 1)
        event = Event(f'{name} {type}', start=start, end=end, recurrence = Recurrence.rule(freq= WEEKLY, by_week_day = days, until = until), description="Created by Python!", location=location)
        event = gc.add_event(event)
        event = gc.move_event(event, getCalendarId("Classes"))
        print(f"Successfully created {event.summary}")
    else:
        start = datetime.strptime(f"{days[0]} {startTime}", "%m/%d/%Y %H:%M")
        end = datetime.strptime(f"{days[0]} {endTime}", "%m/%d/%Y %H:%M")
        event = Event(f'{name} FINAL', start=start, end=end, description="Created by Python!", location=location)
        event = gc.add_event(event)
        event = gc.move_event(event, getCalendarId("Classes"))
        print(f"Successfully created {event.summary}")
    
deleteEventsInCalendar("Classes")

lines = open("Classes.txt", "r")
classLines = []
curLine = 0
lastLine = 0
for line in lines:
    if line.find("FI") != -1:
        classLines.append((lastLine, curLine))
        lastLine = curLine+1
    curLine = curLine + 1

for i in range(0,len(classLines)):
    currentClass = dataparser.ClassInfo(classLines[i][0], classLines[i][1])
    currentClass.getData()
    for x in range(0, len(currentClass.eventInfo)):
        addEvent(currentClass.eventInfo[x]["className"], 
                 currentClass.eventInfo[x]["type"], 
                 currentClass.eventInfo[x]["startTime"], 
                 currentClass.eventInfo[x]["endTime"],
                 currentClass.eventInfo[x]["days"],
                 currentClass.eventInfo[x]["location"],
                 )
        
# addEvent("ECE 10000", "LE", "9:00", "10:00", [MONDAY,WEDNESDAY], "some location")
# addEvent("ECE 10000", "FI", "9:00", "10:00", "12/30/2023", "some location")