import openpyxl #导入库。
for name in ['北京','天津','成都','苏州']: #循环要提取的工作表名。
    wb=openpyxl.load_workbook('Chapter-11-13-1.xlsx') #读取工作簿。
    for ws in wb.worksheets: #循环工作簿下的所有工作表，并赋值给ws变量。
        if ws.title!=name: #判断ws的工作表名如果不等于要提取的工作表名。
            wb.remove(ws) #那么则删除ws工作表。
    wb.save(name+'.xlsx') #另存工作簿。







