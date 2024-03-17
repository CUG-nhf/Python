import numpy as np
import matplotlib.pyplot as plt

def compute_derivative(f, x, h):
    derivative = (f(x+h) - f(x-h)) / 2*h
    return derivative

x = 1
h = np.power(10, range(-16, 1), dtype=float)

approx_derivative = compute_derivative(np.cos, x, h)
true_derivative = -np.sin(x)
error = approx_derivative - true_derivative
print(approx_derivative, true_derivative, error)

print("Min error:", np.min(error), ",h of min-error:", h[np.argmin(error)])

plt.loglog(h, abs(error))
plt.xlabel('h')
plt.ylabel('Error')
plt.show()

print(np.sqrt(abs(3*(4/3-1)-1)))
