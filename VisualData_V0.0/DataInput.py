import csv
from operator import index
reader = csv.reader(    open(".\\VisualData_V0.0\\TestData2.csv"), delimiter=";")
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

   


#X values
xValues=data[0]
xLabel=xValues[0]
del xValues[0]
xValuesDouble=list(map(float,xValues))

#Y values
yValues=data[1]
yLabel=yValues[0]
del yValues[0]
yValuesDouble=list(map(float,yValues))

#Z values
zValues=data[2]
zLabel=zValues[0]
del zValues[0]
for index, a in enumerate(zValues):
    temp=zValues[index].replace(",",".")
    zValues[index]=temp


zValuesDouble=list(map(float,zValues))


print(xValues)

