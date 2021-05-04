import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-12-1-1.xlsx') #读取工作簿。
ws=wb.worksheets[0] #读取工作表。
lst1=list(ws.values)[1:] #获取工作表除表头外，所有的数据。
print(lst1)
lst2=sorted(lst1,key=lambda x:['经理','主管','职员'].index(x[3])) #按自定义的职务排序。
ws.delete_rows(2,ws.max_row) #删除工作表中除表头外的所有行数据。
for row in lst2: #循环将lst列表中的元素赋值给row变量。
    ws.append(row) #将row的值写入ws工作表。
wb.save('Chapter-12-1-1.xlsx') #保存工作簿。
