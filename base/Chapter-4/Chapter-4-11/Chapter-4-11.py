import xlrd#导入读取xls文件的库。
from xlutils.copy import copy#导入工作簿复制函数。
wb=xlrd.open_workbook('Chapter-4-11.xls')#读取工作簿。
ws=wb.sheet_by_name('员工表')#读取工作表。
nwb=copy(wb)#复制工作簿产生一个副本。
nws=nwb.get_sheet('员工表')#读取副本中的工作表。
row_num=0#初始化row_num变量为0。
while row_num<ws.nrows-1:#当row_num变量小于已使用单元格区域行数时。
    row_num +=1#则对row_num变量累加1。
    roster=ws.cell_value(row_num, 1)#获取B列单元格的值。
    for symbol in '、\|':#循环要被替换的符号。
        roster=roster.replace(symbol,'-')#将指定字符替换为'-'。
    nws.write(row_num,2,roster)#将替换结果写入C列单元格。
nwb.save('Chapter-4-11.xls')#保存副本工作簿。