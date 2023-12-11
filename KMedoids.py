import cvxpy as cp
import numpy as np
from pulp import LpMaximize, LpProblem, LpVariable, lpDot
import warnings
import scipy.io

warnings.filterwarnings('ignore')

def Cvxpy(A, B, C):
    n = A.shape[1]
    x = cp.Variable(n).reshape((n, 1))
    prob = cp.Problem(cp.Maximize(A @ x), 
                    [B @ x <= C, x >= 0])

    prob.solve()

    print("Objective value:", prob.value)
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

small = scipy.io.loadmat('instance_small.mat')
medium = scipy.io.loadmat('instance_medium.mat')
large = scipy.io.loadmat('instance_large.mat')

state, obj, c_small = Cvxpy(small['A'], small['B'], small['C'])
state, obj,  c_medium = Cvxpy(medium['A'], medium['B'], medium['C'])
state, obj,  c_large = Cvxpy(large['A'], large['B'], large['C'])

state, obj,  p_small = PuLP(small['A'], small['B'], small['C'])
state, obj,  c_medium = Cvxpy(medium['A'], medium['B'], medium['C'])
state, obj,  c_large = Cvxpy(large['A'], large['B'], large['C'])
