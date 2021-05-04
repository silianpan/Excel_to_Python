import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-12-5-1.xlsx')#读取工作簿。
ws1=wb['业绩表'];ws2=wb['提成表']#读取工作表
lst=list(ws2.values)[1:]#获取提成表的数据。
def query(num,iterable):# 自定义query函数，用于查询提成点数和计算提成金额。
    for level in iterable: #循环获取每个提成等级的起始、终止金额和提成百分点。
        if num>=level[0] and num<level[1]:#如果num的值大于等于起始金额，并且小于终止金额。
           return num*level[2]#那么将num的值乘以提成百分点，将得到的提成金额做为函数返回值。
           break #跳出循环。
for v in [cell for cell in ws1['B']][1:]:#将'业绩表'工作表B列单元格循环赋值给v变量。
    v.offset(0,1).value=query(v.value,lst)#使用query函数计算每个业绩的提成金额，并写入单元格。
wb.save('Chapter-12-5-2.xlsx')#保存工作簿。
