import numpy
from queue import Queue


def L(x):
	return (63 * x**5 - 70 * x**3 + 15*x)/8

def derivative(x):
    return (315 * x**4 - 210 * x**2 + 15)/8


def solve_equation(low, high):
    while (high - low) > 1e-6:
        mid = (low + high) / 2
        if L(mid) == 0:
            roots.append(mid)
            return True, mid
        if L(mid) * L(low) < 0:
            high = mid
        else:
            low = mid
    # 如果在一个极小的区间内俩端点还是异号
    # 这把他们的中点作为零点
    if L(high)*L(low) < 0: 
        mid = (low + high) / 2
        roots.append(mid)
        return True, mid
    return False, -2


def newton_method(initial_guess):
    x = initial_guess
    while True:
        fx = L(x)
        f_prime_x = derivative(x)
        x_next = x - fx / f_prime_x
        if abs(x_next - x) < 1e-6:
            # 避免牛顿法找到零点已被二分法找到
            for r in roots:
                if abs(r - x_next) < 1e-6:
                    return 
            roots.append(x_next)
            return
        x = x_next

roots = []
q = Queue()
q.put((-1, 1))

while(q.empty() == False):
    (low, high) = q.get()
    find_zero, zero_point = solve_equation(low, high)
    if find_zero:
        # 如果找到根，则从零点分割区间再次查找	
        q.put((low, zero_point-1e-6))
        q.put((zero_point+1e-6, high))
    else:  
        # 如何没找到根，则用牛顿法找
        if (high - low > 1e-6):    
            newton_method((low + high) / 2)
            
print(roots)