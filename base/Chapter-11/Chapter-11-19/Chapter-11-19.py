import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-19-1.xlsx') #读取工作簿。
ws=wb.active #读取活动工作表
ws.append(['张三',88,99]) #写入值为列表。
ws.append(('李四',88,99)) #写入值为元组。
ws.append(range(1,4)) #写入值为range生成器。
ws.append({'A':'小花','B':69,'C':96}) #写入值为字典1。
ws.append({1:'小曾',2:100,3:100}) #写入值为字典2。
wb.save('Chapter-11-19-2.xlsx') #另存工作簿。
