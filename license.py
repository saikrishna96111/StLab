import pandas as pd
excel_file='D:\\covid\\7sem\\st\\practise\\sheet.xlsx'
records = pd.read_excel(excel_file)
number = int(input("Enter the licensce key you want to search: "))
found=0
for i in records.index:
    if(records['Key'][i] == number):
        print("License key found\n")
        found=1

if(found==0):
    print("License key not found\n")
