import xlwt #导入xlwt库。
year_num=2015 #初始化year_num变量为年份数。
while year_num<=2019: #判断如果year_num小于等于2019则执行循环。
    year_name='{}年.xls'.format(year_num) #格式化年份数为工作簿名。
    nwb=xlwt.Workbook('utf-8') #新建工作簿。
    year_num +=1 #对year_num变量累加1。
    month_num=1 #初始化month_num变量为月份数。
    while month_num<=12: #判断如果month_num小于等于12则执行循环。
        month_name='{}月份'.format(month_num) #格式化月份数为工作表名。
        nws=nwb.add_sheet(month_name) #新建工作表。
        month_num +=1 #对month_num变量累加1。
    nwb.save(year_name) #保存工作簿。
