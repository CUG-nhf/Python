import numpy as np
import matplotlib.pyplot as plt

# Define Runge function
def runge_func(x):
    return 1 / (1 + 25 * x**2)


def draw_fig_7_7():
	for i in [5, 10]:
		n = i + 1
  
		# equally spaced points
		x_interp = np.linspace(-1, 1, n)
		y_interp = runge_func(x_interp)
		coeffs = np.polyfit(x_interp, y_interp, 10)

		# Plot curves
		x_plot = np.linspace(-1, 1, 100)
		plt.plot(x_plot, np.polyval(coeffs, x_plot), label=f'p{i}(t)', linestyle='--')

	plt.plot(x_plot, runge_func(x_plot), label='Runge Function', linestyle='-')
	plt.legend()
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('equally spaced points')
	plt.grid(True)
	plt.show()


def draw_fig_7_8():
	for i in [5, 10]:
		n = i + 1
		
		# Chebyshev points
		x_interp = np.cos((2*np.arange(n) + 1) * np.pi / (2*n))
		y_interp = runge_func(x_interp)
		coeffs = np.polyfit(x_interp, y_interp, 10)

		# Plot curves
		x_plot = np.linspace(-1, 1, 100)
		plt.plot(x_plot, np.polyval(coeffs, x_plot), label=f'p{i}(t)', linestyle='--')

	plt.plot(x_plot, runge_func(x_plot), label='Runge Function', linestyle='-')
	plt.legend()
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Chebyshev points')
	plt.grid(True)
	plt.show()

	
draw_fig_7_7()