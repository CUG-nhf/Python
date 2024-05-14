import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)

# midpoint rule
def midpoint_rule(f, a, b, k):
    h = (b - a) / k
    integral = 0
    for i in range(k):
        x = a + (i + 0.5) * h
        integral += f(x)
    integral *= h
    return integral

# trapezoid rule
def trapezoid_rule(f, a, b, k):
    h = (b - a) / k
    integral = 0
    for i in range(k):
        x = a + i * h
        integral += (f(x) + f(x+h))
    integral *= (h/2)
    return integral

# Simpson's rule
def Simpson_rule(f, a, b, k):
    h = (b - a) / k
    integral = 0
    for i in range(k):
        x = a + i * h
        integral += (f(x) + 4*f(x+h/2) + f(x+h))
    integral *= (h/6)
    return integral

# 3-points Gauss
def gauss_rule(f, _a, _b, k):
    h = (_b - _a) / k
    integral = 0
    for i in range(k):
        a, b = _a + i * h, _a+(i+1)*h 
        integral += (b-a)/2*(f((b-a)/2*(-1/np.sqrt(3))+(a+b)/2)+f((b-a)/2*(1/np.sqrt(3))+(a+b)/2))
    return integral


integrals_midpoint = []
integrals_trapezoid = []
integrals_Simpsons = []
integrals_gauss = []

# 1. compute integrals
sizes = [2**i for i in range(1, 11)]
for size in sizes:
    integrals_midpoint.append( midpoint_rule(f, 0, 3, size))
    integrals_trapezoid.append( trapezoid_rule(f, 0, 3, size))
    integrals_Simpsons.append(Simpson_rule(f, 0, 3, size))
    integrals_gauss.append( gauss_rule(f, 0, 3, size))
    
integrals_midpoint = np.array(integrals_midpoint)
integrals_trapezoid = np.array(integrals_trapezoid)
integrals_Simpsons = np.array(integrals_Simpsons)
#integrals_Simpsoms = 2/3 * integrals_midpoint  + 1/3 * integrals_trapezoid
integrals_gauss = np.array(integrals_gauss)

# 2. compute Errors
true_val = f(3) - 1.0
error_midpoint = abs(true_val-integrals_midpoint)
error_trapezoid = abs(true_val-integrals_trapezoid)
error_Simpsom = abs(true_val-integrals_Simpsons)
error_gauss = abs(true_val-integrals_gauss)

# 3. fit Error = C*h^orrder
sizes = 1 / np.array(sizes)
cof_midpoint = np.polyfit(np.log10(sizes), np.log10(error_midpoint), 1)
cof_trapezoid = np.polyfit(np.log10(sizes), np.log10(error_trapezoid), 1)
cof_Simpsom = np.polyfit(np.log10(sizes), np.log10(error_Simpsom), 1)
cof_gauss = np.polyfit(np.log10(sizes), np.log10(error_gauss), 1)

# 4.plot figures
plt.loglog(sizes, error_midpoint, label=f"midpoint: C={np.round(np.power(10, cof_midpoint[1]),4)}, order={np.round(cof_midpoint[0],4)}")
plt.loglog(sizes, error_trapezoid, label=f'trapezoid: C={np.round(np.power(10, cof_trapezoid[1]),4)}, order={np.round(cof_trapezoid[0],4)}')
plt.loglog(sizes, error_Simpsom, label=f'Simpsom\'s: C={np.round(np.power(10, cof_Simpsom[1]),4)}, order={np.round(cof_Simpsom[0],4)}')
plt.loglog(sizes, error_gauss, label=f'3-points Gauss: C={np.round(np.power(10, cof_gauss[1]),4)}, order={np.round(cof_gauss[0],4)}')

plt.ylim(1e-15, 0)
plt.ylabel('abs error')
plt.xlabel('h')
plt.legend()
plt.show()