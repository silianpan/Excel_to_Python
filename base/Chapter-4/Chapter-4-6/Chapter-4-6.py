import xlrd #导入读取xls文件的库。
from xlutils.copy import copy #导入复制工作簿的函数。
wb=xlrd.open_workbook('Chapter-4-6-1.xls') #读取工作簿。
ws=wb.sheet_by_name('分数表') #读取工作表。
nwb=copy(wb) #复制工作簿产生一个副本。
nws=nwb.get_sheet('分数表') #读取副本工作簿中的工作表。
row_num=0 #初始化row_num变量为0。
txt='' #初始化txt变量为空。
while row_num<ws.nrows-1: #当row_num变量小于已使用单元格区域行数时。
    row_num +=1 #则对row_num变量累加1。
    score=ws.cell_value(row_num,1) #获取B列单元格的值。
    for level in '优良中差': #循环'优良中差'4个等级。
        lev_sco='{}:{}\t'.format(level,score.count(level)) #统计每个级别的个数，并进行格式化。
        txt +=lev_sco #累积连接各等级数量。
    nws.write(row_num,2,txt) #将统计结果写入C列单元格。
    txt='' #重新初始化txt变量，便于存储下个单元格各等级的统计结果。
nws.write(0,2,'等级统计') #在C列写入表头。
nwb.save('Chapter-4-6-1.xls') #保存副本工作簿。