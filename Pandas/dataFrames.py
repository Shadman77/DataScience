import numpy as np
import pandas as pd

# random numbers
from numpy.random import randn
# setting seed so that it generates the same random numbers as in the tutorial
np.random.seed(101)


def incrementIter(param):
    incrementIter.i += 1
    print()
    print(str(incrementIter.i) + ' -------- ' + str(param) + ' -------- ')


incrementIter.i = 0

# 1. Creating random data frame
incrementIter('Creating random data frame')
# each column is a pandas series, they share a common index
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

# 2. Selecting columns from data frame
incrementIter('2. Selecting columns from data frame')
print(df['W'])  # selecting W column
print(type(df['W']))  # type of series
print(df[['W', 'Z']])  # Selecting multiple columns

# 3. Selecting rows from data frame
incrementIter('3. Selecting rows from data frame')
print(df.loc['C'])
print(df.iloc[2])

# 4. Selecting rows and columns from data frame
incrementIter('4. Selecting rows and columns from data frame')
print(df)
print(df.loc['B', 'Y'])
# Subset of the data frame
print(df.loc[['A', 'B'], ['W', 'Y']])

# 5. Conditional Selection
incrementIter('5. Conditional Selection')
print(df > 0)
print(df[df > 0])
# for a column
print(df['W'] > 0)
print(df[df['W'] > 0])
print(df[df['W'] > 0]['X'])
# using two conditions
print(df[(df['W'] > 0) & (df['Y'] > 1)])

# 6. Reset Index
incrementIter('6. Reset Index')
print(df)
print(df.reset_index())  # need to use inplace

# 7. Setting Index
incrementIter('7. Setting Index')
newIndex = 'CA NY WY OR CO'.split()
print(newIndex)
df['States'] = newIndex
print(df)
print(df.set_index('States'))  # needs inplace

# 8. Creating new column
incrementIter('8. Creating new column')
df['new'] = df['W'] + df['Y']
print(df)

# 9. Deleting column
incrementIter('9. Deleting column')
# axis = 0 for rows and 1 for columns, the change does not happen to the original df
print(df.drop('new', axis=1))
print(df)
# this time the change happens to the original df as well
df.drop(labels='new', axis=1, inplace=True)
print(df)

# 10. Deleting row
incrementIter('10. Deleting row')
print(df.drop('E'))
df.drop(labels='E', inplace=True)
print(df)

# 11. Multiple Index
incrementIter('11. Multiple Index')
# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))  # returns of tuple of pairs
hier_index = pd.MultiIndex.from_tuples(hier_index) # converts to multi index
# Making data frame
df = pd.DataFrame(randn(6, 2), index=hier_index, columns=['A', 'B'])
print(df)
print(df.loc['G1'])
print(df.loc['G1'].loc[1])
print(df.loc['G2'].loc[2]['B'])

# 12. Naming Index
incrementIter('12. Naming Index')
print(df.index.names) # get the names of the index
df.index.names = ['Groups', 'Num']
print(df)
