import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-22-1.xlsx') #读取工作簿。
nwb=openpyxl.Workbook() #新建工作簿。
nwb.active.append(['月份','姓名','手机','笔记本','电脑']) #给工作表写入表头。
for ws in wb.worksheets: #循环工作簿下的所有工作表。
    for row in list(ws.values)[1:]: #循环工作表下的每行数据。
        nwb.active.append((ws.title,)+row) #将工作表名连接上每行数据，再写入。
nwb.active.title='合并结果' #重命名新工作簿下的活动工作表名。
nwb.save('Chapter-11-22-2.xlsx') #保存新建的工作簿。

