import pandas as pd
import numpy as np

filepath = "DataAnalysis\lab_module1\laptop_pricing_dataset_base.csv"
df = pd.read_csv(filepath, header = None)
headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg" , "Price"]

df.columns = headers

df.replace('?', np.nan, inplace = True)

# Print the data types of the dataframe columns
print(df.dtypes)
# Print the statistical description of the dataset, including that of 'object' data types.
print(df.describe(include="all"))

#print the summary informatino of the dataset
print(df.info())

