import os,openpyxl #导入库。
nwb=openpyxl.Workbook();nwb.active.title='合并结果' #新建工作簿，并修改工作簿下的活动工作表名称。
nwb.active.append(['学区','学校名','班级','姓名','分数']) #给新建工作簿下的活动工作表写入表头。
for file in  os.listdir('某某比赛获奖表'): #获取指定文件夹下的文件名。
    wb=openpyxl.load_workbook('某某比赛获奖表\\'+file) #读取文件夹下的工作簿。
    for ws in wb.worksheets: #循环工作簿下的工作表。
        for row in list(ws.values)[1:]: #循环工作表中的每行数据。
            val=(file.split('.')[0],ws.title)+row #将工作簿名与工作表名组成元组，然后与row元组连接组合。
            nwb.active.append(val) #将组合后的每行数据重写入新工作簿下的新工作表中。
nwb.save('Chapter-11-23-1.xlsx') #保存新工作簿。
