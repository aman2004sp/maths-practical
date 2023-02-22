import numpy as np

def transition_matrix(transitions):
    n = 1+ max(transitions) #number of states

    M = [[0]*n for _ in range(n)]

    for (i,j) in zip(transitions,transitions[1:]):
        M[i][j] += 1

    #now convert to probabilities:
    for row in M:
        s = sum(row)
        if s > 0:
            row[:] = [f/s for f in row]
    return M


arr = np.array([[2,0,1],
                [1,2,0],
                [1,1,1]])
y = ([3.65, 1.55, 3.42])

for i in range(3):
    print(f"Vector {i+1}: ",end="")
    for j in range(3):
        print(arr[j][i],end=" ")
    print()


if (np.linalg.det(arr)):
    print(">>Set of Vectors are linearly independent.")
else:
    print(">>Set of Vectors are linearly dependent.")

print("\nLinear Combination :-")
lin = np.linalg.solve(arr, y)
print(lin)

print("\nTransition Matrix :-")
arr_1d = arr.ravel()
m = transition_matrix(arr_1d)
for row in m:
    print(' '.join('{0:.2f}'.format(x) for x in row))
