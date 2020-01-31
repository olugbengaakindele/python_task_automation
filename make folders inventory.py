# this scripts create a folder with multiple subfolders etc Year-months-Weeks-multiple subjects
import os, time
import datetime
from os import path
from calendar import monthrange
from datetime import  date




main_path = (r'O:\Systems\Olu')
year = '2020'

#check if year folder exist
year_path = os.path.join(main_path, year)
if os.path.isdir(year_path):
    #if folder exisit do nothing
    #create months
    for i in range(1,13):
        mth_date = year + "." + str(i) + ".1"
        mydate = datetime.datetime.strptime(mth_date, '%Y.%m.%d')
        mth  = str(i) + ". " + mydate.strftime("%B")
        mth_path = os.path.join(year_path,mth)
        
        if not os.path.isdir(mth_path):
            os.mkdir(mth_path)
            day_month =monthrange(int(year), i)[1]
            for x in range(1 , day_month+1):
                each_date  = year + "." + str(i).zfill(2) + "." + str(x).zfill(2)
                dates_of_month = datetime.datetime.strptime(each_date, '%Y.%m.%d')
                #check if the date is a monday and then check if folder exists
                if dates_of_month.weekday() == 0:
                    week_folder = os.path.join(year_path,mth,"WK_BG_" + each_date)
                    if not os.path.isdir(week_folder):
                        os.mkdir(week_folder)
                        F1 = os.path.join(week_folder,"Available Inventory Output")
                        F2 = os.path.join(week_folder,"Heritage ON Inventory")
                        F3 = os.path.join(week_folder,"Heritage BC Inventory")
                        F4 = os.path.join(week_folder,"PNP Inventory")
                        if not os.path.isdir(F1):
                            os.mkdir(F1)

                        if not os.path.isdir(F2):
                            os.mkdir(F2)

                        if not os.path.isdir(F3):
                            os.mkdir(F3)

                        if not os.path.isdir(F4):
                            os.mkdir(F4)

                
        else:
            day_month =monthrange(int(year), i)[1]
            for x in range(1 , day_month+1):
                each_date  = year + "." + str(i).zfill(2) + "." + str(x).zfill(2)
                dates_of_month = datetime.datetime.strptime(each_date, '%Y.%m.%d')
                #check if the date is a monday and then check if folder exists
                if dates_of_month.weekday() == 0:
                    week_folder = os.path.join(year_path,mth,"WK_BG_" + each_date)
                    if not os.path.isdir(week_folder):
                        os.mkdir(week_folder)
                        F1 = os.path.join(week_folder,"Available Inventory Output")
                        F2 = os.path.join(week_folder,"Heritage ON Inventory")
                        F3 = os.path.join(week_folder,"Heritage BC Inventory")
                        F4 = os.path.join(week_folder,"PNP Inventory")
                        if not os.path.isdir(F1):
                            os.mkdir(F1)

                        if not os.path.isdir(F2):
                            os.mkdir(F2)

                        if not os.path.isdir(F3):
                            os.mkdir(F3)

                        if not os.path.isdir(F4):
                            os.mkdir(F4)
else:
    #create the folder for year
    os.mkdir(year_path)
    #create months
    for i in range(1,13):
        mth_date = year + "." + str(i) + ".1"
        mydate = datetime.datetime.strptime(mth_date, '%Y.%m.%d')
        mth  = str(i) + ". " + mydate.strftime("%B")
        mth_path = os.path.join(year_path,mth)
        #create month folder
        os.mkdir(mth_path)
        day_month =monthrange(int(year), i)[1]
        for x in range(1 , day_month+1):
            each_date  = year + "." + str(i).zfill(2) + "." + str(x).zfill(2)
            dates_of_month = datetime.datetime.strptime(each_date, '%Y.%m.%d')
            #check if the date is a monday and then check if folder exists
            if dates_of_month.weekday() == 0:
                week_folder = os.path.join(year_path,mth,"WK_BG_" + each_date)
                if not os.path.isdir(week_folder):
                    os.mkdir(week_folder)
                    F1 = os.path.join(week_folder,"Available Inventory Output")
                    F2 = os.path.join(week_folder,"Heritage ON Inventory")
                    F3 = os.path.join(week_folder,"Heritage BC Inventory")
                    F4 = os.path.join(week_folder,"PNP Inventory")
                    if not os.path.isdir(F1):
                        os.mkdir(F1)

                    if not os.path.isdir(F2):
                        os.mkdir(F2)

                    if not os.path.isdir(F3):
                        os.mkdir(F3)

                    if not os.path.isdir(F4):
                        os.mkdir(F4)
                    
       
