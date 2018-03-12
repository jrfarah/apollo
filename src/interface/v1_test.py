# test of the classification and data formatting module

# add filepaths to sys path import
import sys
sys.path.insert(0, '../core/')
sys.path.insert(0, '../prep/')
sys.path.insert(0, '../training_sets/')

import pandas
import ClassificationNetv1

# Load dataset
# downloads the url
url = "https://archive.ics.uci.edu/mlz/machine-learning-databases/iris/iris.data"
# give the names of the columns, the one named class is the one you'll be looking for

filepath = "../../training_sets/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# put the table into a PANDAS dataset object
dataset = pandas.read_csv(filepath, names=names)

prediction = ClassificationNetv1.Predict(dataset, 4, [5.5, 2.4, 3.8, 1.5])
print prediction