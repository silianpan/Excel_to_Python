import openpyxl #导入库。
wb=openpyxl.Workbook();ws=wb.active #新建工作簿及读取工作簿下的工作表。
for x in range(1,10): #循环数字1~9，并赋值给x变量。
    for y in range(1,x+1): #循环数字1~x，并赋值给y变量。
        val='{}×{}={}'.format(y,x,y*x) #将x、y变量的值做为乘法的因数，x*y的值做为乘积，格式化为乘法公式，并赋值给val变量。
        ws.cell(x,y,val) #将val变量中的乘法公式写入对应的单元格。
wb.save('Chapter-11-20-1.xlsx') #保存工作簿。
