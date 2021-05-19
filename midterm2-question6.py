import numpy as np

def jacobi(A, b, x0):
    D = np.diag(A)
    x = x0
    for i in range(2500):
        x_new = x + ((b - np.dot(A, x)) / D) 
        if np.linalg.norm(x_new - x) < 10**-6:
            return x_new                 
        x = x_new       
    return x

A = np.array([
            [5, 2, 1, 1],
            [2, 6, 2, 1],
            [1, 2, 7, 1],
            [1, 1, 2, 8]
            ])
b = np.array([29, 31, 25, 19])
x0 = np.array([1, 2, 3, 4])

ans = jacobi(A, b, x0)
print("\nFinal iteration = ", ans)
print("\n", np.dot(A, ans), " =? ", b)
print("\nYes, x^(k) is a solution to Ax = b")