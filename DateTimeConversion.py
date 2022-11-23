import datetime

'''
datetime is a module in python, that provides us with 6 classes, which has multiple useful functions.
We dont need to install this module seperately, it comes with the default installation of python. 

Classes given by datetime module are given below:
1- date
2- time
3- datetime
4- timedelta
5- tzinfo
6- timezone

every class has many functions and we will explore all of them InshAllah

'''

# Date class
def getDate():
    date = datetime.date(1997,10,10)
    print("date is: ", date)
    print("Type of date is: ",type(date))

    # Uncommenting my_date = date(1996, 12, 39)
    # will raise an ValueError as it is
    # outside range
    
    # uncommenting my_date = date('1996', 12, 11)
    # will raise a TypeError as a string is
    # passed instead of integer



def getTime():

    time = datetime.time(hour = 11,minute = 34, second = 56, microsecond=11)
    print("Hours: " , time.hour)
    print("Minutes: ", time.minute)
    print("Seconds: ", time.second)
    print("Microseconds: ", time.microsecond)


def convertingTimeObjectIntoString():
    time = datetime.time(hour = 11,minute = 34, second = 56, microsecond=11)
    print("Hours: " , time.hour)
    print("Minutes: ", time.minute)
    print("Seconds: ", time.second)
    print("Microseconds: ", time.microsecond)
    print(type(time.hour))
    print(type(time))
    timeInStr = time.isoformat()
    # Seconds will be caluclated upto 6 decimal digits (Microseonds) 
    print("Time in String object is: ", timeInStr, " Type of this time is: ", type(timeInStr))


def convetingStringTimeObjectintoTimeClassObject():
    time = datetime.time(hour = 11,minute = 34, second = 56, microsecond=11)
    print("Hours: " , time.hour)
    print("Minutes: ", time.minute)
    print("Seconds: ", time.second)
    print("Microseconds: ", time.microsecond)
    print(type(time.hour))
    print(type(time))
    timeInStr = time.isoformat()
    # Seconds will be caluclated upto 6 decimal digits (Microseonds) 
    print("Time in String object is: ", timeInStr, " Type of this time is: ", type(timeInStr))

    timeObjectConversion = datetime.time.fromisoformat(timeInStr)
    print(type(timeObjectConversion))
# getDate()
# getTime()

convetingStringTimeObjectintoTimeClassObject()