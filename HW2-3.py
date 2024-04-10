import numpy as np
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def classical_gram_schmidt(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v -= R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    
    return Q, R

def backward_substitution(A, B):
    n = B.size
    X = np.zeros(n)
    X[n-1] = B[n-1] / A[n-1, n-1]
    for k in range (n-2, -1, -1):
        X[k] = (B[k] - A[k, k+1:] @ X[k+1:]) / A[k, k]
    return X

A = np.array([[1, 0, 0], 
              [0, 1, 0],
              [0, 0, 1],
              [-1, 1, 0],
              [-1, 0, 1],
			  [0, -1, 1]], dtype=float)

b = np.array([1237, 1941, 2417, 711, 1177, 475], dtype=float)


Q, R = classical_gram_schmidt(A)
print("Q 矩阵是：\n", Q)
print("R 矩阵是：\n", R)

x = backward_substitution(R, np.dot(Q.T, b))
print(f"得到的解 x 是:\n{x}^T")