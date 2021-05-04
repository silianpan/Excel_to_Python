import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-8-1.xlsx') #读取工作簿。
wb.copy_worksheet(wb['1月']) #复制工作表，工作表名默认。
nws=wb.copy_worksheet(wb['2月']);nws.title='2月份' #复制工作表，并重命名。
wb.copy_worksheet(wb['3月']).title='3月份' #复制工作表，并重命名。
wb.save('Chapter-11-8-2.xlsx') #另保存工作簿。


