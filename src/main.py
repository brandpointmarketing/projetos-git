import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

def integrate_two_variables(func, x_start, x_end, y_start, y_end):
  """
  Calculates the double integral of a function of two variables using scipy.integrate.dblquad.

  Args:
    func: A function that takes two arguments (x, y) and returns a scalar value.
    x_start: The starting value for the x-integration.
    x_end: The ending value for the x-integration.
    y_start: The starting value for the y-integration.
    y_end: The ending value for the y-integration.

  Returns:
    The result of the double integral.
  """
  result, _ = scipy.integrate.dblquad(func, x_start, x_end, y_start, y_end)
  return result

def plot_integral(func, x_start, x_end, y_start, y_end, x_range, y_range):
  """
  Plots the result of the double integral.

  Args:
    func: A function that takes two arguments (x, y) and returns a scalar value.
    x_start: The starting value for the x-integration.
    x_end: The ending value for the x-integration.
    y_start: The starting value for the y-integration.
    y_end: The ending value for the y-integration.
    x_range: A tuple (x_min, x_max) defining the range for the x-axis.
    y_range: A tuple (y_min, y_max) defining the range for the y-axis.
  """
  x = np.linspace(x_range[0], x_range[1], 100)
  y = np.linspace(y_range[0], y_range[1], 100)
  X, Y = np.meshgrid(x, y)
  Z = func(X, Y)
  plt.imshow(Z, extent=(x_range[0], x_range[1], y_range[0], y_range[1]), origin='lower', cmap='viridis')
  plt.colorbar()
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Plot of the Double Integral")
  plt.show()


if __name__ == '__main__':
  def my_func(x, y):
    return x + y

  x_start = 0
  x_end = 1
  y_start = 0
  y_end = 1

  integral_result = integrate_two_variables(my_func, x_start, x_end, y_start, y_end)
  print(f"The integral is: {integral_result}")

  plot_integral(my_func, x_start, x_end, y_start, y_end, (0, 1), (0, 1))