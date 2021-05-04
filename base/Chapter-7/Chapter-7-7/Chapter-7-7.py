import xlrd,xlwt #导入xls文件的读取与写入库。
wb=xlrd.open_workbook('Chapter-7-7-1.xls');ws=wb.sheet_by_name('分数表')#读取工作簿和工作表。
nwb=xlwt.Workbook('utf-8');nws=nwb.add_sheet('汇总表')#新建工作簿和工作表。
nws.write(0,0,'姓名');nws.write(0,1,'总分');nws.write(0,2,'平均分')#给新建工作表写入表头数据。
dic,row_num={},0#初始化dic变量为空字典，num变量为0。
for name,score in ws.get_rows():#读取'分数表'工作表已使用的所有行。
    if not name.value in dic:#如果指定的键在字典中不存在。
        dic[name.value] = [score.value] #则将姓名做为键，分数做为值，新建一个键值对。
    else:#否则
        dic[name.value].append(score.value) #则将分数添加到键对应的值中。
for key,item in tuple(dic.items())[1:]:#循环字典中的键值。
    row_num +=1 #累加row_num变量。
    nws.write(row_num,0,key)#将姓名写入新工作表A列。
    nws.write(row_num,1,sum(item))#将总分写入新工作表B列。
    nws.write(row_num,2,sum(item)/len(item))#将平均分写入新工作表C列。
nwb.save('Chapter-7-7-2.xls')#保存新建的工作簿。
