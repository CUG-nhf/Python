import cvxpy as cp
import numpy as np
from pulp import LpMaximize, LpProblem, LpVariable, lpDot
import warnings
import scipy.io
import time

warnings.filterwarnings('ignore')

def Cvxpy(A, B, C):
    n = A.shape[1]
    x = cp.Variable(n).reshape((n, 1))
    prob = cp.Problem(cp.Maximize(A @ x), 
                    [B @ x <= C, x >= 0])

    prob.solve(solver=cp.SCS)

    return prob.status, prob.value, x.value

def PuLP(A, B, C):
    prob = LpProblem(name="myProblem", sense=LpMaximize)
    
    n = A.shape[1]
    x = np.array([LpVariable(f'x{i}', lowBound=0) for i in range(n)])

    prob += lpDot(A.flatten(), x.flatten())
    for i in range(B.shape[0]):
        prob += (lpDot(B[i], x) <= C[i])

    prob.solve()

    # 输出结果
    return prob.status, prob.objective.value(), [i.value() for i in x]


def runer(model, data):
    start_time = time.time()
    state, obj, c_small = model(data['A'], data['B'], data['C'])
    end_time = time.time()
    execution_time = end_time - start_time
    print(state)
    print(obj)
    print(f"Execution time: {execution_time} seconds")
    return c_small


small = scipy.io.loadmat('instance_small.mat')
medium = scipy.io.loadmat('instance_medium.mat')
large = scipy.io.loadmat('instance_large.mat')



for data in [small, medium, large]:
    ls = []
    for model in [Cvxpy, PuLP]:
        x_value = runer(model, data)
        ls.append(x_value)
    print(np.array_equal(ls[0], ls[1]))
