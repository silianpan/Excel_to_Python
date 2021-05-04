import xlwt #导入xlwt库。
wb=xlwt.Workbook('utf-8') #新建工作簿。
year_num=2010 #初始化year_num变量为2010。
while year_num<2020: #如果year_num变量小于2020则执行while循环体的语句。
    txt='{}年业绩表'.format(year_num) #使用变量year_num格式化为工作表名称。
    wb.add_sheet(txt) #新建工作表。
    year_num +=1 #累加year_num变量。
wb.save('Chapter-3-8-1.xls') #保存工作簿。