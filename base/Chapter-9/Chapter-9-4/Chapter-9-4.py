# 自定义函数
def intercept(s,num,delimiter):
    s1=str(s) #将要分段的对象转换为字符串类型。
    lst=[s1[n:n+num] for n in range(0,len(s1),num)] #对数据进行分段处理。
    s2=delimiter.join(lst) #合并分段的列表。
    return s2 #将合并结果返回函数。
# 自定义函数应用
import xlrd #导入xls文件读取库。
from xlutils.copy import copy #导计工作簿复制函数。
wb=xlrd.open_workbook('Chapter-9-4-1.xls');ws=wb.sheet_by_name('卡号表') #读取工作簿和工作表。
nwb=copy(wb);nws=nwb.get_sheet('卡号表') #复制工作簿，以及读取副本工作簿下的工作表。
for row_num in range(1,ws.nrows): #循环行号。
    val=ws.cell_value(row_num,1)#读取B列单元格值。
    nws.write(row_num,2,intercept(val,4,'-'))#截取指定长度的字符进行分段，再写入单元格。
nwb.save('Chapter-9-4-1.xls') #保存副本工作簿。
