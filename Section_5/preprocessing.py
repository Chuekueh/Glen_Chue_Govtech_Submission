import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split


car_data = pd.read_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/Data/car_data.csv', names = 
                       ['buying','maint','doors','persons','lug_boot','safety','class'])

#Set Index to preserve order of rows:
car_data['row_num'] = np.arange(len(car_data))
car_data['row_num'] = car_data.reset_index().index

# Non-dummified Dataset 
non_dummy = car_data
non_dummy.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/Data/non_dummy.csv', header=True)

#Splitting Data into training and testing Datasets without stratifying based on class 
X = non_dummy.drop(['buying','row_num'],axis=1)
y = non_dummy['buying']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Print the buying distribution in the train and test sets
print("Buying distribution in train set:")
print(y_train.value_counts(normalize=True))
print("Class distribution in train set:")
print(X_train['class'].value_counts(normalize=True))
print("\nBuying distribution in test set:")
print(y_test.value_counts(normalize=True))
print("Class distribution in test set:")
print(X_test['class'].value_counts(normalize=True))

X_train.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/ML_Data/Non_Stratified_80_20/train_features.csv')
y_train.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/ML_Data/Non_Stratified_80_20/train_label.csv')
X_test.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/ML_Data/Non_Stratified_80_20/test_features.csv')
y_test.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/ML_Data/Non_Stratified_80_20/test_label.csv')


#Splitting Data into training and testing Datasets with stratifying based on class
#Splitting Data into training and testing Datasets without stratifying based on class 
X = non_dummy.drop(['class','row_num'],axis=1)
y = non_dummy['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)

# Print the buying distribution in the train and test sets
print("Class distribution in train set:")
print(y_train.value_counts(normalize=True))
print("buying distribution in train set:")
print(X_train['buying'].value_counts(normalize=True))
print("\nClass distribution in test set:")
print(y_test.value_counts(normalize=True))
print("buying distribution in test set:")
print(X_test['buying'].value_counts(normalize=True))

final_y_train = X_train['buying']
final_X_train = X_train.merge(y_train, left_index=True, right_index=True, how='left')

final_y_test = X_test['buying']
final_X_test = X_test.merge(y_test, left_index=True, right_index=True, how='left')

final_X_train.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/ML_Data/Stratified_75_25/train_features.csv')
final_y_train.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/ML_Data/Stratified_75_25/train_label.csv')
final_X_test.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/ML_Data/Stratified_75_25/test_features.csv')
final_y_test.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_5/ML_Data/Stratified_75_25/test_label.csv')
print('done')

