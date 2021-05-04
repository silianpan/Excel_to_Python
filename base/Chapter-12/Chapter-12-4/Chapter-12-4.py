import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-12-4-1.xlsx') #读取工作簿。
ws=wb['分数表'] #读取工作表。
dic={} #创建dic变量为空字典。
nws=wb.create_sheet('转换后');nws.append(['姓名','语文','数学','英语']) #新建工作表，并在新工作表中写入表头。
for row in list(ws.values)[1:]: #按行读取ws工作表除表头外的所有数据。
    if not row[0] in dic.keys(): #如果row[0]在dic字典中不存在。
        dic[row[0]]={'语文':'','数学':'','英语':''} #则在dic字典中创建新的键值对，row[0]为键，值为字典。
        dic[row[0]][row[1]]=row[2] #并且将分数写入字典中的字典。
    else: #否则。
        dic[row[0]][row[1]]=row[2] #不创建字典，只将分数写入字典中的字典。
for key,item in dic.items(): #获取dic字典中的键和值，并赋值给对应的key和item。
    nws.append([key]+list(item.values())) #将key中的值与item字典中的values，也就是分数。合并成新列表再写入新工作表。
wb.save('Chapter-12-4-2.xlsx') #另存工作簿。
