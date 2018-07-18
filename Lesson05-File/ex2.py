'''
    new_queen_x2 = []
    for i in range(1,len(queen_x),2):
        #print(queen_x[i])
        new_queen_x2.append(queen_x[i])
    print(new_queen_x2)
'''
import csv

with open('AQI.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    AQI = []
    minimum=50
    min=''

    for row in reader:
 
        #print(row)
        #if row[2] !="AQI":
        if int(row[2])< minimum:
            minimum=int(row[2])
            min_city=row[0]
        else:
            pass

        #AQI.append(int(row[2]))

    print(str(min_city),'空氣最好','，AQI是',str(minimum))

       
        #print(AQI)
        #print(max(AQI))
        #print(max([AQI]))
     
    
        #AQI = [int(i) for i in AQI]
        #print("最大值為:",df.idxmax(axis=1))
        #print(row[2])
        #maxTemp.append(row[2])  n
        #p=reader['ColumnName'].max()

'''
# -*- coding: utf-8 -*-

import csv

with open('AQI2018.csv',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for column in reader:
        print(column[2], column[0])
print(column)

import csv
f = open('AQI2018.csv', 'r')
for row in csv.DictReader(f):
    print(row[1],row[2])
#for row in csv.reader(f):
 #   print row
f.close()
'''

  
 

        
    #column1 = [column[0]in range ] 
    #column2 = column[2]

  


#for i in range (len(column2)):
 #   column2[i]=int(column2[i])

#print(max(column2))
#print(max(column1))
        #index_2=index,max_2
        #location=column2(index_2)
        
 

#print(location)
