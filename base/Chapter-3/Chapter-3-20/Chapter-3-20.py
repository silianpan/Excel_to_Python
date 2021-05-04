import xlrd #导入xlrd库。
from xlutils.copy import copy #导入copy函数。
wb=xlrd.open_workbook('Chapter-3-20-1.xls') #读取工作簿。
ws=wb.sheet_by_name('业绩表') #读取工作簿中的工作表。
nwb=copy(wb) #复制工作簿，形成副本。
nws=nwb.get_sheet('业绩表') #读取副本中的工作表。
for row_num in range(1,ws.nrows): #确定要循环的行号范围。
    num = 0 #初始化num变量。
    for col_num in range(1,13): #确定要循环的列号范围。
        num +=ws.cell_value(row_num,col_num) #使用num变量累加每个人的业绩。
        if num>=100: #如果num的值大于等于100。
            nws.write(row_num,13,ws.cell_value(0,col_num)) #则将月份写入N列。
            break #终止内层循环。
nwb.save('Chapter-3-20-1.xls') #保存工作簿。