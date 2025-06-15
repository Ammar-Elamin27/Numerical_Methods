import numpy as np

def polynomial_interpolate(x, y, degree, x0):
    coeffs = np.polyfit(x, y, degree)
    y0 = np.polyval(coeffs, x0)
    return y0

# Add the Following

x = [1, 2, 3, 4]           # x-values given
y = [1, 4, 9, 16]          # y-values given 
degree = 2                 # degree 
x0 = 2.5                   # the x-value you want to estimate y for


y0 = polynomial_interpolate(x, y, degree, x0)     # Calling the function


print(f"Interpolated value at x0 = {x0} is y0 = {y0}")
