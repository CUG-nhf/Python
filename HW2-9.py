import math
import numpy as np

def golden_section_search(f, a, b, epsilon=1e-5):
   
    golden_ratio = (math.sqrt(5) - 1) / 2
    
    x1 = b - golden_ratio * (b - a)
    x2 = a + golden_ratio * (b - a)
    y1, y2 = f(x1), f(x2)
    
    while abs(b - a) > epsilon:
        if y1 < y2:
            b = x2
            x2, y2 = x1, y1
            x1 = b - golden_ratio * (b - a)
            y1 = f(x1)
        else:
            a = x1
            x1, y1 = x2, y2
            x2 = a + golden_ratio * (b - a)
            y2 = f(x2)

    return (a + b) / 2


def f(x):
    # return 0.5 - 1 * x * np.exp(-x**2)
    return 1 - 0.3 * x * np.exp(-x**2)

# 搜索区间
a = 0
b = 2

# 执行黄金分割搜索
result = golden_section_search(f, a, b)

print(f"mininum point: x = {result}, f(x) = {f(result)}")