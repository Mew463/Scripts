import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

PATH = r'C:\Users\mingw\Documents\Scripts\Python\chromedriver.exe'
Website1 = "https://wonderland.tf/threads/staff-list.5570/"
Website2 = "https://bans.wonderland.tf/?p=servers"
ILNum = 113 #NUMBER FOR GET NUMBER OF PLAYERS
NYNum = 73 #NUMBER FOR GET NUMBER OF PLAYERS
xPathTableNameIL = f"/html/body/div[3]/div/div[4]/div/table/tbody/tr[{ILNum}]"
xPathTableNameNY = f"/html/body/div[3]/div/div[4]/div/table/tbody/tr[{NYNum}]/td[4]"


option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(PATH,options=option)

serverNameList = []
consoleNameList = []

def serverNameGetter(server):
    if server == "NY":
        serverPath = xPathTableNameNY
        num = NYNum+1
    else:
        serverPath = xPathTableNameIL 
        num = ILNum+1
    
    driver.get(Website2)
    time.sleep(4) #delay to allow the page to load
    #Calculate rows in table
    rows = len(driver.find_elements_by_xpath(f"/html/body/div[3]/div/div[4]/div/table/tbody/tr[{num}]/td/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr"))
    print("Number of players = " + str(rows-1))
    driver.find_element_by_xpath(serverPath).click()

    time.sleep(1)
    #Print all names of people
    for i in range(2,rows):
        name = driver.find_element_by_xpath(f"/html/body/div[3]/div/div[4]/div/table/tbody/tr[{num}]/td/div/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr[{i}]/td[1]").text
        serverNameList.append(name)
    print("======Players in server======")
    print(serverNameList)
    driver.quit()

def namesFromConsole():
    f = open(r"C:\Users\mingw\Documents\Scripts\Python\Current Players.txt", encoding="utf8")
    
    lines = f.readlines()
    for line in lines:
        i = 0
        firstQuotationMark = -1
        for text in line:
            i+=1
            if text == '"':
                if firstQuotationMark == -1:
                    firstQuotationMark = i
                else:
                    consoleNameList.append(line[firstQuotationMark:i-1])
    print(consoleNameList)
            

def playerChecker():
    adminOnline = 0
    for n in serverNameList: 
        if n not in consoleNameList:
            print("Admin currently online: " + n)
            adminOnline = 1

    if adminOnline == 0:
        print("No admins online")
        
namesFromConsole()
serverNameGetter("IL") 
playerChecker()


time.sleep(1)   
driver.quit()

