###################################################################################
# Version 1 of the main neural network implementation
# this will attempt to functionalize the code drawn up in prep2
# and include a way for external programs to interface with this module
# note: this module will ONLY include customization relevant to the data analysis 
# portion, not the data formatting portion
# from there every part of this will be expanded and customized
#
# things that are passed into the function: 
# - dataset, array of names
###################################################################################

valve = ""

# IMPORTS #########################################################################

# add filepaths to sys path import
import sys
sys.path.insert(0, '../interface/')
sys.path.insert(0, '../prep/')
sys.path.insert(0, '../training/')

# rest of the regular imports
import 	numpy
import 	pandas
import 	matplotlib.pyplot as plt
from 	pandas.plotting 				import scatter_matrix
from 	sklearn 						import model_selection
from 	sklearn.metrics 				import classification_report
from 	sklearn.metrics 				import confusion_matrix
from 	sklearn.metrics 				import accuracy_score
from 	sklearn.linear_model 			import LogisticRegression
from 	sklearn.tree 					import DecisionTreeClassifier
from 	sklearn.neighbors 				import KNeighborsClassifier
from 	sklearn.discriminant_analysis 	import LinearDiscriminantAnalysis
from 	sklearn.naive_bayes 			import GaussianNB
from 	sklearn.svm 					import SVC

# METHODS ########################################################################

def getValidation(dset, prediction_column_index):
	'''	extract a validation dataset from the full one
	'''
	reduced_dataset = dset.values

	# split the array into two arrays--one containing the contemplation information and the other containing the information we want to predict

	prediction_column 		= reduced_dataset[:, prediction_column_index]
	contemplation_columns 	= numpy.delete(	reduced_dataset, 
											prediction_column_index, 
											axis = 1 )
	print prediction_column 	# PC
	print contemplation_columns	# CC

	# percentage of data to be used for validation
	validation_size = 0.20

	# set random seed for initial matrices
	seed = 7

	# get the training and validation models (to be passed on)
	CC_train, CC_validation, PC_train, PC_validation = model_selection.train_test_split(contemplation_columns, prediction_column, test_size=validation_size, random_state=seed)

	return CC_train, CC_validation, PC_train, PC_validation


def spotCheckAlgorithms(CC_train, CC_validation, PC_train, PC_validation):
	

def Predict(dset, prediction_column_index):
	'''	coalesces all of the other functions into one thing; 
		will return prediction
	'''
	# split the datasets between validation and prediction
	CC_train, CC_validation, PC_train, PC_validation = getValidation(dset, prediction_column_index)

	# spot check the various algorithms to determine the best model for use in this case






