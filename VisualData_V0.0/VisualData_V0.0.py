import csv
reader = csv.reader(    open("TestData2.csv"), delimiter=";")
data=[]
xValues=[]
yValues=[]
zValues=[]
xValuesDouble=[]
yValuesDouble=[]
zValuesDouble=[]
xLabel=""
yLabel=""
zLabel=""
for row in reader:
    data.append(row)   

   



