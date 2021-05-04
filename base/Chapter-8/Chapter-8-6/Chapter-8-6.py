import xlrd #导入xls文件读取库。
from xlutils.copy import copy #导入函数
wb=xlrd.open_workbook('Chapter-8-6-1.xls');ws=wb.sheet_by_name('评级表') #读取工作簿和工作表。
nwb=copy(wb);nws=nwb.get_sheet('评级表') #复制工作簿及读取副本工作簿下的工作表。
row_num=0 #初始化row_num变量为0。
for row in tuple(ws.get_rows())[1:]: #循环读取每行记录。
   row_num += 1 #对row_num变量累加1。
   if {'优','良'}<={v.value for v in row[1:-1]}: #判断每行的等级是否包含'优'和'良'。
       nws.write(row_num,5,'√') #如果包含则写入'√'。
   else: #否则
       nws.write(row_num,5,'×') #如果不包含则写入'×'。
nwb.save('Chapter-8-6-1.xls') #保存副本工作簿。


