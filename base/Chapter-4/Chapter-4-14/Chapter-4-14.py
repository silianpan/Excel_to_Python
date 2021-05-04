import xlrd,xlwt #导入读取和新建Excel的库。
wb=xlrd.open_workbook('Chapter-4-14-1.xls') #读取工作簿。
nwb=xlwt.Workbook('utf-8') #新建工作簿。
nws=nwb.add_sheet('统计结果') #新建工作表。
nws.write(0,0,'季度') #在新建的工作表中写入'季度'标题。
nws.write(0,1,'统计结果') #在新建的工作表中写入'统计结果'标题。
nums=0 #初始化nums为0。
lst=[] #初始化lst为空列表，便于存放汇总结果。
for ws in wb.sheets(): #循环读取ws工作簿下的每个工作表。
    for row_num in range(1,ws.nrows): #循环读取每个工作表中行号。
        name=ws.cell_value(row_num,0) #读取A列中的姓名。
        num=ws.cell_value(row_num,1) #读取B列中的业绩。
        for n in num.split('、'): #对B列单元格中的业绩进行拆分。
            nums +=int(n) #转换拆分的数字为整型，然后累加到nums变量。
        lst +=[name+':'+str(nums)] #将姓名与nums结果连接，然后累加到lst列表。
        nums=0 #重置nums变量，便于下次循环时使用。
    nws.write(int(ws.name[1]),0,ws.name) #将姓名写入新表A列。
    nws.write(int(ws.name[1]),1,'\n'.join(lst)) #将每个人的总业绩合并，再写入新表B列。
    lst=[] #重复lst为空列表，便于统计下一个工作表数据时使用。
nwb.save('Chapter-4-14-2.xls') #保存新建的工作簿。