import Xlib
import pyautogui
import self as self
from datetime import datetime

self.__display = Xlib.display.Display()
current_time = ''
whichDay = 'A'
dayFlipped = False
listOfHolidays = ["01/18","02/15","03/08","03/09","03/10","03/11","03/12","04/02","04/05","04/23","05/22","05/31"]
weatherDaysDeactivated = 0


def joinClass(code, password, starttime):
    if starttime == current_time:
        # pyautogui.click(70, 1060)
        # pyautogui.sleep(4)
        #pyautogui.click(970, 380)
        pyautogui.click(pyautogui.locateCenterOnScreen('join.png'))
        pyautogui.sleep(1)
        #pyautogui.click(970, 450)
        #pyautogui.sleep(1)
        # pyautogui.write(code)
       # pyautogui.sleep(1)
        #pyautogui.click(970, 410)
        #pyautogui.sleep(1)
        # pyautogui.write(code)
        #pyautogui.sleep(1)
        #pyautogui.click(970, 370)
        #pyautogui.sleep(1)
        #pyautogui.click(970, 335)
        #pyautogui.sleep(1)
        #pyautogui.click(970, 318)
        #pyautogui.sleep(1)
        # pyautogui.click(970,272)
        # pyautogui.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen('meetingid.png'))
        pyautogui.sleep(1)
        pyautogui.write(code)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pyautogui.press('esc')
        pyautogui.sleep(3)
        if len(password) > 1:
            pyautogui.write(password)
            pyautogui.sleep(1)
            pyautogui.press('enter')
        pyautogui.sleep(480)
        pyautogui.press('esc')
        pyautogui.sleep(1)
        pyautogui.press('esc')
        pyautogui.sleep(5010)
        pyautogui.click(pyautogui.locateCenterOnScreen('leave.png'))
        #pyautogui.click(1900, 1060)
        pyautogui.sleep(2)
        pyautogui.press('esc')
        pyautogui.sleep(1)
        pyautogui.press('esc')
        # pyautogui.sleep(6)
        # pyautogui.click(1790, 18)


def changeDayType():
    global dayFlipped
    global whichDay
    whichDayOfficial = open('Day', 'r')
    whichDay = whichDayOfficial.read()
    whichDayOfficial.close()
    if True:#current_time == "00:00" and dayFlipped == False:
        dayFlipped = True
        if True:#datetime.today().weekday() < 4 or datetime.today().weekday() == 6:
            valueOfToday: str = str(datetime.today().month) + "/" + str(datetime.today().day)
            switchDay = True
            for day in listOfHolidays:
                if day == valueOfToday:
                    if (weatherDaysDeactivated == 1 and day == '04/05') or (weatherDaysDeactivated == 2 and day == '04/05' or '04/23'):
                        print('today is a make up day')
                    else:
                        switchDay = False
            if switchDay:
                if whichDay == 'A':
                    whichDay = 'B'
                else:
                    whichDay = 'A'
            else:
                whichDay = 'H'
    if current_time == "00:01":
        dayFlipped = False
    whichDayOfficial = open('Day','w')
    whichDayOfficial.write(whichDay)
    whichDayOfficial.close()

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    changeDayType()
    # A Day
    if whichDay == 'A':
        joinClass('5740536209', "Bakerland", "08:45")
        joinClass('84605087324', "smith2020","11:20")
        joinClass('84053243511', "Z2Mzek1WZjBhd04yNlBRNDNrQitBZz09","12:55")

    # B Day
    if whichDay == 'B':
        joinClass('92144334702', "", "07:00")
        joinClass('91505416920', "ZnFseGN2Um81NjJPSEFmNE43clR2UT09", "08:35")
        joinClass('8713292954', "NzQrRUJlbENUWFdobkIvWkQ5QlFkUT09", "11:20")

    # Test Links
    joinClass('99084651314', "", "22:40")
    pyautogui.sleep(12)
