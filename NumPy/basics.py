import numpy as np

# my_list = [1, 2, 3, 4, 5]
# my_array = np.array(my_list)
# print(my_array)
# print(type(my_array))

# list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = np.array(list_2d)
# print(matrix)

# arange function:
# my_arange = np.arange(0, 10)
# print(my_arange)

# zero's function:
# zeros = np.zeros(5)
# print(zeros)

# zero's 2d:
# zeros_2d = np.zeros((5, 5))
# print(zeros_2d)

# ones function:
# ones = np.ones(5)
# print(ones)

# ones 2d:
# ones_2d = np.ones((5, 5))
# print(ones_2d)

# reshape function:
# arr = np.arange(1, 21)
# arr_2d = arr.reshape(5, 4)
# print(arr_2d)

# random array:
# ran = np.random.randint(1, 101, 36)
# print(ran)
# ran_2d = ran.reshape(6, 6)
# print(ran_2d)

# min and max:
# print(f"Minimum value: {ran_2d.min()}")
# print(f"Maximum value: {ran_2d.max()}")

# print(f"Index of minimum value: {ran_2d.argmin()}")
# print(f"Index of maximum value: {ran_2d.argmax()}")

# dimension and size
# ran = np.random.randint(1, 101, 36)
# ran_2d = ran.reshape(6, 6)
# print(f"Dimension: {ran_2d.shape}")
# print(f"Size: {ran_2d.size}")
# print(f"Memory size of Random 2D Array is {(ran_2d.size)*ran_2d.itemsize} bytes")

# comparison
# x = np.array([3, 5])
# y = np.array([2, 5])
# g_comp = np.greater_equal(x, y)
# l_comp = np.less_equal(x, y)
# print(f"Greater than or equal: {g_comp}")
# print(f"Less than or equal: {l_comp}")