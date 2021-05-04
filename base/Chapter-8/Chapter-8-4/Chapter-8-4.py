import xlrd,xlwt #导入xls文件的读取与写入库。
ws=xlrd.open_workbook('Chapter-8-4-1.xls').sheet_by_name('采购表') #读取工作簿与工作表。
nwb=xlwt.Workbook('utf-8');nws=nwb.add_sheet('提取结果') #新建工作簿和工作表。
row_num=0;nws.write(0,0,'序号');nws.write(0,1,'名称') #在新工作表写入表头。
set1=set() #初始化set1变量为空集合。
for col_num  in range(1,ws.ncols,3): #循环工作表的所有品名列号。
    col=ws.col_values(col_num)[1:] #获取品名列的所有值。
    set1.update(col) #将品名列的值添加到set1集合。
for name in set1: #循环出set1集合中的所有元素。
    row_num +=1 #累加row_num变量。
    nws.write(row_num,0,row_num) #写入序号。
    nws.write(row_num,1,name) #写入品名。
nwb.save('Chapter-8-4-2.xls') #保存新建的工作簿。