import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-12-1.xlsx') #读取工作簿。
for year in range(2020,2024): #循环2020~2023数字给year变量。
    wsname='{}年'.format(year) #格式化工作表名。
    wb.copy_worksheet(wb['业绩表']).title=wsname #复制'业绩表'工作表，并重命名。
wb.remove(wb['业绩表']) #删除'业绩表'工作表。
wb.save('Chapter-11-12-2.xlsx') #另存工作簿。
