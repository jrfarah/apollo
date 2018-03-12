# this program attemps to implement a dynamically selective prediction algorithm

# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy

# Load dataset
# downloads the url
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# give the names of the columns, the one named class is the one you'll be looking for
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# put the table into a PANDAS dataset object
dataset = pandas.read_csv(url, names=names)

# scatter plot matrix
# scatter_matrix(dataset)
# plt.show()

# Split-out validation dataset
# makes an array, each line is a tuple containing the relevant information for the "line"
array = dataset.values
# split the array into two arrays--one containing the contemplation information and the other
# containing the information we want to predict
X = array[:,0:4]
Y = array[:,4]
# what percentage of the data should be validation
validation_size = 0.20
# random seed
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'



# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
# after evaluation, dynamically select the correct model to use
# formula for adjusted/normalized success: 1-(1/(mean/std))
success = []
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	success.append((1-float((1/(cv_results.mean()/cv_results.std()))), model, name))
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

(rate, best_model, name) = (max(success)[0], max(success)[1], max(success)[2])
print rate, best_model, name

print type(X_validation)
numpy.append(X_validation, [5.5, 2.4, 3.8, 1.1] )

# Make predictions on validation dataset
neurNet = best_model
neurNet.fit(X_train, Y_train)
predictions = neurNet.predict(numpy.array([5.5, 2.4, 3.8, 1.5]).reshape(1,-1))
print X_validation
print predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

