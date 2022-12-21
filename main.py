import numpy as np
my_matrix = np.array([[1, 2, 1], [3, 4, 7], [3, 6, 3]])
print(my_matrix)
rank = np.linalg.matrix_rank(my_matrix)
print("Rank of the given Matrix is : ",rank)
