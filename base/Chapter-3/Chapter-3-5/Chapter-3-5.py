import xlwt #导入xlwt库
nwb=xlwt.Workbook('utf-8') #新建工作簿
nws=nwb.add_sheet('乘法表') #新建工作表
for x in range(1,10): #循环数字1到9
    for y in range(1,x+1): #循环数字1到x+1
        txt='{0}×{1}={2}'.format(y,x,x*y) #格式化乘法公式
        nws.write(x,y,txt) #将乘法公式写入单元格
nwb.save('Chapter-3-5-1.xlsx') #保存工作簿
