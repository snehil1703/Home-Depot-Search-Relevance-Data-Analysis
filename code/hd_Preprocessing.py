# Importing required packages
import pandas 
import numpy

#Importing required files
import hd_DataAnalysis as sd
import hd_Preprocessing as prep

# Extracting the features of the three main attributes 
def feature_extraction(main_data):
	main_data['search_term'] = main_data['search_term'].map(lambda x: sd.preprocess_word(x))
	main_data['product_title'] = main_data['product_title'].map(lambda x: sd.preprocess_word(x))
	main_data['product_description'] = main_data['product_description'].map(lambda x: sd.preprocess_word(x))

	return main_data

# Create new features in the main data file
def add_attributes(main_data):

	# Integrating all the above three extracted features into a single column. 
	main_data['prod_combined_info'] = main_data['search_term'] + "\t" + main_data['product_title'] + "\t" + main_data['product_description']

	main_data['length_of_search_query'] = main_data['search_term'].map(lambda x: len(x.split())).astype(numpy.int64)

	main_data['length_of_title'] = main_data['product_title'].map(lambda x: len(x.split())).astype(numpy.int64)

	main_data['length_of_description'] = main_data['product_description'].map(lambda x: len(x.split())).astype(numpy.int64)

	main_data['query_in_title'] = main_data['prod_combined_info'].map(lambda x: sd.freq_of_words(x.split('\t')[0], x.split('\t')[1], 0))

	main_data['query_in_description'] = main_data['prod_combined_info'].map(lambda x: sd.freq_of_words(x.split('\t')[0], x.split('\t')[2], 0))

	main_data['title_commonWord'] = main_data['prod_combined_info'].map(lambda x: sd.find_common_words(x.split('\t')[0], x.split('\t')[1]))

	main_data['description_commonWord'] = main_data['prod_combined_info'].map(lambda x: sd.find_common_words(x.split('\t')[0], x.split('\t')[2]))
	
	print("Step2: Feature Extraction & Integrated attributes")
	return main_data
