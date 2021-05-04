import xlrd#导入xls文件读取库。
from xlutils.copy import copy#导入复制工作簿函数。
wb=xlrd.open_workbook('Chapter-8-15-1.xls');ws=wb.sheet_by_name('达标表')#读取工作簿与工作表。
nwb=copy(wb);nws=nwb.get_sheet('未达标表')#复制工作簿，并且读取副本工作簿下的工作表。
dic={}#初始化dic变量为空字典。
for name,month in ws.get_rows():#循环获取'达标表'工作表的每行数据。
    if not name.value in dic:#如果name.value在字典中不存在。
        dic[name.value]=[month.value]#在新建键值。
    else:#否则。
        dic[name.value].append(month.value)#如果存在，则向键对应的值的列表添加month.value元素。
month_set=set(['{:02}月'.format(m) for m in range(1,13)])#创建01~12月的集合。
row_num=0#初始化row_num为0，做为写入数据时的行号。
for key,item in dic.items():#循环读取dic字典中的键和值。
    lst=list(month_set.difference(item));lst.sort()#将完整的月份集合与键对应的值做差集运算。将差集结果转换为列表，再做排序。
    # lst=list(month_set-set(item));lst.sort()
    nws.write(row_num,0,key)#将姓名写入'未达标表'工作表的A列单元格。
    nws.write(row_num,1,'、'.join(lst))#将未达标的月份合并，再写入'未达标表'工作表的B列单元格。
    row_num +=1#累加row_num变量。
nws.write(0,1,'未达标月份')#将字符串'未达标月份'写入'未达标表'工作表的B1单元格。
nwb.save('Chapter-8-15-1.xls')#保存副本工作簿。