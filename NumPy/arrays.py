import numpy as np


def incrementIter():
    incrementIter.i += 1
    print(str(incrementIter.i) + ' -------- look below')


incrementIter.i = 0

# 1. Convert list to NumPy array
incrementIter()
my_list = [1, 2, 3]
print(my_list)
np_array = np.array(my_list)
print(np_array)

# 2. Convert list of list to NumPy matrix
incrementIter()
my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_mat)
np_matrix = np.array(my_mat)
print(np_matrix)

# 3. Create NumPy array using arange
incrementIter()
np_array = np.arange(0, 10)
print(np_array)
np_array = np.arange(0, 10, 2)  # step size of 2
print(np_array)


# 4. Create NumPy array using zeros
incrementIter()
np_array = np.zeros(3)
print(np_array)
np_array = np.zeros((3, 4))
print(np_array)

# 5. Create NumPy array using ones
incrementIter()
np_array = np.ones(3)
print(np_array)
np_array = np.ones((3, 4))
print(np_array)

# 6. Create NumPy array using linspace
incrementIter()
np_array = np.linspace(1,5,10)
print(np_array)

# 7. Create Identity matrix
incrementIter()
np_matrix = np.eye(4)
print(np_matrix)

# 8. Array and Matrix of a specified shape and random numbers from uniform distribution from 0 to 1
incrementIter()
np_array = np.random.rand(5)
print(np_array)
np_matrix = np.random.rand(5,5)
print(np_matrix)

# 9. Array and Matrix of a specified shape and random numbers from normal distribution around 0
incrementIter()
np_array = np.random.randn(2)
print(np_array)
np_matrix = np.random.randn(5,5)
print(np_matrix)

# 10. Array and Matrix of a specified shape and random integers form low to high
incrementIter()
np_array = np.random.randint(1,100,5)
print(np_array)

# 11. Reshape NumPy array
incrementIter()
np_array = np.arange(25)
print(np_array)
np_matrix = np_array.reshape(5,5)
print(np_matrix)