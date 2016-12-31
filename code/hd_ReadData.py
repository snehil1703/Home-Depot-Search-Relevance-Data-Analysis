# Importing required packages
import numpy
import pandas
import os

# Function to read the csv files 
def read_data(trainD, testD, prodD):

	# Reading all the files
	print("Step1: Reading the files of train, test and product description datasets")

	# Reading all the files 
	homeDepot_train = pandas.read_csv(os.path.dirname(os.path.abspath(__file__))+"/Dataset/input/train.csv", encoding = "ISO-8859-1")

	homeDepot_test = pandas.read_csv(os.path.dirname(os.path.abspath(__file__))+"/Dataset/input/test.csv", encoding = "ISO-8859-1")

	homeDepot_productDescription = pandas.read_csv(os.path.dirname(os.path.abspath(__file__))+"/Dataset/product_descriptions.csv", encoding = "ISO-8859-1")

	return homeDepot_train, homeDepot_test, homeDepot_productDescription
