import sys
sys.path.insert(0, '../core/')
sys.path.insert(0, '../prep/')
sys.path.insert(0, '../training_sets/')

import DataFormatterv1
import IterativeApproximation
import matplotlib.pyplot as plt
import math

dataset = DataFormatterv1.Format("../../training_sets/FormulaicDatasetSpecific.csv", names=['a', 'b', 'c', 'd'])

list_of_columns = [
	list(dataset.a.tolist()),
	list(dataset.b.tolist()),
	list(dataset.c.tolist()),	
	list(dataset.d.tolist()),
]

predict = [45, 13 , 3]
print "The value SHOULD be: ", (predict[0]**3 + predict[1]**2 + predict[2])

(bounds, history) = IterativeApproximation.IterativeApproximation(dataset, predict, list_of_columns, 0, 10, 25)

print "The value SHOULD be: ", (predict[0]**3 + predict[1]**2 + predict[2])
print "The program thinks the value lies between: "
print bounds

desirability = []
for point in history:
	print point
	desirability.append(1/(((point[1]-point[0]))*((history.index(point)-7.5)**10)))

print "It is most likely on this range: ", history[desirability.index(max(desirability[1:]))]

print desirability

plt.plot(desirability)
plt.show()

