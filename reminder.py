import openpyxl as op
import datetime
import pandas as pd
import numpy as np
import os
from files import create

## Columns "ID","Reminder","Day","Finished"


def add_reminder(reminder,id):
    if not os.path.exists(str(id)+".xlsx"):
        create(id)
    wb=op.load_workbook("{id}.xlsx".format(id=id))
    wb.active=wb["reminder"]
    ws=wb.active
    ws.append((str(ws.max_row),reminder[1:].capitalize(),datetime.date.today(),"N"))
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
    for i in range(1,ws.max_row+1):
        if ws.cell(row=i,column=1).value==str(rem_id):
            rem=ws.cell(row=i,column=2).value
            ws.cell(row=i,column=4).value="Y"
    wb.save(filename="{id}.xlsx".format(id=id))
    return rem


def remove_reminder(rem_id,id):
    wb=op.load_workbook(str(id)+".xlsx")
    ws=wb["book"]
    for i in range(1,ws.max_row+1):
        if ws.cell(row=i,column=1).value==str(rem_id):
            rem=ws.cell(row=i,column=2).value
            ws.delete_rows(i)
            break
    wb.save(filename="{id}.xlsx".format(id=id))
    return rem