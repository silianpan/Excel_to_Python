import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-12-10-1.xlsx') #读取工作簿。
ws1=wb['招生表'];ws2=wb['计划表'] #读取'招生表'和'计划表'。
dic=dict.fromkeys([v.value for v in ws2['A'][1:]],0)#创建字典，用招生员批量创建键。
for row in list(ws1.values)[1:]: #读取ws1工作表中所有的数据，并逐行赋值给row变量。
    dic[row[3]] +=1 #对row[3]键对应的值累加1。
for row in ws2.iter_rows(min_row=2): #获取'计划表'表的数据，从第二行开始按行获取。
    lst=[cell.value for cell in row] #使用列表推导获取row变量中的值。
    if dic[lst[0]]>=lst[1]: #判断每个招生员的招生数量如果大于等于计划数量。
        row[2].value='已达标（{}人）'.format(dic[lst[0]]) #则在对应的单元格写入'已达标'。
    else:#否则。
        row[2].value='未达标（{}人）'.format(dic[lst[0]]) #则在对应的单元格写入'未达标'。
wb.save('Chapter-12-10-1.xlsx') #保存工作簿。
