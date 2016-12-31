#!/usr/bin/python
#  Importing Required files and variables
from hd_dataMerge import hd_train

data = hd_train

# Frequency Distribution of Product Titles
freqDist_prodTitle = data['product_title'].value_counts(sort=False,dropna=False)
print ("\n################ Product Titles Frequency Distribution ###############\n")
print (freqDist_prodTitle)

# Frequency Distribution of Search Terms
freqDist_searchTerm = data['search_term'].value_counts(sort=False,dropna=False)
print ("\n################### Search Terms Frequency Distribution ################\n")
print (freqDist_searchTerm)

# Frequency Distribution of Sellers
freqDist_seller = data['Name_Of_Seller'].value_counts(sort=False,dropna=False)
print ("\n#################### Sellers Frequency Distribution ###################\n")
print (freqDist_seller)
