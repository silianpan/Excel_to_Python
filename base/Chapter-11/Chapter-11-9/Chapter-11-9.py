import openpyxl #导入库。
wb=openpyxl.load_workbook('Chapter-11-9-1.xlsx') #读取工作簿。
wb.move_sheet(wb['1月'],2) #将'1月'工作表向右移2个工作表位置。
wb.move_sheet(wb['4月'],-1) #将'4月'工作表向左移1个工作表位置。
wb.save('Chapter-11-9-2.xlsx')# 另存工作簿。
