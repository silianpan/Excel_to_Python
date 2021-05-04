import xlwt,xlrd#导入xls文件的写入和读取库。
wb=xlrd.open_workbook('Chapter-7-6-1.xls');ws=wb.sheet_by_name('分数表')#读取工作簿与工作表。
nwb=xlwt.Workbook('utf-8');nws=nwb.add_sheet('汇总表')#新建工作簿与工作表。
dic,row_num=dict(),0#将dic变量初始化为空字典，row_num变量初始化为0。
for cls,name in ws.get_rows():#循环指定工作表的所有行。
    dic[cls.value] =name.value#新建或修改字典。
for key,item in dic.items():#循环字典中的键值对。
    nws.write(row_num,0,key)#将字典中的键写入A列。
    nws.write(row_num,1,item)#将字典中的值写入B列。
    row_num +=1#累加row_num变量。
nwb.save('Chapter-7-6-2.xls')#保存新建的工作簿。