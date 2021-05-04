import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-10-1.xlsx') #读取工作簿。
wb.remove(wb['1月']) #删除指定工作表。
wb.save('Chapter-11-10-2.xlsx') #另存工作簿。
