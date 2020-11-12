# test of the classification and data formatting module

# add filepaths to sys path import
import sys
sys.path.insert(0, '../core/')
sys.path.insert(0, '../prep/')
sys.path.insert(0, '../training_sets/')

import DataFormatterv1
import ClassificationNetv1

# put the table into a PANDAS dataset object
dataset = DataFormatterv1.Format("../../training_sets/FormulaicDataset.csv")

print (ClassificationNetv1.Predict(dataset, 3, [-45, 2, -7]))