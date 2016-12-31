# Importing the required packages
import pandas
import os

# Reading the files of train, product descriptions and attributes datasets
hd_train = pandas.read_csv(os.path.dirname(os.path.abspath(__file__))+"/Dataset/input/train.csv", encoding = "ISO-8859-1")
hd_desc = pandas.read_csv(os.path.dirname(os.path.abspath(__file__))+"/Dataset/product_descriptions.csv", encoding = "ISO-8859-1")
hd_attrib = pandas.read_csv(os.path.dirname(os.path.abspath(__file__))+"/Dataset/attributes.csv")

# Combining the product descriptions with the train data
hd_train = pandas.merge(hd_train, hd_desc, on="product_uid", how="left")

# Getting the actual number and count of products
products = pandas.DataFrame(pandas.Series(hd_train.groupby(["product_uid"]).size(), name="Count_Of_Product"))
hd_train = pandas.merge(hd_train, products, left_on="product_uid", right_index=True, how="left")

# Getting the brand names and renaming it to seller
brands = hd_attrib[hd_attrib.name == "MFG Brand Name"][["product_uid", "value"]].rename(columns={"value": "Name_Of_Seller"})
hd_train = pandas.merge(hd_train, brands, on="product_uid", how="left")
hd_train.Name_Of_Seller.fillna("NA", inplace=True)

# Generating the output data
print("#################Product Statistics####################")
print(str(hd_train.describe()))

