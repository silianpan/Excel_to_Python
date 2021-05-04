import xlrd #导入xls文件读取库。
from xlutils.copy import copy #导入工作簿复制函数
wb=xlrd.open_workbook('Chapter-5-4-1.xls') #读取工作簿。
ws=wb.sheet_by_name('分数表') #读取工作表。
nwb=copy(wb) #复制工作簿为副本。
nws=nwb.get_sheet('分数表') #读取副本工作簿中的工作表。
for row_num in range(1,ws.nrows): #循环行号。
    row_vals=ws.row_values(row_num) #根据行号读取每行的值。
    avg_score=sum(row_vals[1:-1])/12 #对每行的分数求平均值。
    fmt_score=round(avg_score,2) #将平均值四舍五入到小数点后两位。
    nws.write(row_num,13,fmt_score) #将平均值写入13列中的单元格。
nwb.save('Chapter-5-4-1.xls') #保存副本工作簿。