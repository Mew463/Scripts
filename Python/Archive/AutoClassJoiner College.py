import webbrowser
import schedule
import time
import pyperclip
from datetime import datetime

class MyClasses:
  def __init__(self, name, time, url):
    self.name = name
    self.time = time
    self.url = url

LE1 = MyClasses('ECE 16', '08:59', 'https://ucsd.zoom.us/j/97407068391#success')
LE2 = MyClasses('PHYS 2A', '12:59', 'https://ucsd.zoom.us/j/98907014136#success')
LE4 = MyClasses('CHEM 6A', '07:59', 'https://urldefense.proofpoint.com/v2/url?u=https-3A__ucsd.zoom.us_j_94921220900&d=DwMGaQ&c=-35OiAkTchMrZOngvJPOeA&r=ZR5UGwVeTf7lvLvkoaucLg&m=Zlxraww8-Y1-EmT7qmk0kxoHhoBPipCdj5u2roEEIWmjd4LMo6C1LeXmoH3Rn0HE&s=NVVdHnEhEFCnsUFIJW9ndGqE4d608dDmy6nsTfGQyI8&e=')
DI1 = MyClasses('HUM 1', '15:59', 'https://ucsd.zoom.us/j/91277471662')
DI2 = MyClasses('Chem 6A discussion', '15:59', 'https://ucsd.zoom.us/j/94186932985#success')
DI3 = MyClasses('PHYS 2A discussion', '19:00', 'https://www.google.com/url?q=https://urldefense.proofpoint.com/v2/url?u%3Dhttps-3A__ucsd.zoom.us_j_94549691952%26d%3DDwMCaQ%26c%3D-35OiAkTchMrZOngvJPOeA%26r%3DZR5UGwVeTf7lvLvkoaucLg%26m%3DtdgBthTWU0jFoiTzGdweD1gWG6pyow3I2ToIakHYKC7svsVEXClAW-Qm5osQoHh1%26s%3DUB4GBrbAip9XZvIHGG2s4iIyosZZ0aqMQwSuaurgKjk%26e%3D&sa=D&source=calendar&ust=1642316803862182&usg=AOvVaw0xZxgSk1AxOVZp1UPs0_LU')
TUT = MyClasses('ECE 5 tutoring', '13:59', 'https://ucsd.zoom.us/s/95192013715#success')
QUIZ = MyClasses('PHYS 2A quiz', '16:58', 'https://ucsd.zoom.us/j/98907014136#success')

mondaySchedule = []
tuesdaySchedule = [DI1]
wednesdaySchedule = []
thursdaySchedule = [DI1]
fridaySchedule = [DI2, TUT]

def joinClass(dayList):
    now = datetime.now()
    dt_string = now.strftime("%H:%M")
    for a in dayList:
        if a.time == dt_string:
            print("Time =", dt_string)
            webbrowser.open_new_tab(a.url)
            pyperclip.copy(a.url)
            print(f"Joining {a.name} . . .")
            break
    
for classTime in mondaySchedule:
    schedule.every().monday.at(classTime.time).do(joinClass,mondaySchedule)
for classTime in tuesdaySchedule:
    schedule.every().tuesday.at(classTime.time).do(joinClass,tuesdaySchedule)
for classTime in wednesdaySchedule:
    schedule.every().wednesday.at(classTime.time).do(joinClass,wednesdaySchedule)
for classTime in thursdaySchedule:
    schedule.every().thursday.at(classTime.time).do(joinClass,thursdaySchedule)
for classTime in fridaySchedule:
    schedule.every().friday.at(classTime.time).do(joinClass,fridaySchedule)

while True:
    schedule.run_pending()
    time.sleep(1)
