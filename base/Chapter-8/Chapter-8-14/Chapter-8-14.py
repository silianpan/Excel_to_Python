import xlrd#导入xls文件读取库。
from xlutils.copy import copy#导入复制工作簿函数。
wb=xlrd.open_workbook('Chapter-8-14-1.xls');ws=wb.sheet_by_name('优秀员工名单表')#读取工作簿与工作表。
nwb=copy(wb);nws=nwb.get_sheet('全年优秀表')#复制工作簿，并且读取副本工作簿下的工作表。
set1=set(ws.col_values(1)[1:])#将B列的姓名转换为集合，并赋值给set1变量。
for col_num in (1,2,3,4):#循环序列值1~4，做为'优秀员工名单表'工作表列号。
    set1.intersection_update(ws.col_values(col_num)[1:])#将set1集合与'优秀员工名单表'工作表中B列到E列的数据做累计交集。
    # set1=set1.intersection(ws.col_values(col_num)[1:])
    # set1=set1&set(ws.col_values(col_num)[1:])
    # set1 &=set(ws.col_values(col_num)[1:])
row_num=0#初始化row_num变量为0。
for name in set1:#循环set1集合的内容。
    row_num += 1#累加row_num变量。
    nws.write(row_num,0,row_num)#将序号写入'全年优秀表'工作表A列单元格。
    nws.write(row_num,1,name)#将姓名写入'全年优秀表'工作表B列单元格。
nwb.save('Chapter-8-14-1.xls')#保存副本工作簿。
