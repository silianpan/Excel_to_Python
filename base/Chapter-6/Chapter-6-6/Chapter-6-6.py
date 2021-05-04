import xlrd,xlwt#导入xls文件的读取库与写入库。
wb=xlrd.open_workbook('Chapter-6-6-1.xls');ws=wb.sheet_by_name('名单表')#读取工作簿和工作表。
nwb=xlwt.Workbook('utf-8');nws=nwb.add_sheet('整理结果')#新建工作簿和工作表。
col_count=int(input("输确认每行存放姓名个数："))#用户确认转换成多少列。
row_count=ws.nrows//col_count if ws.nrows%col_count==0 else ws.nrows//col_count+1#获取行数。
col_num=tuple(range(0,col_count))*row_count#生成列号元组。
row_num=(v2 for v1 in ((r,)*col_count for r in range(0,row_count)) for v2 in v1)#生成行号元组。
col_val=ws.col_values(0)#获取要转换的列数据。
num=tuple(range(1,ws.nrows+1))#获取序号。
for r,c,n,v in zip(row_num,col_num,num,col_val):#将行号、列号、序号、名单使用zip转换组合，再循环出来。
    nws.write(r,c,'{:02}、{}'.format(n,v))#将r,c做为写入单元格的行、列号，对n、v中的序号和姓名格式化后写入单元格。
nwb.save('Chapter-6-6-2.xls')#保存新建的工作簿。