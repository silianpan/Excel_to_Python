import xlrd #导入xlrd库。
from xlutils.copy import copy #导入xlutils库中的copy函数。
wb=xlrd.open_workbook('Chapter-3-17-1.xls') #读取工作簿。
ws=wb.sheet_by_name('分数表') #读取'分数表'工作表。
nwb=copy(wb) #复制工作簿。
nws=nwb.get_sheet('分数表') #读取工作簿副本中工作表。
col_vals=ws.col_values(1) #读取工作表中B列数据。
row_num=0 #初始化row_num变量。
for num in col_vals: #将工作表B列中的数据循环赋值给num变量。
    if type(num)==float: #判断num是否为float类型。
        if num>=90: #如果大于等于90。
            nws.write(row_num,2,'优') #则将'优'写入C列单元格。
        elif num>=80: #如果大于等于80。
            nws.write(row_num,2,'良') #则将'良'写入C列单元格。
        elif num>=60: #如果大于等于60。
            nws.write(row_num,2,'中') #则将'中'写入C列单元格。
        else: #如果上面的条件均不成立。
            nws.write(row_num,2,'差') #则将'差'写入C列单元格。
    row_num +=1 #对row_num累加1。
nwb.save('Chapter-3-17-1.xls') #保存工作簿。