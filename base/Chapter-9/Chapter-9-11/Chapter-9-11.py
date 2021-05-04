# 自定义replaces函数。
def replaces(string,new,*old):
    for o in old: #循环old参数中的元素赋值给o变量。
        string = string.replace(o,new) #将o变量中的值，替换为new变量中的值，最后再赋值给string参数。
    return string #循环替换完成后，将string中的值返回给replaces函数。
# 自定义函数应用
import xlrd #导入xls文件读取库。
from xlutils.copy import copy #导计工作簿复制函数。
wb=xlrd.open_workbook('Chapter-9-11-1.xls');ws=wb.sheet_by_name('书单表') #读取工作簿和工作表。
nwb=copy(wb);nws=nwb.get_sheet('书单表') #复制工作簿，以及读取副本工作簿下的工作表。
for row_num in range(1,ws.nrows): #循环'书单表'的行号，赋值给row_num。
    val1=ws.cell_value(row_num,1) #获取B列单元格的书名，并赋值给val变量。
    val2='《'+replaces(val1,'》《',' ','|')+'》' #将' '和'|'替换为'》、《'，再补齐两端书名号，赋值给val2变量。
    nws.write(row_num,2,val2) #将处理好后的val2变量写入C列单元格。
nwb.save('Chapter-9-11-1.xls') #保存副本工作簿。