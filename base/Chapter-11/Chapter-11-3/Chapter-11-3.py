from openpyxl import Workbook#导入openpyxl库中的Workbook类。
for num in range(1,13):#循环1~12给变量num。
    nwb=Workbook()#新建工作簿。
    wbname='{:02}.xlsx'.format(num)#格式化工作簿名称，再赋值给wbname变量。
    nwb.save(wbname)#保存工作簿。


