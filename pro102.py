#Reminder for medicine, set alarms, click my picture

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
    print("Picture Taken")
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

    dailyTasks=input("Enter list of tasks in order for today(separated by space-->5): ")
    task_list=dailyTasks.split()
    i = 0
    while i < len(task_list):
        task=input("Enter alarm for the task: ")
        print("Alarm is set for", task_list[i],"at", task)
        i = i + 1
    

if task=="Reminder For Medicine":
    medicineReminder()
elif task=="Click My Picture":
    take_picture()
elif task=="Set Alarm":
    Alarms()
    





