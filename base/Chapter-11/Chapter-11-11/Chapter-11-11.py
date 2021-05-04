import openpyxl #导入库。
nwb=openpyxl.Workbook() #新建工作簿。
for name in ['张三','李四','王二','麻子']: #循环列表中的姓名。
    nwb.create_sheet(name) #新建工作表时用name变量中的值做为名称。
nwb.remove(nwb['Sheet']) #删除新建工作簿时默认新建的工作表。
nwb.save('Chapter-11-11-1.xlsx') #保存工作簿。
