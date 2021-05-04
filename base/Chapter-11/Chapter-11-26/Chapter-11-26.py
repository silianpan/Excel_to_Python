import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-26-1.xlsx',data_only=True) #读取工作簿。
ws=wb.worksheets[0] #读取工作表。
for cell in ws['F'][1:]: #循环将F列的单元格对象赋值给cell变量。
    if cell.value<270: #如果单元格的值小于270。
        ws.delete_rows(cell.row) #则删除单元格所在行。
wb.save('Chapter-11-26-2.xlsx') #另存工作簿。
