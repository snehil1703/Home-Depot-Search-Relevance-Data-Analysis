#!/usr/bin/python

# Importing required packages
import numpy 
import pandas 
import os
import sys
import csv

#Importing required files
import hd_ReadData as read
import hd_DataAnalysis as sd
import hd_Algorithm as model
import hd_Preprocessing as prep
import hd_visualization as visual



# Applying data preprocessing algorithm to the columns in main data file 
def data_processesing(main_data):
	main_data['search_term'] = main_data['search_term'].map(lambda x: sd.preprocess_word(x))
	main_data['product_title'] = main_data['product_title'].map(lambda x: sd.preprocess_word(x))
	main_data['product_description'] = main_data['product_description'].map(lambda x: sd.preprocess_word(x))

	return main_data

# Create new features in the main data file
def add_attributes(main_data):

	# Adding all the above 3 into 1 column. 
	main_data['prod_combined_info'] = main_data['search_term'] + "\t" + main_data['product_title'] + "\t" + main_data['product_description']

	main_data['length_of_search_query'] = main_data['search_term'].map(lambda x: len(x.split())).astype(numpy.int64)

	main_data['length_of_title'] = main_data['product_title'].map(lambda x: len(x.split())).astype(numpy.int64)

	main_data['length_of_description'] = main_data['product_description'].map(lambda x: len(x.split())).astype(numpy.int64)

	main_data['query_in_title'] = main_data['prod_combined_info'].map(lambda x: sd.freq_of_words(x.split('\t')[0], x.split('\t')[1], 0))

	main_data['query_in_description'] = main_data['prod_combined_info'].map(lambda x: sd.freq_of_words(x.split('\t')[0], x.split('\t')[2], 0))

	main_data['title_commonWord'] = main_data['prod_combined_info'].map(lambda x: sd.find_common_words(x.split('\t')[0], x.split('\t')[1]))

	main_data['description_commonWord'] = main_data['prod_combined_info'].map(lambda x: sd.find_common_words(x.split('\t')[0], x.split('\t')[2]))

	return main_data

def main(trainD, testD, prodD, visualD, combineD):

	homeDepot_train, homeDepot_test, homeDepot_productDescription = read.read_data(trainD, testD, prodD)

	print ("")
	import hd_freqDist
	print("")

	# Calculate the total number of rows
	rows_in_train = homeDepot_train.shape[0]

	# Concatenating the train and test file and merging the two DataFrames based on product's UID 
	hd_main = pandas.concat((homeDepot_train, homeDepot_test), axis = 0, ignore_index = True)

	hd_main = pandas.merge(hd_main, homeDepot_productDescription, how = 'left', on = 'product_uid')

	hd_main = (hd_main)

	# Adding the new attributes to the data file 
	hd_main = prep.add_attributes(hd_main)

	hd_main.to_csv(os.path.dirname(os.path.abspath(__file__)) + "/Output/CSV/hd_combinedfile.csv", encoding = "ISO-8859-1", index = False)

	print("")
	if os.path.isfile(combineD):
		input_file = open(combineD, 'r+')
	else:
		print ("File does NOT exist")
		sys.exit()

	csvr = csv.reader(input_file)
	for i in range(100):
		print (csvr.next())
	print("")

    # Removing the redundant columns from the main file 
	hd_main = hd_main.drop(['search_term', 'product_title', 'product_description', 'prod_combined_info'], axis = 1)

	# Splitting the main data file created above into train and test 
	hd_train = hd_main.iloc[:rows_in_train]

	hd_test = hd_main.iloc[rows_in_train:]

	id_test = hd_test['id']

	# Creating train and test files to be passed to the analysis model
	xTrain = hd_train.drop(['id', 'relevance'], axis = 1).values

	yTrain = hd_train['relevance'].values

	xTest = hd_test.drop(['id', 'relevance'], axis = 1).values

	# Calling the analysis module and passing the train and test files as parameters 
	model.RF(xTrain, yTrain, xTest, id_test)

	print("")
	if os.path.isfile(visualD):
		input_file = open(visualD, 'r+')
	else:
		print("File does NOT exist")
		sys.exit()

	csvr = csv.reader(input_file)
	for i in range(100):
		print(csvr.next())
	print("")

	#Different types of Visualization
	visual.LineChart(visualD)
	visual.Histogram(visualD)
	visual.Wordcloud(trainD,testD,combineD)
	visual.PieChart(visualD)
	visual.ScatterPlot(visualD)


if __name__ == '__main__':

	homeDepot_train = os.path.dirname(os.path.abspath(__file__))+"/Dataset/input/train.csv"
	homeDepot_test = os.path.dirname(os.path.abspath(__file__))+"/Dataset/input/test.csv"
	homeDepot_productDescription = os.path.dirname(os.path.abspath(__file__))+"/Dataset/product_descriptions.csv"
	homeDepot_visualization = os.path.dirname(os.path.abspath(__file__)) + "/Output/CSV/BigDataOutput.csv"
	homeDepot_combinedData = os.path.dirname(os.path.abspath(__file__)) + "/Output/CSV/hd_combinedfile.csv"

	main(homeDepot_train, homeDepot_test, homeDepot_productDescription,homeDepot_visualization,homeDepot_combinedData)
