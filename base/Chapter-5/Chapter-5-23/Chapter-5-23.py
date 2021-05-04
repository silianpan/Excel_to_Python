import xlrd#导入读取库xlrd。
from xlutils.copy import copy#导入工作簿复制函数。
wb=xlrd.open_workbook('Chapter-5-23-1.xls');ws=wb.sheet_by_name('工资表')#读取工作簿和工作表。
nwb=copy(wb);nws=nwb.get_sheet('工资表')#复制工作簿和读取副本工作簿中的工作表。
for row_num in range(1,ws.nrows):#循环可用行号。
    lst=[v for v in ws.row_values(row_num)[1:-1] if v!='']#获取每行工资数据列表。
    name=['工资总计','月份总数','平均工资','最高工资','最低工资']#统计名称
    units=['元','个','元','元','元']#统计单位
    total=[sum(lst),len(lst),sum(lst)/len(lst),max(lst),min(lst)]#统计结果
    lst1=['{}：{}{}'.format(x,int(y),z) for x,y,z in zip(name,total,units)]#用列表推导式将name、untis、total三个列表合并成一个列表。
    txt='\n'.join(lst1)#合并lst1列表为一个字符串。
    nws.write(row_num,13,txt)#将txt变量中值写入副本工作簿中的工作表。
nwb.save('Chapter-5-23-1.xls')#保存副本工作簿。
