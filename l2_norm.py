import numpy as np

# Define matrix A and vector y
A = np.array([[1, 0, 1, 0, 0, 1], [0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 1]])

Ybar = np.array([[2, -1, -3, 0]])

# Compute the solution using the Moore-Penrose pseudoinverse
Xhat = np.linalg.pinv(A) @ Ybar.T

print("The optimal solution via l2 norm minimization is:\n", Xhat)
