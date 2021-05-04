import xlrd,xlwt #导入xls文件的读取与写入库。
wb=xlrd.open_workbook('Chapter-7-10-1.xls');ws=wb.sheet_by_name('分数表')#读取工作簿和工作表。
nwb=xlwt.Workbook('utf-8');nws=nwb.add_sheet('提取结果')#新建工作簿和工作表。
lst=[tuple(v.value for v in l[0:3]) for l in ws.get_rows()]#获取每行值，并转换为元组。
row_num=0#初始化row_num变量为0。
for key in dict.fromkeys(lst).keys():#使用fromkeys函数取得lst列表的唯一值。
    nws.write(row_num,0,key[0])#将学校名称写入A列。
    nws.write(row_num,1,key[1])#将年级名称写入B列。
    nws.write(row_num,2,key[2])#将班级名称写入C列。
    row_num +=1#累加row_num变量。
nwb.save('Chapter-7-10-2.xls')#保存新建的工作簿。