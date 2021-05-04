import xlrd #导入xlrd
wb=xlrd.open_workbook(r'Chapter-2-3-1.xlsx') #读取工作簿对象。
all_ws1=wb.sheets() #读取工作簿下的所有工作表对象
all_ws2=wb.sheet_names() #读取工作簿下的所有工作表对象的名称
ws1=wb.sheet_by_index(0) #用索引值读取工作表-方法1
ws2=wb.sheets()[1] #用索引值读取工作表-方法2
ws3=wb.sheet_by_name('雪豹队') #用索引值读取工作表-方法3
ws4=xlrd.open_workbook(r'Chapter-2-3-1.xlsx').sheet_by_name('飞龙队')#直接通过工作簿读取工作表对象
