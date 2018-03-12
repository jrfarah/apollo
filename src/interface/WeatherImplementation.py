# this program will use past data to predict whether it will rain tomorrow

import sys
sys.path.insert(0, '../core/')
sys.path.insert(0, '../prep/')
sys.path.insert(0, '../training_sets/')

import pandas
import ClassificationNetv1


filepath = "../../training_sets/reduced_weather_data.data"
names = ["Day of the year","High","low","Snow or not"]
dataset = pandas.read_csv(filepath, names=names)
prediction = ClassificationNetv1.Predict(dataset, 3, [73, 35, 29])
print prediction
