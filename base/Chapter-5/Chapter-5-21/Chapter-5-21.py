import xlrd,xlwt #导入xls文件的读取库与写入库。
wb=xlrd.open_workbook('Chapter-5-21-1.xls');ws=wb.sheet_by_name('员工表') #读取工作簿与工作表。
nwb=xlwt.Workbook('uft-8');nws=nwb.add_sheet('整理结果') #新建工作簿与工作表。
nws.write(0,0,'公司名');nws.write(0,1,'名单') #将表头写入新工作表第1行。
for row_num in range(1,ws.nrows): #循环行号。
    val1=ws.cell_value(row_num,0) #读取'员工表'A列数据。
    val=ws.cell_value(row_num,1) #读取'员工表'B列数据。
    lst1=val.split('、') #对B列数据按'、'拆分。
    zip_iter=zip(range(1,len(lst1)+1),lst1) #将序号列表与名单列表组合。
    lst2=[str(num)+''+name for num,name in zip_iter] #将序号与姓名合并，构成列表。
    val2='、'.join(lst2) #将构成的lst2列表用'、'合并。
    nws.write(row_num,0,val1) #将公司名写入新工作表A列。
    nws.write(row_num,1,val2) #将val2的值写入新工作表B列。
nwb.save('Chapter-5-21-2.xls') #保存新工作簿。
