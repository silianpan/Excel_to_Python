import xlwt,xlrd #导入读取与写入xls文件的库。
wb=xlrd.open_workbook('Chapter-5-15-1.xls') #读取工作簿。
nwb=xlwt.Workbook('uft-8');nws=nwb.add_sheet('汇总表') #新建工作簿与工作表。
lst=[[ws.name,sum(ws.col_values(1)[1:])] for ws in wb.sheets()] #求和工作表中B列的金额。
row_num=0 #初始化row_num变量为0。
for rows in [['月份','总营业额']]+lst: #将表头连接到lst列表前面，并开始循环。
    nws.write(row_num,0,rows[0]) #将月份写入A列。
    nws.write(row_num,1,rows[1]) #将每个月的总营业额写入B列。
    row_num +=1 #累加row_num变量，并做为写入数据时的行号。
nwb.save('Chapter-5-15-2.xls') #保存工作簿。