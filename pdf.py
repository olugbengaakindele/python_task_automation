import os, time
from os import path
from os import walk
import PyPDF2,pyodbc
import datetime

conn = pyodbc.connect('Driver={SQL Server};Server=stayner-sql01\CRONOSSYSTEMS;Database=PCD;Trusted_Connection=yes;')
cursor = conn.cursor()
#lets set our all_data which will hold tthe data in a tabluar format but stored in pythin object first
lotNo = []
comment = {}
updated_by = 'Jordan'
Created_by = 'Jordan'

st_time = datetime.datetime.now()
a=0

path = (r"O:\Manufacturing\Production Control\Harvest Planning Report\2019")
os.chdir(path)

sub_fol = os.listdir(path)
#this  loop through the monthly folders in the working directory
for x in range(0, len(sub_fol)):
    
    month_fol = os.path.join(path,sub_fol[x])
    if os.path.isdir(month_fol):
        month_path =os.listdir( month_fol)
    
        #loop through sub folders in monthly folder i.e get the weekly folder
        for y in range(0,len(month_path)):
            weekly_path = os.path.join(month_fol,month_path[y])
           #loop through each week to find pDFS
            all_files_wk = os.listdir(weekly_path)
            os.chdir(weekly_path)
            for z in range(0, len(all_files_wk)):
                if all_files_wk[z].endswith(".pdf"):
                    #this get the date modified
                    mo_time = time.ctime(os.path.getmtime(all_files_wk[z]))
                    #mo_time = mo_time_long.strftime("%Y-%m-%d")
                    cr_time =  time.ctime(os.path.getmtime(all_files_wk[z]))
                    
                    lot_No = all_files_wk[z][0:4]
                    pdfFileObj = open(all_files_wk[z], 'rb')
                    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)    
                    pageObj = pdfReader.getPage(0)
                    lot_text = pageObj.extractText()
                    
                    if lot_text.find('Lot#') >= 0  :
                        print(lot_No)
                        comment = lot_text[lot_text.find('Lot#')+4 : lot_text.find('Failure')]
                        print(weekly_path + "-" + mo_time)
                        cursor.execute("INSERT INTO [PCD].[dbo].[PCD_batch_harvest_comments] ([batch_id],[comment],[created_by]) VALUES(?,?,?)", lot_No, comment,Created_by)
                        conn.commit()