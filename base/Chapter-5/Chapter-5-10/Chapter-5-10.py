import xlrd,xlwt #导入读取与写入xls文件的库。
wb=xlrd.open_workbook('Chapter-5-10-1.xls') #读取工作簿。
nwb=xlwt.Workbook('utf-8') #新建工作簿。
nws=nwb.add_sheet('统计结果') #新建工作表。
nws.write(0,0,'时间');nws.write(0,1,'次数') #在新工作表中创建表头。
new_row_num,num=0,0 #初始化new_row_num和num变量为0。
for ws in wb.sheets(): #循环读取工作簿下的所有工作表。
    for row_num in range(1,ws.nrows): #循环读取工作表下的每行。
        if '问问梅' in ws.row_values(row_num): #判断如果'问问梅'在每行中有出现。
            num +=1 #则对num变量累加1。
    new_row_num +=1 #对new_row_num变量累加与做写入数据时的行号。
    nws.write(new_row_num,0,ws.name) #将循环出来的工作表名写入新表A列。
    nws.write(new_row_num,1,num) #将num变量的值写入新表B列。
    num=0 #重置num变量，方便后续循环时的重新计数。
nwb.save('Chapter-5-10-2.xls') #保存新建的工作簿。