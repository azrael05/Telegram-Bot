import openpyxl as op
import datetime
import pandas as pd
import numpy as np
import os
from files import create

def add_reminder(reminder,id):
    if not os.path.exists(str(id)+".xlsx"):
        create(id)
    wb=op.load_workbook("{id}.xlsx".format(id=id))
    wb.active=wb["reminder"]
    ws=wb.active
    ws.append((str(ws.max_row+1),reminder[1:].capitalize(),datetime.date.today(),"N"))
    wb.save(filename="{id}.xlsx".format(id=id))
    

def show_reminder(id):
    df=pd.read_excel(str(id)+".xlsx",sheet_name="reminder")
    pos=np.where(df["Finished"]=="N")[0]
    reminder=""
    for i in pos:
        reminder+=str(df["ID"].iloc[i])+"->"+str(df["Reminder"].iloc[i])+"\n"
    return reminder



def count_reminders(id):
    df=pd.read_excel(str(id)+".xlsx",sheet_name="reminder")
    pos=np.where(df["Finished"]=="N")[0]
    count=pos.shape[0]
    return count



def finish_reminder(rem_id,id):
    wb=op.load_workbook(str(id)+".xlsx")
    ws=wb["reminder"]
    for i in range(ws.max_row):
        if ws.cell(row=i,column=1)==str(rem_id):
            ws.cell(row=i,column=4).value("Y")