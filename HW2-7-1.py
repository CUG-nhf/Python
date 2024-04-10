import numpy
from queue import Queue


def L(x):
	return (63 * x**5 - 70 * x**3 + 15*x)/8


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
        # 如何没找到根，则从中点分割区间再次查找
        # 如果区间足够小，则不再划分
        if (high - low > 1e-6):    
            mid = (low + high) / 2
            q.put((low, mid))
            q.put((mid, high))
            
print(roots)