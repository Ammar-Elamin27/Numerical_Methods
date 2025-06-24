import matplotlib.pyplot as plt
 


def linear_regression(x, y):
    if len(x) != len(y):
        raise ValueError("Lists x and y must be of the same length")

    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    # Calculate slope (m) and intercept (b) using the least squares formula
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = sum((xi - mean_x) ** 2 for xi in x)

    if denominator == 0:
        raise ValueError("Cannot perform linear regression: all x values are identical.")

    m = numerator / denominator
    b = mean_y - m * mean_x

    return m, b

# EXAMPLE ON HOW TO USE IT

x = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
y = [2, 3, 3, 5, 5, 4, 4, 6, 5, 6]


slope, intercept = linear_regression(x, y)
print(f"y = {slope:.2f}x + {intercept:.2f}")

# Plot data points and regression line
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Data Points')

# Generate predicted y values for the line
x_line = sorted(set(x))  # unique x values for line
y_line = [slope * xi + intercept for xi in x_line]

plt.plot(x_line, y_line, color='red', label='Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.legend()
plt.grid(True)
plt.show()
