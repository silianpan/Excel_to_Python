# 自定义vlookup函数
def vlookup(val,lst,num=1):
    r=lst[0].index(val) #对lst列表第1个元素使用index函数进行查找。得到返回值赋值给r变量。
    v=lst[num][r] #再使用num和r变量确定截取位置。
    return v #将截取的值返回给函数
# 自定义函数应用
import xlrd #导入读取xls文件的库。
from xlutils.copy import copy#导入复制工作簿函数。
wb=xlrd.open_workbook('Chapter-9-6-1.xls')#读取工作簿。
ws_price=wb.sheet_by_name('单价表') #读取工作簿下的工作表。
ws_Sale=wb.sheet_by_name('销售表') #读取工作簿下的工作表。
nwb=copy(wb);nws=nwb.get_sheet('销售表') #复制工作簿，以及读取副本工作簿下的工作表。
lst=[ws_price.col_values(0)[1:],ws_price.col_values(1)[1:]] #读取'单价表'下的产品列和单价列。
for row_num in range(1,ws_Sale.nrows): #循环'销售表'中的行号。
    val1=ws_Sale.cell_value(row_num,0) #读取'销售表'A列的品名。
    val2=ws_Sale.cell_value(row_num,1) #读取'销售表'B列的数量。
    val3=vlookup(val1,lst)*val2 #将val1中的品名去lst列表查找，返回对应的单价，再乘以val2的数量，得到金额。
    nws.write(row_num,2,val3) #将计算出来的金额写入'销售表'的C列单元格。
nwb.save('Chapter-9-6-1.xls') #保存副本工作簿。