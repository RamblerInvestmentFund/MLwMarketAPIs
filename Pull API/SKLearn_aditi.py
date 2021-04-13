#set up environment
import os
import time
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#Load data
current_path = os.getcwd()
file_path = current_path + '/Christian Stock Data/SNAP_data.csv'
stock_data = pd.read_csv(file_path)                                                                #read in stock data



#clean + prepare data
for i, row in stock_data.iterrows():                                                               #convert dates to epoch
    format = "%Y-%m-%d %H:%M:%S"
    stock_data.loc[i,'date'] = int(time.mktime(time.strptime(stock_data.loc[i,'date'], format)))

for column in stock_data:                                                                          #fill in missing values with column means
    stock_data[column] = stock_data[column].fillna(stock_data[column].mean)


X = stock_data.drop(columns=['5. volume'])                                                         #create training data sets and testing data sets (last column 'volume' is the "answer")
y = stock_data['5. volume']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


#train model + make predictions
model = DecisionTreeClassifier()                                                                   #define model
model.fit(X_train,y_train)                                                                         #fit training data sets
predictions = model.predict(X_test)                                                                #make predictions

#measure accuracy
score = accuracy_score(y_test, predictions)                                                        #compare testing data set with predictions
print(score)

#Notes: accuracy score is 0.0 on every run, picked a random model to use from the library, not really sure what its doing
