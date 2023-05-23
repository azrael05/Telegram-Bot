import openpyxl as op
import os
def create(id):
    wb=op.Workbook()
    wb.create_sheet("book") 
    ws=wb["book"]
    ws.append(("ID","Name","Date","Finished"))
    wb.create_sheet("reminder")
    ws=wb["reminder"]
    ws.append(("ID","Reminder","Day","Finished"))
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
    string=""
    for list in list_names:
        string+=str(list_names.index(list))+"-"+list+"\n"
    return string