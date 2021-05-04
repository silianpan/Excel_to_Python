import xlrd #导入xls文件读取库。
from xlutils.copy import copy #导入工作簿复制函数。
wb=xlrd.open_workbook('Chapter-5-8-1.xls') #读取工作表。
ws=wb.sheet_by_name('分数表') #读取工作表
nwb=copy(wb);nws=nwb.get_sheet('分数表') #复制工作簿及读取副本的工作表。
lst=[] #初始化lst变量为空列表。
for row_num in range(1,ws.nrows): #循环读取每行数据。
    row_vals=ws.row_values(row_num)[1:-1] #通过切片获取每行的数字区域。
    for val in row_vals: #循环row_vals列表中的每个数字赋值给val变量。
        if val>=80: #如果val变量中的数字大于等于80.
            lst.append(val) #则将数字添加到lst列表。
            lst +=[val] #则将数字累积到lst列表。
    nws.write(row_num,13,sum(lst)) #将lst列表求和，并写入副本工作表的单元格。
    lst=[] #重置lst变量为空列表。
nwb.save('Chapter-5-8-1.xls') #保存工作簿。