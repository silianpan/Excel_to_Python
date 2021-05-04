import xlwt #导入xlwt
nwb=xlwt.Workbook('utf-8') #新建工作簿
nws=nwb.add_sheet('工资表') #在新建工作簿中创建工作表
nws.write(0,0,'张三：9000元') #在工作表的指定单元格写入值
nwb.save('工资表.xls') #保存工作簿
