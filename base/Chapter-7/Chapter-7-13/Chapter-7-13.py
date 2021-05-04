import xlrd,xlwt #导入xls文件的读取与写入库。
ws=xlrd.open_workbook('Chapter-7-13-1.xls').sheet_by_name('业绩表') #读取'业绩表'工作表。
dic={} #初始化dic变量为空字典。
for row_num in range(1,ws.nrows): #获取'业绩表'工作表已使用行号并循环。
    lst=ws.row_values(row_num) #获取每行的值，以列表形式赋值给lst变量。
    key=(lst[0],lst[1]) #将lst列表中的省份、客户名称组成元组。
    if not key in dic: #如果key在dic字典中不存在。
        dic[key]=[lst[4]] #则以key为键，金额为值写入列表。
    else: #否则。
        dic[key].append(lst[4]) #将金额添加到key键对应值列表中。
for province in dict.fromkeys(tuple(zip(*dic.keys()))[0]): #获取省份进行循环。
    nwb=xlwt.Workbook('utf-8');nws=nwb.add_sheet(province) #新建工作簿、工作表。
    num=0;nws.write(num,0,'客户名');nws.write(num,1,'交易次数');nws.write(num,2,'总金额') #在新工作表写入表头。
    for v in [(k[1],i) for k,i in dic.items() if k[0]==province]: #循环属于当前省份的键值。
        num +=1 #累加num变量做为写入数据时的行号。
        nws.write(num,0,v[0]) #在新工作表A列写入公司名称。
        nws.write(num,1,len(v[1])) #在新工作表B列写入交易次数。
        nws.write(num,2,sum(v[1])) #在新工作表C列写入总金额。
    nwb.save('统计结果/'+province+'.xls') #以省份名为工作簿名称保存工作簿。

