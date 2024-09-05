import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors

cars = pd.read_csv('.\\data\\mtcars.csv')
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
print("DataFrame shape:", cars.shape)
print("DataFrame columns:", cars.columns)
# Define target values
t = [15, 300, 160, 3.2]

# Correctly select columns by index
X = cars.iloc[:, [1, 3, 4, 6]].values  # Use list instead of tuple

# Print the first 5 rows of X
print(X[0:5])

nbrs = NearestNeighbors(n_neighbors=1).fit(X)
print(nbrs.kneighbors([t]))