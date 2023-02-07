import numpy as np
from sympy import Matrix
  
M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]])
print("Matrix : {} ".format(M))
   
# Use sympy.rref() method 
M_rref = M.rref()  
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))
my_matrix = np.array([[1, 2, 1], [3, 4, 7], [3, 6, 3]])
print(my_matrix)
rank = np.linalg.matrix_rank(my_matrix)
print("Rank of the given Matrix is : ",rank)     


import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print(f'Original Array:\n{arr1}')

arr1_transpose = arr1.transpose()

print(f'Transposed Array:\n{arr1_transpose}')
