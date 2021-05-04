import xlrd#导入读取xls文件的库。
from xlutils.copy import copy#导入复制工作簿函数。
wb=xlrd.open_workbook('Chapter-10-5-1.xls');ws=wb.sheet_by_name('分数表')#读取工作簿，以及工作簿下的工作表。
nwb=copy(wb);nws=nwb.get_sheet('转换表')#复制工作簿，以及读取副本工作簿下的工作表。
l=[[[n.value]*3,['语文','数学','英语'],[x.value,y.value,z.value]] for n,x,y,z in ws.get_rows()]#获取工作表各行数据，并格式化。

row_num=0;nws.write(0,0,'转换合并')#初始化row_num变量为0，给'转换合并'工作表写入表头。
for x,y,z in l[1:]:#循环l变量中的数据。
    for k in map(lambda a,b,c:'{}({}{:.0f})'.format(a,b,c),x,y,z):#转换l中的数据，并格式化。
        print(k)
        row_num +=1#将row_num变量累加1，做为写入时的行号。
        nws.write(row_num,0,k)#将格式化后的数据入写入'转换合并'工作表A列单元格。
nwb.save('Chapter-10-5-1.xls')#保存副本工作簿。
