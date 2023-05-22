import openpyxl as op

def create(id):
    wb=op.Workbook()
    wb.create_sheet("book")
    ws=wb["book"]
    ws.append(("ID","Name","Date","Finished"))
    wb.create_sheet("reminder")
    ws=wb["reminder"]
    ws.append(("ID","Reminder","Day","Finished"))
    wb.save(filename="{id}.xlsx".format(id=id))