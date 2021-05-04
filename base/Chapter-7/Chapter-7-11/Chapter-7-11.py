import xlrd #导入xls文件的读取库。
from xlutils.copy import copy#导入复制函数。
wb=xlrd.open_workbook('Chapter-7-11-1.xls')#读取工作簿。
ws1=wb.sheet_by_name('全部名单')#读取'全部名单'工作表。
ws2=wb.sheet_by_name('已完成名单')#读取'已完成名单'工作表。
nwb=copy(wb);ws3=nwb.get_sheet('未完成名单')#读取'已完成名单'工作表，具有写入功能。
lst1=[tuple(v.value for v in l) for l in ws1.get_rows()]#获取'全部名单'记录。
lst2=[tuple(v.value for v in l) for l in ws2.get_rows()][1:]#获取'已完成名单'记录。
dic=dict.fromkeys(lst1)#将lst1转换为dic字典。
[dic.pop(t) for t in lst2]#从dic字典删除lst2中的已完成名单。
row_num=0#初始化row_num变量为0。
for key in dic.keys():#将dic字典中的键循环出来。
    ws3.write(row_num,0,key[0])#将姓名写入A列。
    ws3.write(row_num,1,key[1])#将部分写入B列
    row_num +=1#row_num变量累加1。
nwb.save('Chapter-7-11-1.xls')#保存工作簿副本。