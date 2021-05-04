import xlrd #导入读取xls文件的库。
from xlutils.copy import copy #导入工作簿复制函数。
wb=xlrd.open_workbook('Chapter-4-9-1.xls') #读取工作簿。
ws=wb.sheet_by_name('信息表') #读取工作表。
nwb=copy(wb) #复制工作簿产生一个副本。
nws=nwb.get_sheet('信息表') #读取副本中的工作表。
row_num=0 #初始化row_num变量为0。
while True: #条件为True，表示会一直循环，在循环中做终止循环处理。
    row_num +=1 #对row_num变量累加1。
    if row_num > ws.nrows-1: #当row_num变量大于已使用单元格区域行数时。
        break #则终止循环。
    info=ws.cell_value(row_num, 0) #获取A列单元格的值。
    strat=info.find('（')+1 #搜索'（'的位置，应该从'（'之后，所以最后要加1。
    end=info.find('）') #搜索'）'的位置。
    dept=info[strat:end] #截取A列单元格'（'和'）'之间的部门信息。
    nws.write(row_num,1,dept) #将截取到的部门信息写入B列单元格。
nwb.save('Chapter-4-9-1.xls') #保存工作簿。