# this program tries to predict a numerical value using classifications

# add filepaths to sys path import
import sys
sys.path.insert(0, '../src/core/')
sys.path.insert(0, '../src/prep/')
sys.path.insert(0, '../training_sets/')

import DataFormatterv1
import ClassificationNetv1
import pandas
import numpy
import random
import math

# get dataset
dataset = DataFormatterv1.Format("../training_sets/FormulaicDatasetSpecific.csv", names=['a', 'b', 'c', 'd'])

# convert every column into a list
list_of_columns = [
	dataset.a.tolist(),
	dataset.b.tolist(),
	dataset.c.tolist(),	
	dataset.d.tolist(),
]

del list_of_columns[-1]

important_column = dataset.d.tolist()

boundaries = [-1*numpy.inf, 1*numpy.inf]
history_of_boundaries = [boundaries]
print boundaries

# decide if it is greater than or less than or zero
newclass_column = []
v = 0
for res in dataset.d.tolist():
	if res >= v:
		newclass_column.append(1)
	else:
		newclass_column.append(0)

list_of_columns.append(newclass_column)
new_dataframe = pandas.DataFrame(list_of_columns)
rotated = pandas.DataFrame.transpose(new_dataframe)

output = ClassificationNetv1.Predict(rotated, 3, [-45, 2, -7])

if output == 1:
	boundaries = [v, boundaries[1]]
	sign = 1
elif output == 0:
	boundaries = [boundaries[0], v]
	sign = -1

history_of_boundaries.append(boundaries)

# v = random.randrange(0,max(important_column))
v = sign*10
number_of_iterations = 25
for iteration in range(number_of_iterations):
	del list_of_columns[-1]
	newclass_column = []
	motion = output
	print v
	if boundaries[0] == -1*numpy.inf or boundaries[1] == numpy.inf:
		v = 2*v
	else:
		v = boundaries[0] + boundaries[1]
		v = v/2

	print v

	for res in important_column:
		if res >= sign*v:
			newclass_column.append(1)
		else:
			newclass_column.append(0)


	list_of_columns.append(newclass_column)
	new_dataframe = pandas.DataFrame(list_of_columns)
	rotated = pandas.DataFrame.transpose(new_dataframe)

	output = ClassificationNetv1.Predict(rotated, 3, [3, 1, -7])

	if output == 1 and sign*v >= boundaries[0]:
		boundaries = [sign*v, boundaries[1]]
	elif output == 0 and sign*v < boundaries[1]:
		boundaries = [boundaries[0], sign*v]

	history_of_boundaries.append(boundaries)



print boundaries
# print history_of_boundaries