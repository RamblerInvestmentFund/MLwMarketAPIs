#File for Brianna Chou's Code
#Used Pandas and PyTorch
#PLEASE:
    #pip3 install pandas
import pandas as pd
import math

#Pandas
data = pd.read_csv('/Users/briannachou/Documents/GitHub/MLwMarketAPIs/Pull API/stock_data.csv', sep=',')
data.drop(data.columns[0], axis = 1, inplace = True) #Takes out the first column

#print (data.head(27)) #  First 5 rows

#Replaced the NaN values with the average of the values in that column
for column in data:
    print (data[column])
    for row in data[column]:
        if(math.isnan(row)):
            print(row)
            row = data[column].mean()
            print("REPLACED NaN value:")
            print (row)

        