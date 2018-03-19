import sys
sys.path.insert(0, '../core/')
sys.path.insert(0, '../prep/')
sys.path.insert(0, '../training_sets/')

import DataFormatterv1
import IterativeApproximation

dataset = DataFormatterv1.Format("../../training_sets/FormulaicDatasetSpecific.csv", names=['a', 'b', 'c', 'd'])

list_of_columns = [
	dataset.a.tolist(),
	dataset.b.tolist(),
	dataset.c.tolist(),	
	dataset.d.tolist(),
]

predict = [31, -40, -34]


(bounds, history) = IterativeApproximation.IterativeApproximation(dataset, predict, list_of_columns, 0, 10, 25)

print "The value SHOULD be: ", (predict[0]**3 + predict[1]**2 + predict[2])
print "The program thinks the value lies between: "
print bounds
