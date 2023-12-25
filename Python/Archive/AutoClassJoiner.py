import webbrowser
import schedule
import time
import pyperclip
from datetime import datetime
MonThruThursday = ["08:40", "09:51", "11:35", "12:46", ]
Fridays = ["08:40","10:11","11:50","12:55", ]
SpecialDay = ["08:40","09:45","11:55","12:55", ] 

ClassName = ["ECE 5", "ENG 15", "Suite Acitvity", "Suite Meeting"]
url = [
    "https://meet.google.com/lookup/dne7cgjac2?authuser=1&hs=179",
    "https://meet.google.com/lookup/dptyyxtbx2?authuser=1&hs=179",
    "https://meet.google.com/lookup/eiur6atnru?authuser=1&hs=179",
    "https://meet.google.com/lookup/auchg4uran?authuser=1&hs=179",
    ]

def job():
    now = datetime.now()
    dt_string = now.strftime("%H:%M")
    print("Time =", dt_string)

    try:
        index = MonThruThursday.index(dt_string)
        print("Mon-Thursday, correct time found at", index+1)
    except ValueError:
        try:
            index = Fridays.index(dt_string)
            print("Friday, correct time found at", index)
        except ValueError:
            print("Time not found.")
            try:
                index = SpecialDay.index(dt_string)
                print("Specialday, correct time found at", index)
            except ValueError:
                return

    webbrowser.open_new_tab(url[index])
    pyperclip.copy(url[index])
    print("Joining " + ClassName[index] + " ...")


for meettime in MonThruThursday:
    schedule.every().monday.at(meettime).do(job)
    schedule.every().tuesday.at(meettime).do(job)
    schedule.every().wednesday.at(meettime).do(job)
    #schedule.every().thursday.at(meettime).do(job)

#for meettime in SpecialDay:
    #schedule.every().monday.at(meettime).do(job)
    #schedule.every().tuesday.at(meettime).do(job)
    #schedule.every().wednesday.at(meettime).do(job)
    #schedule.every().thursday.at(meettime).do(job)
    #schedule.every().friday.at(meettime).do(job)

#for meettime in Fridays:
    #schedule.every().friday.at(meettime).do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
