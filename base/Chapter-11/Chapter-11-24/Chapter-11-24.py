import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-24-1.xlsx');ws=wb.active #读取工作簿与工作表。
ws.insert_rows(2,3) #在第2行的上面插入3行空白行。
ws.insert_cols(3,1) #在第3列的前面插入1列空白列。
ws.delete_rows(10,3) #在第10行的上面删除3行数据。
ws.delete_cols(5,1) #在第5列的前面删除1列数据。
wb.save('Chapter-11-24-2.xlsx') #另存工作簿。

