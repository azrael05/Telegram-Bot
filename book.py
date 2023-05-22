import os
from files import create
import openpyxl as op
import datetime
import pandas as pd
import numpy as np
## Columns "ID","Name","Date","Finished"

def add_book(book_name,id):
    if not os.path.exists(str(id)+".xlsx"):
        create(id)
    wb=op.load_workbook("{id}.xlsx".format(id=id))
    wb.active=wb["book"]
    ws=wb.active
    ws.append((str(ws.max_row+1),book_name[1:].capitalize(),datetime.date.today(),"N"))
    wb.save(filename="{id}.xlsx".format(id=id))


def show_books(id):
    df=pd.read_excel(str(id)+".xlsx",sheet_name="book")
    pos=np.where(df["Finished"]=="N")[0]
    books=""
    for i in pos:
        books+=str(df["ID"].iloc[i])+"->"+str(df["Name"].iloc[i])+"\n"
    return books

def count_books(id):
    df=pd.read_excel(str(id)+".xlsx",sheet_name="book")
    pos=np.where(df["Finished"]=="N")[0]
    count=pos.shape[0]
    return count

def finish_book(book_id,id):
    wb=op.load_workbook(str(id)+".xlsx")
    ws=wb["book"]
    for i in range(ws.max_row):
        if ws.cell(row=i,column=1)==str(book_id):
            ws.cell(row=i,column=4).value="Y"
    wb.save(filename="{id}.xlsx".format(id=id))

def remove_book(book_id,id):
    df=pd.read_excel(str(id)+".xlsx")
    df.drop(np.where(df["ID"]==str(book_id))[0],axis=0)