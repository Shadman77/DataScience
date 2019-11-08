import numpy as np


def incrementIter():
    incrementIter.i += 1
    print(str(incrementIter.i) + ' -------- look below')


incrementIter.i = 0

# 1. Bracket Indexing and Selection
incrementIter()
np_array = np.arange(0, 11)
print(np_array[1:5])  # get values in a range
print(np_array[0:5])  # get values in a range
print(np_array[5])  # get value at the position

# 2. Brodcasting
incrementIter()
print(np_array)
np_array[1:5] = 100
print(np_array)

# 3. Slicing
incrementIter()
slice_np_array = np_array[1:5]
print(slice_np_array)

# 4. Copying
incrementIter()
slice_np_array[:] = 5
print(slice_np_array)
print(np_array)  # changes occured in the original array as well
np_array = np.arange(0, 11)
# copying a portion of the array
slice_np_array = np_array[0:5].copy()
print(slice_np_array)
slice_np_array[:] = 200
print(slice_np_array)
print(np_array)

# 5. Indexing 2d array
incrementIter()
np_mat = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(np_mat)
print(np_mat[0,0])
print(np_mat[0])
# Slice notation
print(np_mat[:2,:2])

# 6. Boolean 
incrementIter()
np_array = np.arange(1,11)
print(np_array)
np_bool = np_array >= 5
print(np_bool)
# Comparison selection
print(np_array[np_bool])

# 7. Conditional selection
incrementIter()
print(np_array[np_array > 5])
print(np_array[np_array <= 5])