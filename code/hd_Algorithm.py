# Importing required packages
import pandas 
import numpy
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor
import os


def RF(xTrain, yTrain, xTest, id_test): 

	# Applying the random forrest regressor model with number_of_trees = 12 and max_depth = 5 for each tree
	randomForrest = RandomForestRegressor(n_estimators = 12, max_depth = 5)
	classifier = BaggingRegressor(randomForrest, n_estimators = 55, max_samples = 0.1, random_state = 25)

	print("Step3: Algorithm Implementation and Classifier fitting")

	# Fitting the data into train and test data of the classifier 
	classifier.fit(xTrain, yTrain)

	# Predicting the search relevance value
	yPred = classifier.predict(xTest)

	print("Step4: Output Generation")

	# Writing the output to a csv file
	pandas.DataFrame({"id": id_test, "relevance": yPred}).to_csv(os.path.dirname(os.path.abspath(__file__)) + "/Output/CSV/BigDataOutput.csv", index = False)
