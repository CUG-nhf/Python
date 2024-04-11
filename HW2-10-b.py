import numpy as np
import matplotlib.pyplot as plt

# 函数
def rosenbrock(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

# 导函数
def rosenbrock_gradient(x):
    
    gradient = np.zeros_like(x, dtype=float)
    gradient[0] = -2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0]**2)
    gradient[1] = 200 * (x[1] - x[0]**2)
    return gradient

def H(x):

    gradient = np.zeros_like(x, dtype=float)
    gradient[0] = 2 - 400 * x[1] + 1200 * x[0]**2
    gradient[1] = -400 * x[0]

    gradient1 = np.zeros_like(x, dtype=float)
    gradient1[1] = 200
    gradient1[0] = -400 * x[0]
    
    return np.vstack((gradient, gradient1))

def newton(initial_guess, max_iterations=100, alpha = 0.01, tol=1e-6):
    x = initial_guess
    path = [x]
    for _ in range(max_iterations):
        gradient = rosenbrock_gradient(x)
        try:
            s = np.linalg.solve(H(x), -gradient)
        except np.linalg.LinAlgError:
            break

        x = x + s
        path.append(x)

        if np.linalg.norm(gradient) < tol:
            break

    return x, path

 
# x0 = np.array([-1, 1])
# x0 = np.array([0, 1])
x0 = np.array([2, 1])

result, path = newton(x0)  

x_coords = [point[0] for point in path]
y_coords = [point[1] for point in path]
    

# 绘图
fig = plt.figure()
ax = fig.add_subplot()

plt.plot(x_coords, y_coords, '-ro', linewidth=2)

plt.xlabel('x')
plt.ylabel('y')
plt.title(f'startpoint:{x0}, endpint:{result},\n minValue:{rosenbrock(result)}')
plt.show()