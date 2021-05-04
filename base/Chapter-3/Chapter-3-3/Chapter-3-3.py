import xlwt#导入xlwt
for month_num in range(1,13):#循环1到13之间的数字
    month_name = '{}月份.xls'.format(month_num)#格式化数字为工作簿名
    nwb=xlwt.Workbook('utf-8')#新建工作簿
    nwb.add_sheet(month_name)#在工作簿中新建工作表
    nwb.save(month_name)#保存工作簿










