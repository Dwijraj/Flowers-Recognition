### Checking variance of data and see if we need to do any sort of feature scaling
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import pandas
d=pandas.read_csv("data_set.txt")
#print d
#print d.describe()
'''-----------------------
We see all the features have nearly the same domain of values 0-10
so no need to do any sort of feature scaling and stuff
-------------------------------------'''
File=open("data_set.txt","r")
data=File.read()
File.close()
Split=data.split(',')
z=''
New_data=[]
for i in Split:
     if len(i.split('\n'))==2:
             New_data.append((i.split('\n')[0]))
             New_data.append((i.split('\n')[1]))
        
     else:
             New_data.append((i))
             pass
modified=[]
feature=[]
label=[]
data_point=[]
counter=0
#print New_data
for i in range(0,len(New_data)):
     counter=counter+1
     if counter%5==0:
          counter=0
          feature.append(data_point)
          data_point=[]
          label.append(New_data[i])
     else:
          data_point.append(float(New_data[i]))

#print feature[:5]
#print label
'''-----------------------feature has all the features and labels has all the data-------------------------------------'''
features_train=[]
features_test=[]
labels_train=[]
labels_test=[]
for data_1 in feature[:30]:
     features_train.append(data_1)
for data_1 in feature[51:81]:
     features_train.append(data_1)
for data_1 in feature[100:131]:
     features_train.append(data_1)

for data_1 in label[:30]:
     labels_train.append(data_1)
for data_1 in label[51:81]:
     labels_train.append(data_1)
for data_1 in label[100:131]:
     labels_train.append(data_1)

for data_1 in feature[31:52]:
     features_test.append(data_1)
for data_1 in feature[81:101]:
     features_test.append(data_1)
for data_1 in feature[131:]:
     features_test.append(data_1)

for data_1 in label[31:52]:
     labels_test.append(data_1)
for data_1 in label[81:101]:
     labels_test.append(data_1)
for data_1 in label[131:]:
     labels_test.append(data_1)
'''---
Applying PCA
----'''
#print features_train
#print labels_train
import numpy as np
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
pca.fit(np.array(features_train))
d=pca.transform(np.array(features_train))

#First=d.components_[0]
#Second=d.components_[1]

import matplotlib.pyplot as plt

Flowers=['Iris-setosa','Iris-versicolor','Iris-virginica']
Feature_train=[]
for i in range(0,91):
    Feature_train.append([d[i][0],d[i][1]])
    if labels_train[i]==Flowers[0]:
         pass
         plt.plot(d[i][0],d[i][1],color="r",marker='x')
    if labels_train[i]==Flowers[1]:
         pass
         plt.plot(d[i][0],d[i][1],color="b",marker='x')
    if labels_train[i]==Flowers[2]:
         pass
         plt.plot(d[i][0],d[i][1],color="g",marker='x')
plt.show() ##Gives a clear Idea of data
'''
     Prediciting accuracy of various machine learning models on the data set
'''

#for model in List_Models:
def Show_Accuracy(clf):
     clf.fit(Feature_train,labels_train)

     Features_test=[]
     test_data=pca.transform(np.array(features_test))
     for i in range(0,60):
          Features_test.append([test_data[i][0],test_data[i][1]])
     from sklearn.metrics import accuracy_score
     print "Accuracy",accuracy_score(clf.predict(Features_test),labels_test)


from sklearn.naive_bayes import GaussianNB
for model in [SVC(),GaussianNB(),DecisionTreeClassifier()]:
     clf=model
     Show_Accuracy(clf)
















