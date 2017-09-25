### Checking variance of data and see if we need to do any sort of feature scaling
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import matplotlib.pyplot as plt
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

''''----- Splitting data into testing and training set-----'''
sepal_1=[]
sepal_2=[]
petal_1=[]
petal_2=[]
for data in features_train:
    sepal_1.append(data[0])
    sepal_2.append(data[1])
    petal_1.append(data[2])
    petal_2.append(data[3])

Sepal_Combined=[]
Petal_Combined=[]

for i in range(0,len(sepal_1)):
    Sepal_Combined.append([sepal_1[i],sepal_2[i]])
for i in range(0,len(petal_1)):
    Petal_Combined.append([petal_1[i],petal_2[i]])
''''------------Extraction sepal parameters and petal parameters------------'''
pca_Sepal=PCA(n_components=1)
pca_Petal=PCA(n_components=1)

pca_Sepal.fit(Sepal_Combined)
pca_Petal.fit(Petal_Combined)

Sepal_train=pca_Sepal.transform(Sepal_Combined)
Petal_train=pca_Petal.transform(Petal_Combined)

#print Sepal_train

'''-----Visualizing the data ------------'''
Flowers=['Iris-setosa','Iris-versicolor','Iris-virginica']
Feature_train=[]
for i in range(0,len(Sepal_train)):
    Feature_train.append([Sepal_train[i][0],Petal_train[i][0]])
    if labels_train[i]==Flowers[0]:
         pass
         plt.plot(Sepal_train[i],Petal_train[i],color="r",marker='x')
    if labels_train[i]==Flowers[1]:
         pass
         plt.plot(Sepal_train[i],Petal_train[i],color="b",marker='x')
    if labels_train[i]==Flowers[2]:
         pass
         plt.plot(Sepal_train[i],Petal_train[i],color="g",marker='x')
plt.xlabel("Sepal")
plt.ylabel("Petal")
plt.show()

#print Feature_train
'''-- Converting test data into PCA -----'''
sepal_1=[]
sepal_2=[]
petal_1=[]
petal_2=[]
for data in features_test:
    sepal_1.append(data[0])
    sepal_2.append(data[1])
    petal_1.append(data[2])
    petal_2.append(data[3])

Sepal_Combined=[]
Petal_Combined=[]

for i in range(0,len(sepal_1)):
    Sepal_Combined.append([sepal_1[i],sepal_2[i]])
for i in range(0,len(petal_1)):
    Petal_Combined.append([petal_1[i],petal_2[i]])

Sepal_test=pca_Sepal.transform(Sepal_Combined)
Petal_test=pca_Petal.transform(Petal_Combined)
Features_test=[]
for i in range(0,len(Sepal_test)):
    Features_test.append([Sepal_test[i][0],Petal_test[i][0]])
   
'''-----Evalutaion of the data--------'''
def Show_Accuracy(clf):
     clf.fit(Feature_train,labels_train)

     from sklearn.metrics import accuracy_score
     from sklearn.metrics import precision_score
     from sklearn.metrics import recall_score
     print "Accuracy",accuracy_score(clf.predict(Features_test),labels_test),"Precision",precision_score(clf.predict(Features_test),labels_test,average='macro'),"Recall",recall_score(clf.predict(Features_test),labels_test,average='macro')
     
for model in [SVC(),GaussianNB(),DecisionTreeClassifier()]:
     clf=model
     Show_Accuracy(clf)






