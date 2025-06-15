import numpy as np

# Paste your function here
def lagrange_interpolate(x, y, degree, x0):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    x0_arr = np.asarray(x0, dtype=float)
    n = x.size

    if y.size != n:
        raise ValueError("x and y must have the same length")
    
    if degree < 0 or degree > n - 1:
        raise ValueError(f"degree must be between 0 and {n-1}")
    
    if n < degree + 1:
        raise ValueError("Not enough points for the requested degree")

    # Use only the first degree+1 points
    x_sub = x[:degree+1]
    y_sub = y[:degree+1]

    x0_vec = np.atleast_1d(x0_arr)
    y0_vec = np.zeros_like(x0_vec, dtype=float)

    for i in range(degree + 1):
        Li = np.ones_like(x0_vec, dtype=float)
        for j in range(degree + 1):
            if j != i:
                Li *= (x0_vec - x_sub[j]) / (x_sub[i] - x_sub[j])
        y0_vec += y_sub[i] * Li

    if y0_vec.size == 1:
        return float(y0_vec[0])
    
    return y0_vec
# Change these values:

x = [0, 1, 2, 3]           #  x-values
y = [1, 2, 0, 5]           #  y-values
degree = 2                 # use 3 points and add one to the degree
x0 = 1.5                   # x-value to estimate


y0 = lagrange_interpolate(x, y, degree, x0)


print(f"Estimated y at x = {x0} is y = {y0}")
