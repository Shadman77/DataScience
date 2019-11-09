import numpy as np
import pandas as pd


def incrementIter():
    incrementIter.i += 1
    print(str(incrementIter.i) + ' -------- look below')


incrementIter.i = 0

# 1. Creating a series which is a labelled array using labels and data list
incrementIter()

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]

series = pd.Series(data=my_data)  # without specifying index
print(series)

series = pd.Series(data=my_data, index=labels)  # specifying index
print(series)

# specifying index, no need to use = if is in correct order
series = pd.Series(my_data, labels)
print(series)

# Series can hold all types of data types
print(pd.Series(labels))
print(pd.Series([sum, print, len]))

# 2. Creating a series which is a labelled array using numpy array
incrementIter()

arr = np.array(my_data)

series = pd.Series(arr)
print(series)

series = pd.Series(arr, labels)
print(series)

# 3. Creating a series which is a labelled array using dictionary
incrementIter()

dict = {'a': 10, 'b': 20, 'c': 30}
series = pd.Series(dict)
print(series)

# 4. Indexing, looking up data, fast because of hash tables
incrementIter()

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'BD', 'IND', 'AUS'])
print(ser1)

ser2 = pd.Series([1, 2, 5, 4], ['USA', 'BD', 'PAK', 'AUS'])
print(ser2)

print(ser1['BD'])

print(ser1 + ser2)