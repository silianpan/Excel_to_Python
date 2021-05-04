import xlrd,xlwt #导入xls文件的读取与写入库。
nwb=xlwt.Workbook('utf-8');nws=nwb.add_sheet('统计结果') #新建工作簿和工作表。
row_num=0;nws.write(0,0,'年份');nws.write(0,1,'名单') #将表头写入新工作表。
for ws in xlrd.open_workbook('Chapter-8-8-1.xls').sheets(): #循环工作簿下的所有工作表。
    set1=set(ws.col_values(1)[1:]) #获取工作表的B列的名单，并转换为集合。
    row_num +=1 #累加row_num变量。
    nws.write(row_num,0,ws.name) #将工作表名写入新工作表A列单元格。
    nws.write(row_num,1,'、'.join(set1)) #将集合中的名单合并写入新工作表B列单元格。
nwb.save('Chapter-8-8-2.xls') #保存新建的工作簿。