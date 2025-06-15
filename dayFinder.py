import sys
from datetime import date as dat

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def validDate(day,month,year):
    monthDays = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:81,9:30,10:31,11:30,12:31}

    if month < 1 or month > 12:
        return False

    if day < 1:
        return False
    
    if isLeapYear(year):
        if day -1 > monthDays[month]:
            return False
    else:
        if day > monthDays[month]:
            return False
        
    return True
        
date = dat.fromisoformat(input("Please enter date in ISO format YYYY-MM-DD => "))

if not validDate(date.day,date.month,date.year):
    print("Invalid Date")
    sys.exit()

monthKey = {1:1,2:4,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:4,12:6}

DOWList = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

centuryOffset = {1:4,2:2,3:0,0:6}

counter = int((date.year%100)/4) + date.day + monthKey[date.month] + centuryOffset[int(date.year/100)%4] + (date.year%100)

if date.month in [1,2]:
    if isLeapYear(date.year):
        counter = counter -1

offset = counter % 7

print (date,"will be a",DOWList[offset-1])
