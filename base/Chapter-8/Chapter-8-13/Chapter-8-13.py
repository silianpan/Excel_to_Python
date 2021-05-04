import xlrd,xlwt#导入xls文件的读取与写入库。
nwb=xlwt.Workbook('utf-8');nws=nwb.add_sheet('统计结果')#新建工作簿与工作表。
set1=set();row_num=0#初始化set1变量为空集合，row_num变量为0。
nws.write(0,0,'公司名');nws.write(0,1,'名单')#在新建的工作表中写入表头。
for ws in xlrd.open_workbook('Chapter-8-13-1.xls').sheets():#循环读取'Chapter-8-13-1.xls'工作簿下所有工作表。
    for col_num in (1,2,3):#循环1、2、3序列做为读取工作表的列号。
        set1= set1.union(set(ws.col_values(col_num)[1:]))#将每列数据转换成集合，再合并。
        # set1 =set1|set(ws.col_values(col_num)[1:])
        # set1 |=set(ws.col_values(col_num)[1:])
        # set1.update(set(ws.col_values(col_num)[1:]))
    row_num +=1#累加row_num变量。
    nws.write(row_num,0,ws.name)#在新工作表A列写入公司名。
    nws.write(row_num,1,'、'.join(set1))#在新工作表B列写入合并集合后的字符串。
    set1 = set()#重置set1变量为空集合。
nwb.save('Chapter-8-13-2.xls')#保存新建的工作簿。
