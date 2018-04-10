# test of the classification and data formatting module

# add filepaths to sys path import
import sys
sys.path.insert(0, '../core/')
sys.path.insert(0, '../prep/')
sys.path.insert(0, '../training_sets/')

import DataFormatterv1
import ClassificationNetv1

from numba import jit
from timeit import default_timer as timer

# put the table into a PANDAS dataset object
dataset = DataFormatterv1.Format("../../training_sets/FormulaicDataset.csv")

fastClassification_predict = jit(nopython=True)(ClassificationNetv1.Predict)

print "OLD"
t0 = timer()
print ClassificationNetv1.Predict(dataset, 3, [-45, 2, -7])
tpython = (timer() - t0) 
print "TIME: ", tpython

# this doesn't work!!

print "NEW"
t0 = timer()
print fastClassification_predict(dataset, 3, [-45, 2, -7])
tnumba = (timer() - t0) 
print "TIME: ", tnumba
tnumba = (timer() - t1) 
print "TIME: ", tnumba

