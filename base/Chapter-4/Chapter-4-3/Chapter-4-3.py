import xlrd,xlwt #导入所需库。
wb=xlrd.open_workbook('Chapter-4-3-1.xls') #读取工作簿。
ws=wb.sheet_by_name('员工信息表') #读取工作表。
nwb=xlwt.Workbook('utf-8') #新建工作簿。
nws=nwb.add_sheet('员工信息表-1') #新建工作表。
nws.write(0,0,'姓名') #在表头写入'姓名'。
nws.write(0,1,'身份证号') #在表头写入'身份证号'。
nws.write(0,2,'性别') #在表头写入'性别'。
row_num=0 #初始化row_num变量为0。
while row_num<ws.nrows-1: #当row_num小于'员工信息表'已用行数时，开始循环。
    row_num +=1 #累加row_num变量。
    card=ws.cell_value(row_num,1) #获取单元格的身份证号信息。
    sex_num=int(card[14:17][-1]) #截取判断性别的数字。
    sex='男' if sex_num % 2 == 1 else '女' #根据数字判断性别。
    name=ws.cell_value(row_num,0) #获取姓名。
    nws.write(row_num,0,name) #将姓名写入新工作表中的A列单元格。
    nws.write(row_num,1,card) #将身份证号写入新工作表中的B列单元格。
    nws.write(row_num,2,sex) #将性别写入新工作表中的C列单元格。
nwb.save('Chapter-4-3-2.xls') #保存新建的工作簿。