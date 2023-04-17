# -*- coding: utf-8 -*-
"""Kidney disease

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xNsue-LgwyEEmbtIINWjsVk5KuW-0oR1

# task 1: problem understanding

## 1) specify business problem

## 2) business requirement
## 3) literature survey 
## 4) social/business impact


# task 2: data understanding
## 1) data collection
## 2) loading data


# task 3: EDA 
## 1) data cleaning 
## 2) data manipulation
## 3) visualization


# task 4: model building 

# task 5: testing the model
# task 6: deployment
# task 7: document
"""

# Importing required lib

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings 
warnings.filterwarnings('ignore')

# checking for available styles

plt.style.available

# Applying styles to notebook

plt.style.use('fivethirtyeight')

# Reading csv data
df = pd.read_csv('/content/kidney_disease.csv') 
df.head()

# univariate analysis - extracting info from a single column

# checking data distribution

plt.figure(figsize=(15,8))
plt.subplot(121)
sns.distplot(df['age'])
plt.subplot(122)
sns.distplot(df['al'],color='green')

# creating dumy dataframe for categorical values 

df_cat =df.select_dtypes(include='float')
df_cat.head()



import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(20,12))
sns.set(font_scale=2.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('Comparison of Model by Classification Metric')
plt.savefig('./benchmark_models_performance.png',dpi=300)

for i,j in enumerate(df_cat):
  print(j)

# visualizing counts in each variable

plt.figure(figsize=(18,4))
for i,j in enumerate(df_cat):
  plt.subplot(1,11,i+1)
  sns.countplot(df[j])

# Bivariate analysis - extracting info from double column

# visualizing the relation between cad, al, pcc & bp


plt.figure(figsize=(30,8))
plt.subplot(111)
sns.countplot(data=df,x='age',hue='classification')

plt.figure(figsize=(30,8))
plt.subplot(222)
sns.countplot(data=df,x='age',hue='bp')

# finding relation between age_ & bp

pd.crosstab(df['age'],df['bp'])

# multivariate analysis - extract info from more than 2 columns

sns.swarmplot(data=df,x='al',y='su',hue='rbc')

sns.swarmplot(data=df,x='pc',y='hemo',hue='classification')

#finding corr

sns.heatmap(df.corr())

# descriptive analysis _ descriptive stot
df.describe(include='all')

# data preprocessing

# finding the shape of data
df.shape

# finding null values
df.isnull().any()

df.isnull().sum().sum()

print(df['age'].mean())

print(df['age'].mean())
df['age'] = df['age'].fillna(51.483)
print(df.isnull().sum())

print(df['bp'].mean())
print(df['al'].mean())
print(df['su'].mean())
print(df['bgr'].mean())
print(df['bu'].mean())
print(df['sc'].mean())
print(df['sod'].mean())
print(df['pot'].mean())
print(df['hemo'].mean())

print(df['bp'].mean())
df['bp'] = df['bp'].fillna(76.469)
print(df.isnull().sum())

print(df['sg'].mean())
df['sg'] = df['sg'].fillna(1.01)
print(df.isnull().sum())

print(df['al'].mean())
df['al'] = df['al'].fillna(0.450)
print(df.isnull().sum())

print(df['su'].mean())
df['su'] = df['su'].fillna(148.0)
print(df.isnull().sum())

print(df['bu'].mean())
df['bu'] = df['bu'].fillna(57.4)
print(df.isnull().sum())

print(df['sc'].mean())
df['sc'] = df['sc'].fillna(3.07)
print(df.isnull().sum())

print(df['sod'].mean())
df['sod'] = df['sod'].fillna(137.5)
print(df.isnull().sum())

print(df['pot'].mean())
df['pot'] = df['pot'].fillna(4.62)
print(df.isnull().sum())

print(df['hemo'].mean())
df['hemo'] = df['hemo'].fillna(12.5)
print(df.isnull().sum())

# coverting object datatype to int

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder

# Encoding
#Encoding with replace method
df['rbc'] = df['rbc'].replace({'normal' :1,'abnormal' :0})
df.head()

# Encoding
#Encoding with replace method
df['pc'] = df['pc'].replace({'normal' :1,'abnormal' :0})
df.head()

# Encoding
#Encoding with replace method
df['pcc'] = df['pcc'].replace({'present' :1,'notpresent' :0})
df.head()

# Encoding
#Encoding with replace method
df['ba'] = df['ba'].replace({'present' :1,'notpresent' :0})
df.head()

# Encoding
#Encoding with replace method
df['pcv'] = df['pcv'].replace({'NaN' :1})
df.head()

# Encoding
#Encoding with replace method
df['wc'] = df['wc'].replace({'NaN' :1})
df.head()

# Encoding
#Encoding with replace method
df['htn'] = df['htn'].replace({'no' :0,'yes' :1})
df.head()

# Encoding
#Encoding with replace method
df['dm'] = df['dm'].replace({'no' :0,'yes' :1})
df.head()

# Encoding
#Encoding with replace method
df['cad'] = df['cad'].replace({'no' :0,'yes' :1})
df.head()

# Encoding
#Encoding with replace method
df['appet'] = df['appet'].replace({'poor' :0,'good' :1})

df.head()

# Encoding
#Encoding with replace method
df['pe'] = df['pe'].replace({'no' :0,'yes' :1})
df.head()

# Encoding
#Encoding with replace method
df['ane'] = df['ane'].replace({'no' :0,'yes' :1})
df.head()

# Encoding
#Encoding with replace method
df['ane'] = df['ane'].replace({'ckd' :1})
df.head()

# finding dtype
df.info()

# finding outliers
sns.boxplot(df['bp'])

# finding the count of outliers
# IQR = q3-q1...,ub=q3+(1.5*IQR),lb=q1-(1.5*IQR)
q1 = np.quantile(df['bp'],0.25)
q3 = np.quantile(df['bp'],0.75)

print('Q1={}'.format(q1))
print('Q3={}'.format(q3))

IQR =q3-q1

print('IQR value is {}'.format(IQR))

upperbound = q3+(1.5*IQR)
lowerbound = q1-(1.5*IQR)

print('the upper bound value is {} & the lower bound value is {}'.format(upperbound,lowerbound))

print('skwed data :',len(df[df['bp']>upperbound]))

# handling outliers

from scipy import stats

plt.figure(figsize=(15,4))
plt.subplot(131)
sns.distplot(df['bp'])
plt.subplot(132)
stats.probplot(np.log(df['bp']),plot=plt)
plt.subplot(133)
sns.distplot(np.log(df['bp']))

# transforming normal value to log values

df['al']=np.log(df['al'])
df.head()

stats.probplot(np.log(df['bp']))

df['bp']=np.log(df['bp'])

df.head()

# Encoding

# Encoding with list comp

df['bp']=[0 if x=='LOW' else 1 if x=='NORMAL' else 2 for x in df['bp']]

df.head()

# encoding with replace method

df ['pc'] = df ['pc'].replace({'normal':0,'high':1})
df.head()

# encoding with replace method

df ['rbc'] = df ['rbc'].replace({'normal':0,'high':1})
df.head()

# encoding with replace method

df ['pcc'] = df ['pcc'].replace({'normal':1,'high':0})
df.head()

# spliting dep & indep variables

x=df.drop('classification',axis=1)
x.head()
y=df['classification']
y

# spliting dep & indep variables

x=df.drop('classification',axis=1)
x.head()

# visualizing data points
import matplotlib.pyplot as plt

"""Simple Linear Regression"""

# importing required lib

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("/content/kidney_disease.csv")   #loading the csv data

df.head() #return you the first 5 rows values

df.columns

catcols=set(df.dtypes[df.dtypes=='0'].index.values) 
print(catcols)

# Descript stat

df.describe()

# checking null values

df.isnull().sum()

sns.distplot(df.age)

# visualizing data points
import matplotlib.pyplot as plt
plt.scatter(df['bp'],df['hemo'])

# independent variable

x=df.iloc[:,0:1]
x.head()

# dependent variable

y=df.iloc[:,5:]
y.head()

# split training & testing 

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest= train_test_split(x,y,test_size=0.1,random_state=11)

print(xtrain.shape)
print(xtest.shape)

xtrain

ytrain

catcols=['anemia','pedal_edema','appetite','bacteria','class','coronary_artery_disease','diabetesmellit',
   
         'hypertension','pus_cell','pus_cell_clumps','red_blood_cells']

contcols=set(df.dtypes[df.dtypes!='0'].index.values)

print(contcols)

for i in contcols:
  print("Continous Columns :",i)
  print((df[i]))
  print('*'*120+'/n')

contcols.remove('su')
contcols.remove('al')
contcols.remove('sg')
print(contcols)

contcols.add('red_blood_cell_count')
contcols.add('packed_cell_volume')
contcols.add('white_blood_cell_count')
print(catcols)

contcols.add('specific_gravity')
contcols.add('albumin')
contcols.add('sugar')
print(catcols)

df.describe()

import matplotlib.pyplot as plt # import the matplotlib libaray
fig=plt.figure(figsize=(5,5)) #plot size
plt.scatter(df['age'],df['bp'],color='blue')
plt.xlabel('age') #set the label for x-axis
plt.ylabel('bp') #set the label for y-axis
plt.title("age vs bp scatter plot") #set a title for the axes

f,ax=plt.subplots(figsize=(18,18))
sns.heatmap(df.corr(),annot=True,fmt=".2f",ax=ax,linewidths=0.5,linecolor="orange")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()

"""
# Multi Linear Regression"""

# multi linear reg

# import necessary lib
import numpy as np
import pandas as pd
# reading the data
df = pd.read_csv('/content/kidney_disease.csv')
df.head()

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(20, 12))
sns.set(font_scale=2.5)
g = sns.boxplot(x="model", y="values", hue="metrics", df=results_long_nofit, palette="set3")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('Comparison of Model by Classification Metric')
plt.savefig('./benchmark_models_performance.png',dpi=300)

"""MLR-Poly

## 1) Problem Understand
## 2) Data Understanding
## 3) EDA
## 4) Model Building
## 5) Testing model
## 6) Deployment
## 7) Docs
"""

# importing req lib

import numpy as np # Numerical pyton
import pandas as pd # for data manupulation
import matplotlib.pyplot as plt # for visualization
from sklearn.preprocessing import PolynomialFeatures # polynomial regression
from sklearn.linear_model import LinearRegression # checking accuracy

# reading csv data

df = pd.read_csv('/content/kidney disease.csv')
df.head()

# finding dtype
df.info()

"""Logisitic Regression"""

# import req lib

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('/content/kidney disease.csv')
df.head(10)

# Descriptive stat 

df.describe()

df.shape

# finding dtype
df.info()

df.drop(columns=['wc', 'pcv', 'rc', 'dm', 'cad', 'classification'])

df['pcc'].unique()

# feature mapping 
df['pcc'].replace({"present":1,"female":0},inplace=True)

# spliting independent & dependent variable
x = df.drop('su',axis=1)
y = df['su']
y

# spliting training data & testing data

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=10)

print("shape of independent training data is {}. shape of independent testing data is {}".format(xtrain.shape, xtest.shape))
print("shape of dependent training data is {}. shape of dependent testing data is {}".format(ytrain.shape, ytest.shape))

# initializing logistic reg 
log_r = LogisticRegression()

ytest

# Evaluating model 
from sklearn.metrics import classification_report, confusion_matrix

"""classification"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from scipy import stats

# read and run the data

df = pd.read_csv('/content/kidney disease.csv')
df.head()

sns.boxplot(df['hemo'])

# finding the count of outliers
q1 = np.quantile(df['id'],0.25)
q3 = np.quantile(df['id'],0.75)

IQR =q3-q1

upperbound = q3+(1.5*IQR)
lowerbound = q1-(1.5*IQR)

skewed_values = len(df[df['id']>upperbound])

print('Q1 = {}'.format(q1))
print('Q3 = {}'.format(q3))
print('IQR = {}'.format(IQR))
print('upper bound = {}'.format(upperbound))
print('lower bound = {}'.format(lowerbound))
print('count of skewed data = {}'.format(skewed_values))

# Handling outliers
def transform(variable):
  plt.figure(figsize=(14,6))
  plt.distplot(variable)
  stats.probplot(variable,plot=plt)

"""Navie bayes"""

from sklearn import naive_bayes
import pandas as pd
import numpy as np

df = pd.read_csv('/content/kidney_disease.csv') 
df.head()

df['rbc'] = df['rbc'].replace({'normal' :1,'abnormal' :0})
df['pc'] = df['pc'].replace({'normal' :1,'abnormal' :0})
df['pcc'] = df['pcc'].replace({'present' :1,'notpresent' :0})
df['ba'] = df['ba'].replace({'present' :1,'notpresent' :0})
df['pcv'] = df['pcv'].replace({'NaN' :1})
df['wc'] = df['wc'].replace({'NaN' :1})
df['htn'] = df['htn'].replace({'no' :0,'yes' :1})
df['dm'] = df['dm'].replace({'no' :0,'yes' :1})
df['cad'] = df['cad'].replace({'no' :0,'yes' :1})
df['appet'] = df['appet'].replace({'poor' :0,'good' :1})
df['pe'] = df['pe'].replace({'no' :0,'yes' :1})
df['ane'] = df['ane'].replace({'no' :0,'yes' :1})
df['ane'] = df['ane'].replace({'ckd' :1})
df.info()

#spliting denpendent &independent 

x = df.iloc[:,1:]
y = df.iloc[:,0]

y

col_name = x.columns

#manual encoding

x = np.where(x=='y',1,x)
x = np.where(x=='n',0,x)
x = np.where(x=='?',1,x)

x = pd.DataFrame(x,columns=col_name)
x.head()

"""ANN Regression"""

# importing the keras libraries and packages
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# creating ANN skleton view

classifications  = Sequential()
classifications.add(Dense(30,activation='relu'))
classifications.add(Dense(128,activation='relu'))
classifications.add(Dense(64,activation='relu'))
classifications.add(Dense(32,activation='relu'))
classifications.add(Dense(1,activation='sigmoid'))

# Compiling the ANN model

classifications.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

classifications.compile(optimizer='rmsprop', loss='mse', metrics=['mse'])

classifications.predict([[3535.56,575757.63,5465.657,5]])

classifications.predict([[457436.56,68578.63,986456.657,1]])