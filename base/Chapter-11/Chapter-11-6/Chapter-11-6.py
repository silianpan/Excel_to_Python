import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-6-1.xlsx') #读取工作簿。
print(wb.worksheets) #返回所有工作表对象。
print([ws for ws in wb]) #返回所有工作表对象
print(wb.sheetnames) #返回所有工作表名。


