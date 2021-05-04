import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-7-1.xlsx') #读取工作簿。
print(wb.active) #读取活动工作表。
print(wb.worksheets[1]) #按顺序读取第1个工作表。
print(wb['1月']) #读取指定工作表。
