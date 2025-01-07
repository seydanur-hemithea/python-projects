# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:20:19 2025

@author: asus
"""
#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('veriler.csv')

print(veriler)
x = veriler.iloc[:,1:4].values #bağımsız değişkenler
y = veriler.iloc[:,4:].values #bağımlı değişken
print(y)
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)
#LogisticRegression
from sklearn.linear_model import LogisticRegression
logr=LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred=logr.predict(X_test)
y_pred
print(y_pred)
print(y_test)
#KNeighborsClassifier
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print("cm")
print(cm)
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1,metric='minkowski')#neighbors arttığınds tahmin artar genelde ama bazı anlgoritmalarda düşürmek sitemin daha iyi çalışmasını sağlar burada olduğu gibi
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
cm=confusion_matrix(y_test,y_pred)
print("kncm")
print(cm)


from sklearn.svm import SVC
svc=SVC(kernel="rbf")#farklı kernel seçimleriyle tahminler iyileştirilmelidir
svc.fit(X_train,y_train)
y_pred=svc.predict(X_test)
#kernel tricklerlerle sınıflanıdrmayı 3.bir boyut yaratarak daha da iyiliştirebiliriz.

cm=confusion_matrix(y_test,y_pred)
print("SVC")
print(cm)


#naive bayes:ihtimalleri hesaplayark sınıflandrıma yapıyor, eğer veriler sürekli ise yani ondalıklı sayıgibi reel sayı gibi  gaussion naivebayes ile kulllanmak daha doğru olucaktır.nominal veri tiplerinde eğer int ifade kullanıyorsak ve bunları sınıflandıracaksak multinominal naive bayes kullanılır.Bernouilli naive bayeste ise ikili sınıflandırma varsa 0,1 gibi bu sınıflandırma tercih edilir. 

from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(X_train,y_train)
y_pred=gnb.predict(X_test)

cm=confusion_matrix(y_test,y_pred)
print("gnb")
print(cm)

#decision treee sınıflandırmasında information gain hesaplaması yapılarak treenin hangi değerden başlaması gerrektiğine karar verilir. en yüksek info gaine sahip olanla bailanır ve ağaç oluşturulur


from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(criterion='entropy') #ihtimalin log2 tabanındaki karşıllığıyla çarpılmasından elde edilen info gain kullanılır.gini de ihtimalin 2 olarak hesaplanan infor durumu vardır
dtc.fit(X_train,y_train)
y_pred=dtc.predict(X_test)
cm=confusion_matrix(y_test,y_pred)
print("dtc")
print(cm)


from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=10,criterion='entropy')
rfc.fit(X_train,y_train)
y_pred=rfc.predict(X_test)
cm=confusion_matrix(y_test,y_pred)
print("rfc")
print(cm)