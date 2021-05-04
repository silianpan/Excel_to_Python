import xlrd#导入xlrd库。
wb=xlrd.open_workbook('Chapter-3-12-1.xlsx')#读取工作簿。
ws=wb.sheet_by_name('成绩表')#读取工作表。
col_vals=ws.col_values(1)#获取工作表指定列已用单元格区域的值。
for score in col_vals:#循环列区域的每个值。
    if type(score)==float and score>=90:#判断条件表达式是否成立。
        print(score,'优秀')#条件成立，则执行。
