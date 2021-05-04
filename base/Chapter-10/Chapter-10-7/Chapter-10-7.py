import xlrd #导入读取xls文件的库。
from xlutils.copy import copy #导入复制工作簿函数。
wb=xlrd.open_workbook('Chapter-10-7-1.xls');ws=wb.sheet_by_name('分数表') #读取工作簿，以及工作簿下的工作表。
nwb=copy(wb);nws=nwb.get_sheet('分数表') #复制工作簿，以及读取副本工作簿下的工作表。
lst=ws.col_values(1)[1:] #获取B列的分数。
for num in range(1,ws.nrows): #获取行号循环。
    en_rank=1+len(list(filter(lambda x:lst[num-1]<x,lst))) #计算美式排名。
    cn_rank=1+len(list(filter(lambda x:lst[num-1]<x,set(lst)))) #计算中式排名。
    nws.write(num,2,en_rank) #将美式排名写入C列。
    nws.write(num,3,cn_rank) #将美式排名写入D列。
nwb.save('Chapter-10-7-1.xls') #保存副本工作簿。

