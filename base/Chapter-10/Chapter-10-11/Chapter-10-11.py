import xlrd #导入读取xls文件的库。
from xlutils.copy import copy #导入复制工作簿函数。
wb=xlrd.open_workbook('Chapter-10-11-1.xls');ws=wb.sheet_by_name('销量表') #读取工作簿，以及工作簿下的工作表。
nwb=copy(wb);nws=nwb.get_sheet('销量表') #复制工作簿，以及读取副本工作簿下的工作表。
for row_num in range(1,ws.nrows): #获取工作表行号循环。
    lst=ws.cell_value(row_num,1).split('、') #以顿号拆分B列单元格的值为列表。
    lst.sort(key=lambda x:int(x.split('：')[1]),reverse=True) #以数量为排序依据，进行降序排列。
    val='、'.join(lst) #将排序后的列表再以顿号合并成字符串。
    nws.write(row_num,2,val) #当val变量的值写入C列单元格。
nwb.save('Chapter-10-11-1.xls') #保存副本工作簿。
