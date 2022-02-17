import numpy as np
import pandas as pd

# Read a csv file, get a Pandas DataFrame back.
dataframe = pd.read_csv('WorldCupWinners.csv')

print(dataframe)
# # Get the 'Team' column.

for col in dataframe:
    print(dataframe[col])
