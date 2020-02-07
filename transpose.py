import csv
from os import path
from datetime import datetime

matrix = []
data = {}
control = 686 #unique starting control number for each property

with open('input1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        if row[0] != 'Total':
            matrix.append(row)

for i in range(0,len(matrix[0])):
    propName = ''
    if matrix[0][i] != '' and matrix[0][i] != 'Total':
        propName = matrix[0][i]

        for j in range(1,len(matrix)):
            if matrix[j][i] != '0.00':
                accountCode = matrix[j][1][0:4]+matrix[j][1][5:9]
                if propName in data:
                    data[propName].append([matrix[j][i], accountCode])
                else: data[propName] = [[matrix[j][i], accountCode]]

now = datetime.now().strftime("%Y%m%d%f")
filename = path.basename(__file__)[0:len(path.basename(__file__))-3] #get current script name

w = csv.writer(open(filename+" output "+now+".csv","w", newline=''))
w.writerow(['FinTrialBalances'])
w.writerow(['Transaction_Type','Control_Number','Blank_1','Blank_2','Transaction_Date','Post_Month','Reference','Notes','Property_Code','Amount','Account','Blank_3','Blank_4','Books','Remarks','Flag','Blank_5','Beginning_Balance','Blank_6','Blank_7','Segment1','Segment2','Segment3','Segment4','Segment5','Segment6','Segment7','Segment8','Segment9','Segment10','Segment11','Segment12'])

tempName = list(data.keys())[0]

for key, val in data.items():
    if tempName != key:
        tempName = key
        control += 1
    for k in range(len(val)):
        csv_array = []
        amount = val[k][0]
        account = val[k][1]
        csv_array.extend(('',control,'','','','','','',tempName,amount,account))
        w.writerow(csv_array)