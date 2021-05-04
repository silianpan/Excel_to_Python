import xlrd #导入读取xls文件的库。
from xlutils.copy import copy #导入工作簿复制函数。
wb=xlrd.open_workbook('Chapter-9-14-1.xls');ws=wb.sheet_by_name('身份证表') #读取工作簿和工作表。
nwb=copy(wb);nws=nwb.get_sheet('身份证表') #复制工作簿，并且读取副本工作簿中的工作表。
for row_num in range(1,ws.nrows):#循环'身份证表'工作表的行号。
    card=lambda id:'男' if int(id[-2])%2==1 else '女'#自定义根据身份证号判断性别的匿名函数。
    val=ws.cell_value(row_num, 0)#获取A列的身份证号，并赋值给val变量。
    nws.write(row_num,1,card(val))#将val做为匿名函数card的参数，将判断出的性别写入B列单元格。
nwb.save('Chapter-9-14-1.xls')#保存副本工作簿。