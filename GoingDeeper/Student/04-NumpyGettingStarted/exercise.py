import numpy as np
import pandas as pd

dataframe = pd.read_csv("BergenWeather2019.csv")
print(dataframe["Precipitation"].dtype)

precipitation = np.array(dataframe["Precipitation"], dtype="float32")
