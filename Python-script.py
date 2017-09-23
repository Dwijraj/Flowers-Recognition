#Loading the libraries required
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt   #For visualiztion
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score #Getting the accuracy
### Various models that we will use to find the best fir for our data set
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

##Getting the data set (Loading it)
url="data_set.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

#print "Dimension of dataset",dataset.shape

##Visualizing the data_set in matrix form
#print "Sample run",dataset.head(20)

'''
The below step is required to get the domain of each feature(range of values)
it helps to determine if we need to process the data before feeing it to the algorithm
like feature scaling and stuff
'''
#print dataset.describe()
#print dataset.groupby('class').size()
'''Visualizing the data set on graph'''
#dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
#dataset.hist()
scatter_matrix(dataset)
plt.show()
