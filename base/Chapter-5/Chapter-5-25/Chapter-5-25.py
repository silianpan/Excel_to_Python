import xlrd #导入读取库xlrd。
from xlutils.copy import copy #导入工作簿复制函数。
wb=xlrd.open_workbook('Chapter-5-25-1.xls');ws=wb.sheet_by_name('成绩表') #读取工作簿和工作表。
nwb=copy(wb);nws=nwb.get_sheet('成绩表') #复制工作簿和读取副本工作簿中的工作表。
for row_num in range(1,ws.nrows): #循环可用行号。
    lst=ws.row_values(row_num)[1:-1] #获取每行工资数据列表。
    level=['优','良','中','差'] #列出要判断的等级。
    l=[v+':'+str(lst.count(v)) for v in level] #用列表推导式统计每个等级的个数。
    nws.write(row_num,7,'\n'.join(l)) #将统计结果写入副本工作表的H列。
nwb.save('Chapter-5-25-1.xls') #保存副本工作簿。