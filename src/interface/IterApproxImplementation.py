import sys
sys.path.insert(0, '../core/')
sys.path.insert(0, '../prep/')
sys.path.insert(0, '../training_sets/')

import DataFormatterv1
import IterativeApproximation
import matplotlib.pyplot as plt
import math
import random

difflist = []

def measure_correctness(list_of_columns, dataset):
	predict = [random.uniform(-50,50), random.uniform(-50,50) , random.uniform(-50,50), random.uniform(-50,50)]
	# print( "The value SHOULD be: ", (predict[0]**3 + predict[1]**2 + predict[2]))

	(bounds, history) = IterativeApproximation.IterativeApproximation(dataset, predict, list_of_columns, start_v = 0, second_v=1, num_iter=25, show_graph=False)

	print( SECTION)
	# print( "The value SHOULD be: ", (predict[0]**3 + predict[1]**2 + predict[2]))
	# print( "The value SHOULD be: ", (predict[0]*(2.71**(-predict[1]+predict[2]))))
	# print( "The value SHOULD be: ", predict[0]*math.cos(predict[)0]*predict[1]+predict[2])
	print( "The value SHOULD be: ", ((predict[0]+predict[1])/(((predict[2]+predict[3])**2))+0.001))
	print( "The program thinks the value lies between: ")
	print( bounds)
	print( SECTION)

	act = math.fabs(bounds[0]+bounds[1])/2
	diff = math.fabs(act-(((predict[0]+predict[1])/(((predict[2]+predict[3])**2)+0.001))))/act
	difflist.append(diff)



dataset = DataFormatterv1.Format("../../training_sets/dividendtest.csv", names=['a', 'b', 'c', 'd', 'e'])

SECTION = "========================================================"

list_of_columns = [
	list(dataset.a.tolist()),
	list(dataset.b.tolist()),
	list(dataset.c.tolist()),	
	list(dataset.d.tolist()),
	list(dataset.e.tolist())
]

N = 100
for i in range(N):
	measure_correctness(list_of_columns, dataset)

# desirability = []
# for point in history:
# 	# print( point)
# 	desirability.append(1/(((point[1]-point[0]+0.00001))*((history.index(point)-7.5)**10)))

# print( "It is most likely on this range: ", history[desirability.index(max()desirability[1:]))]

# print( desirability)

# plt.plot(desirability)
# plt.show()

plt.hist(difflist, bins=100)
plt.xlabel('Percent diff')
plt.show()

raw_input()
plt.hist(difflist, bins=50, range=range(0,2))
plt.xlabel('Percent diff')
plt.show()

