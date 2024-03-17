import numpy as np
import math

def my_exp(x):
	s, n = 1.0, 1
	while(n<30):
		s += np.power(x, n) / math.factorial(n)
		n += 1

	return s

x = [-1, 1, -5, 5, -10, 10, -15, 15, -20, 20]

for i in x:
	print(f"x={i},  IS={my_exp(i)},  exp(x)={np.exp(i)},  error={abs(my_exp(i)-np.exp(i))}")