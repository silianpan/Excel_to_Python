import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-25-1.xlsx');ws=wb.active #读取工作簿与工作表。
ws.move_range('G8:J10',-5,3,False) #向上向右移动。
ws.move_range('G15:J16',4,-5,True) #向下向左移动。
wb.save('Chapter-11-25-2.xlsx')#另存工作簿。
