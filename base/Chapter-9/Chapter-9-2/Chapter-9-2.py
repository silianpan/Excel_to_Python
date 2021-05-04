# 自定义平均函数
def average(lst):
    num=sum(lst)/len(lst) #平均处理。
    avg=float('{:.2f}'.format(num)) #格式化平均值。
    return avg #返回平均值。
# 数据平均处理
import xlrd #导入xls文件读取库。
from xlutils.copy import copy #导计工作簿复制函数。
wb=xlrd.open_workbook('Chapter-9-2-1.xls');ws=wb.sheet_by_name('工资表') #读取工作簿和工作表。
nwb=copy(wb);nws=nwb.get_sheet('工资表') #复制工作簿，以及读取副本工作簿下的工作表。
for row_num in range(1,ws.nrows): #循环行号。
    salary_list=ws.row_values(row_num)[1:-1] #获取1到12月份的工资列表。
    nws.write(row_num,13,average(salary_list)) #调用平均函数average对salary_list列表求平均。
nwb.save('Chapter-9-2-1.xls') #保存副本工作簿。
