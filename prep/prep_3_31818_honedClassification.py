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
import matplotlib.pyplot as plt

# get dataset,
dataset = DataFormatterv1.Format("../training_sets/FormulaicDatasetSpecific.csv", names=['a', 'b', 'c', 'd'])
# dataset = DataFormatterv1.Format("../training_sets/dadsdataset.csv", names=['a', 'b', 'c', 'd'])

# convert every column into a list
# NEEDED BY THE PROGRAM
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


test = [31, 6, 34]

output = ClassificationNetv1.Predict(rotated, 3, test)
print output

if output == 1:
	boundaries = [v, boundaries[1]]
	sign = 1
elif output == 0:
	boundaries = [boundaries[0], v]
	sign = -1
 
history_of_boundaries.append(boundaries)

print "Sign:", sign

# v = random.randrange(0,max(important_column))
v = sign*0.0005*dataset.d.median()
print "V", v
number_of_iterations = 50
for iteration in range(number_of_iterations):
	del list_of_columns[-1]
	newclass_column = []
	motion = output
	print v
	if boundaries[0] == -1*numpy.inf or boundaries[1] == numpy.inf:
		v = 10*abs(v)
	else:
		v = abs(boundaries[0]) + abs(boundaries[1])
		v = float(abs(v/2))

	print v

	for res in important_column:
		if res >= sign*v:
			newclass_column.append(1)
		else:
			newclass_column.append(0)


	list_of_columns.append(newclass_column)
	new_dataframe = pandas.DataFrame(list_of_columns)
	rotated = pandas.DataFrame.transpose(new_dataframe)

	output = ClassificationNetv1.Predict(rotated, 3, test)

	if output == 1 and sign*v >= boundaries[0]:
		boundaries = [sign*v, boundaries[1]]
	elif output == 0 and sign*v <= boundaries[1]:
		boundaries = [boundaries[0], sign*v]

	print boundaries

	history_of_boundaries.append(boundaries)



print boundaries

# plt.hist(dataset.a.tolist(), 50)
# plt.show()
# raw_input()

# plt.hist(dataset.b.tolist(), 50)
# plt.show()
# raw_input()

# plt.hist(dataset.c.tolist(), 50)
# plt.show()
# raw_input()

plt.plot(history_of_boundaries)
plt.show()

# print history_of_boundaries