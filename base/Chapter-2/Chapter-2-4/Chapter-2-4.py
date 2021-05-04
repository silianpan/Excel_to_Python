import xlrd #导入xlrd
wb=xlrd.open_workbook(r'Chapter-2-4-1.xlsx') #读取工作簿对象。
ws=wb.sheet_by_name('飞龙队') #读取工作表对象。
row_count=ws.nrows #返回工作表中已使用的行数。
col_count=ws.ncols #返回工作表中已使用的列数。
row_obj=ws.row(1)#返回工作表中指定行已使用的单元格对象。
row_val=ws.row_values(1)#返回工作表中指定行已使用的单元格的值。
col_obj=ws.col(0)#返回工作表中指定列已使用的单元格对象。
col_val=ws.col_values(0)#返回工作表中指定列已使用的单元格的值。
cell_obj=ws.cell(3,1)#返回工作表中指定行、列交叉单元格对象。
cell_val=ws.cell_value(3,1)#返回工作表中指定行、列交叉单元格的值。


