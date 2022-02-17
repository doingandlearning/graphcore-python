import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

# Read a csv file, get a Pandas DataFrame back.
dataframe = pd.read_csv('WorldCupWinners.csv')

wins = np.array(dataframe['Wins'])
teams = np.array(dataframe['Team'])

plt.xlabel('Element in array')
plt.ylabel('Value')
plt.bar(teams, wins)

plt.savefig("test.png")

plt.xlabel('Element in array')
plt.ylabel('Value')
plt.bar(teams, wins)
plt.savefig("test.png")

plt.show()
