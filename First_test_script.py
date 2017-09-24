### Checking variance of data and see if we need to do any sort of feature scaling
import pandas
d=pandas.read_csv("data_set.txt")
#print d
#print d.describe()
'''-----------------------feature has all the features and labels has all the data-------------------------------------'''

File=open("data_set.txt","r")
data=File.read()
File.close()
Split=data.split(',')
z=''
New_data=[]
for i in Split:
     if len(i.split('\n'))==2:
         New_data.append(i.split('\n')[0])
         New_data.append(i.split('\n')[1])
     else:
         New_data.append(i)
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
'''-----------------------
We see all the features have nearly the same domain of values 0-10
so no need to do any sort of feature scaling and stuff
-------------------------------------'''


'''--------SPlitting data into training and testing test------------'''
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


from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.svm import SVC
for models in [SVC(),GaussianNB(),DecisionTreeClassifier()]:
     clf=models
     from sklearn.metrics import accuracy_score
     clf.fit(np.array(features_train),np.array(labels_train))
     print "Accuracy",accuracy_score(clf.predict(np.array(features_test)),np.array(labels_test))
