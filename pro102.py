#Reminder for medicine, wake me up on a certain day, click my picture

import time
import datetime
import cv2 
import random
from datetime import date

task=input("Enter the task you want to automate: ")

start_time=time.time()

def medicine():
    print("It is time to take your medicine.")
    start_time=time.time
    
def medicineReminder():
    while (True):
        if (time.time()-start_time) == 2*60*60:
            medicine()
            

def picture():
    cheese=input("Okay! Say Cheese: ")
    number= random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        for i in range(1,4):
            print (i)
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+ ".jpg"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        
        result=False
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def take_picture():
    while (True):
        if (time.time()-start_time) >= 3:
            picture()
            break

def Alarms():
    
    year=int(input("Enter current year: "))
    month=int(input("Enter current month(number): "))
    date_today=int(input("Enter todays date(only the day): "))

    week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    week_num=datetime. date(year,month,date_today). weekday()
    day_today=(week_days[week_num])
    print("Today is a", day_today)

    
    taskToday=input("Enter the task you want to set the alarm for(classes/evening walk/dinner/prayers): ")
    if taskToday=="Classes":
        print("Your alarm is set for 1pm today.")
            
    elif taskToday=="Evening Walk":
        print("Your alarm is set for 5pm today.")
            
    elif taskToday=="Dinner":
        print("Your alarm is set for 9pm today.")
            
    elif taskToday=="Prayers":
        print("Your alarm is set at 2:30pm for your prayers today.")
        

if task=="Reminder For Medicine":
    medicineReminder()
elif task=="Click My Picture":
    take_picture()
elif task=="Set Alarm":
    Alarms()
    




