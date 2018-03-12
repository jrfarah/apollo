# add filepaths to sys path import
import sys
sys.path.insert(0, '../core/')
sys.path.insert(0, '../prep/')
sys.path.insert(0, '../training/')

import pandas
import MainNetv1

# Load dataset
# downloads the url
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# give the names of the columns, the one named class is the one you'll be looking for
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# put the table into a PANDAS dataset object
dataset = pandas.read_csv(url, names=names)

prediction = MainNetv1.Predict(dataset, 4, [5.5, 2.4, 3.8, 1.5])
print prediction