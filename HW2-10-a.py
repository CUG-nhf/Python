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

# 最速下降
def steepest_descent(initial_guess, max_iterations=100, tol=1e-6):
    x = initial_guess
    path = [x]
    for _ in range(max_iterations):
        gradient = rosenbrock_gradient(x)
        alpha = line_search(x, gradient)
        x = x - alpha * gradient
        path.append(x)

        if np.linalg.norm(gradient) < tol:
            break

    return x, path

# 线性搜索
def line_search(x, gradient, max_iterations=100, beta=0.5):

    alpha = 1.0
    for _ in range(max_iterations):
        if rosenbrock((x - alpha * gradient)) < rosenbrock(x) - beta * alpha * np.dot(gradient, gradient):
            break
        alpha *= beta

    return alpha


x0 = np.array([-1, 1])
# x0 = np.array([0, 1])
# x0 = np.array([2, 1])

result, path = steepest_descent(x0)  

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