# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:20:26 2025

@author: asus
"""
import pandas as pd
veriler=pd.read_csv('Churn_Modelling.csv')
veriler

X=veriler.iloc[:,3:13].values
Y=veriler.iloc[:,13].values
from sklearn import preprocessing 
le=preprocessing.LabelEncoder()
X[:,1]=le.fit_transform(X[:,1])
le2=preprocessing.LabelEncoder()
X[:,2]=le2.fit_transform(X[:,2])

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ohe=ColumnTransformer([("ohe",OneHotEncoder(dtype=float),[1])],remainder='passthrough')
X=ohe.fit_transform(X)
X=X[:,1:]

from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(X,Y,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)

#ANN
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import keras
from keras.models import Sequential
from keras.layers import Dense

classifier=Sequential()
classifier.add(Dense(6,kernel_initializer = 'uniform',activation='relu',input_dim=11))#11 tane nitelik
classifier.add(Dense(6,kernel_initializer = 'uniform',activation='relu')) #girş katmanı lineer
classifier.add(Dense(1,kernel_initializer = 'uniform',activation='sigmoid'))#çıkış katmanı
#uniform dağılımı kullanıldır istenirse farklı dağılımlarda denenbilir
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])#1 ve 0 sıfır olan nominal değerler binomial değerlderdir

#veriler birden fazla kategoriden oluştuysa categorical entropy
#çok fazla boşluktan oluşan bir yapı varsa sparse categorcal netropy

classifier.fit(X_train,y_train,epochs=50)

y_pred=classifier.predict(X_test)
y_pred=(y_pred>0.5)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
cm
