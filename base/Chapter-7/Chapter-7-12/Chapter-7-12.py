import os,xlrd,xlwt #导入操作系统接口模块，xls读取与写入库。
nwb=xlwt.Workbook('utf-8');nws=nwb.add_sheet('合并结果') #新建工作簿和工作表。
files=os.listdir('销售表') #获取销售表文件夹下的所有工作簿名称。
row_num=0;[nws.write(row_num,n,v) for n,v in ((0,'店名'),(1,'品牌'),(2,'型号'),(3,'数量'))] #在新工作表写入表头。
for file in files: #循环工作簿名称。
    wb=xlrd.open_workbook('销售表/'+file) #根据工作簿名称读取工作簿对象。
    for ws in wb.sheets(): #循环工作簿下所有工作表。
        for t,n in tuple(ws.get_rows())[1:]: #循环工作表下所有行记录（除开表头）。
            tup=(file.split('.')[0],ws.name,t.value,n.value) #准备好要写入新工作表的数据。
            row_num +=1 #累加row_num变量。
            for num in range(0,4): #循环数字0~3，做为写入数据时的列号。
                nws.write(row_num,num,tup[num]) #循环将数据写入新工作表。
nwb.save('Chapter-7-12-1.xls') #保存新建的工作簿。



