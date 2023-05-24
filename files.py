import openpyxl as op
import os
import datetime
import pandas as pd
import numpy as np
def create(id):
    wb=op.Workbook()
    wb.create_sheet("book") 
    ws=wb["book"]
    ws.append(("ID","Name","Date","Finished"))
    wb.create_sheet("reminder")
    ws=wb["reminder"]
    ws.append(("ID","Reminder","Date","Finished"))
    wb.save(filename="{id}.xlsx".format(id=id))

def create_list(name,id):
    if os.path.exists(str(id)+".xlsx"):
        wb=op.load_workbook(str(id)+".xlsx")
    else:
        wb=op.Workbook()
    wb.create_sheet(name) 
    ws=wb[name]
    ws.append(("ID","Name","Date","Finished"))
    wb.save(filename="{id}.xlsx".format(id=id))

def remove_list(list_id,id):
    wb=op.load_workbook(str(id)+".xlsx")
    list_name=wb.sheetnames[list_id]
    wb.remove_sheet(list_name)
    wb.save(filename="{id}.xlsx".format(id=id))

def show_list(id):
    wb=op.load_workbook(str(id)+".xlsx")
    list_names=wb.sheetnames
    string="\n"
    for list in list_names[1:]:
        string+=str(list_names.index(list))+"-"+list+"\n"
    return string

def get_list(id):
    wb=op.load_workbook(str(id)+".xlsx")
    list_names=wb.sheetnames[1:]
    return list_names

def get_help():
    with open("variables.py","r") as f:
        lines=f.readlines()
    help=""
    for line in lines:
        help+=line
    return help

def add_element(list_name,info,id):
    wb=op.load_workbook(str(id)+".xlsx")
    ws=wb[list_name]
    ws.append((str(ws.max_row),info.capitalize(),datetime.date.today(),"N"))
    wb.save(filename="{id}.xlsx".format(id=id))

def show_element(list_name,id):
    df=pd.read_excel(str(id)+".xlsx",sheet_name=list_name)
    pos=np.where(df["Finished"]=="N")[0]
    books=""
    for i in pos:
        books+=str(df["ID"].iloc[i])+"->"+str(df["Name"].iloc[i])+"\n"
    return books