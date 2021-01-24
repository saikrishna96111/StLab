import pandas as pd
import xlsxwriter
workbook = xlsxwriter.Workbook('C:\\Users\\Admin\\Desktop\\STLabPrgm\\student60.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0,'Name')
worksheet.write(0,1,'Marks1')
worksheet.write(0,2,'Marks2')
worksheet.write(0,3,'Marks3')
excel_file='C:\\Users\\Admin\\Desktop\\STLabPrgm\\stud.xlsx'
j=1
records = pd.read_excel(excel_file)
for i in records.index:
    if(records['Marks1'][i]<60 or records['Marks2'][i]<60 or records['Marks3'][i]<60):
        worksheet.write(j, 0, records['Name'][i])
        worksheet.write(j, 1, records['Marks1'][i])
        worksheet.write(j, 2, records['Marks2'][i])
        worksheet.write(j, 3, records['Marks3'][i])
        j+=1


workbook.close()
