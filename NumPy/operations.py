import numpy as np


def incrementIter():
    incrementIter.i += 1
    print(str(incrementIter.i) + ' -------- look below')


incrementIter.i = 0

# 1. Adding array
incrementIter()
arr1 = np.arange(1,11)
arr2 = np.arange(11,21)
print(arr1)
print(arr2)
print(arr1 + arr2)

# 2. Scalar operation array
incrementIter()
print(arr1)
print(arr1 + 50)

# 3. Warning
incrementIter()
arr1 = np.arange(0,10)
print(arr1)
print(arr1 / arr1)

# 4. Exponents
incrementIter()
print(arr1 ** 2)

# 5. Universal operators
incrementIter()
print(np.sqrt(arr1 ** 2))
print(np.max(arr1))
print(np.sin(arr1))