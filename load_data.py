# Import libraries

import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt 
np.random.seed(42)


# load the dataset - using pandas .read_excel
df = pd.read_excel('AB Test.xlsx')


# show the dataframe head
df.head()


# show dataframe info
df.info()

