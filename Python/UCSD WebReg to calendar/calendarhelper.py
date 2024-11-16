from gcsa.event import Event
from gcsa.calendar import Calendar
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import *

from beautiful_date import *
from datetime import timedelta, timezone
D = MDY()

gc = GoogleCalendar(credentials_path='credentials.json') 

class calendarHelper:
    def __init__(self, first_day_of_classes, last_day_of_classes):
        self.first_day_of_classes = first_day_of_classes
        self.last_day_of_classes = last_day_of_classes    

    def getCalendarId(self, name):
        for calendar in gc.get_calendar_list():
            if calendar.summary == name:
                return calendar.id

    def addTestCalendar():
        calendar = Calendar("test calendar", description = "used for testing")
        calendar = gc.add_calendar(calendar)

    def deleteEventsInCalendar(self, calendarname): # Present day -> One year forward; Only delete Events made by bot
        first_day_of_class_date = datetime.strptime(self.first_day_of_classes, "%m/%d/%Y").replace(tzinfo=timezone.utc)
        
        # offset = timedelta(seconds=-25200)
        # timezone_with_offset = timezone(offset)
        # first_day_of_class_date = first_day_of_class_date.replace(tzinfo=timezone_with_offset)
        for event in gc.get_events(calendar_id=self.getCalendarId(calendarname)):
            if event.description == "Created by Python!" and event.start.astimezone(timezone.utc) > first_day_of_class_date:
                print(f"deleting {event.summary}")
                gc.delete_event(event, calendar_id=self.getCalendarId(calendarname))
            
    def addEvent(self,name,type,startTime,endTime,days,location): 
        targetCalendar = "Classes"
        days = self.fixDays(days)
        
        if type != "FI": # For non finals (items that are reocurring)
            start = datetime.strptime(f"{self.first_day_of_classes} {startTime}", "%m/%d/%Y %H:%M")
            end = datetime.strptime(f"{self.first_day_of_classes} {endTime}", "%m/%d/%Y %H:%M")
            
            start_day_enum = start.weekday()
            
            # Need to find the actually first day that we can put the event. It needs to be the first day that the class occurrs.

            foundStartingDay = False
            for day in days: # these are the days of the week that it reoccurrs
                event_day_enum = [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY].index(day)
                if event_day_enum >= start.weekday(): # it starts ocurring AFTER the start of classes, then we good
                    start = start - timedelta(days = start_day_enum) + timedelta(days = event_day_enum)
                    end = end - timedelta(days = start_day_enum) + timedelta(days = event_day_enum)
                    foundStartingDay = True
                    break
                    
            if foundStartingDay == False: # it never ocurrs AFTER the start of classes, lets offset by a week and start on the following Monday
                start = start - timedelta(days = start_day_enum) + timedelta(days = [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY].index(days[0]) + 7)
                end = end - timedelta(days = start_day_enum) + timedelta(days = [MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY].index(days[0]) + 7)
            
            until = datetime.strptime(self.last_day_of_classes, "%m/%d/%Y") + timedelta(days = 1)
            event = Event(f'{name} {type}', start=start, end=end, recurrence = Recurrence.rule(freq= WEEKLY, by_week_day = days, until = until), description="Created by Python!", location=location)
            event = gc.add_event(event)
            event = gc.move_event(event, self.getCalendarId(targetCalendar))
            print(f"Successfully created {event.summary}")
        else:
            start = datetime.strptime(f"{days} {startTime}", "%m/%d/%Y %H:%M")
            end = datetime.strptime(f"{days} {endTime}", "%m/%d/%Y %H:%M")
            event = Event(f'{name} FINAL', start=start, end=end, description="Created by Python!", location=location)
            event = gc.add_event(event)
            event = gc.move_event(event, self.getCalendarId(targetCalendar))
            print(f"Successfully created {event.summary}")
    
    def fixDays(self, text):
        days = []
        targets = [["M", "Tu", "W", "Th", "F"], [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY]]
        for i in range(5):
            if text.find(targets[0][i]) != -1:
                days.append(targets[1][i])
        if not days:
            days = text
        return days
    
# test = calendarHelper("02/12/2024", "03/12/2024")
# test.deleteEventsInCalendar("test calendar")
# test.addTestCalendar
# test.addEvent("ECE 10000", "LE", "9:00", "10:00", [MONDAY,WEDNESDAY], "some location")