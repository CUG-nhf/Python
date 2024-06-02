import numpy as np
import matplotlib.pyplot as plt

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

# LLorenz system
def lorenz_system(state, t):
	x, y, z = state
	dxdt = sigma * (y - x)
	dydt = x * (rho - z) - y
	dzdt = x * y - beta * z
	return np.array([dxdt, dydt, dzdt])

# the classical fourth-order Runge-Kutta method
def runge_kutta_4(f, y0, t):
	n = len(t)
	y = np.zeros((n, len(y0)))
	y[0] = y0
	for i in range(1, n):
		h = t[i] - t[i-1]
		k1 = f(y[i-1], t[i-1])
		k2 = f(y[i-1] + 0.5*h*k1, t[i-1] + 0.5*h)
		k3 = f(y[i-1] + 0.5*h*k2, t[i-1] + 0.5*h)
		k4 = f(y[i-1] + h*k3, t[i-1] + h)
		y[i] = y[i-1] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
	return y

t = np.arange(0, 100, 0.01)
initial_state_a = [0.1, 0.1, 0.0]
initial_state_b = [0.1, 0.100001, 0.0]

# solve
solution_a = runge_kutta_4(lorenz_system, initial_state_a, t)
solution_b = runge_kutta_4(lorenz_system, initial_state_b, t)

# plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(solution_a[:, 0], solution_a[:, 1], solution_a[:, 2], label='x0=0.1, y0=0.1, z0=0.0', linewidth=0.3)
# # ax.plot(solution_b[:, 0], solution_b[:, 1], solution_b[:, 2], label='x0=0.1, y0=0.100001, z0=0.0', linewidth=0.3)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# # ax.set_box_aspect([1, 1, 0.6])
# ax.legend()
# plt.show()


# Plot the trajectory 𝑥(𝑡) against 𝑡 for 95 ≤ 𝑡 ≤ 100 obtained from (a) and (b)
plt.figure()
plt.plot(t[9500:], solution_a[9500:, 0], 'b', label='[x0=0.1, y0=0.1, z0=0.0]')
plt.plot(t[9500:], solution_b[9500:, 0], 'r', label='[x0=0.1, y0=0.100001, z0=0.0]')
plt.xlabel('Time')
plt.ylabel('x(t)')
plt.legend()
plt.show()