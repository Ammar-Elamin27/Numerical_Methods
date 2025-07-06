import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# -----------------------------
#  1. Input your x and y data
# -----------------------------
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)  # You modify here
y = np.array([70, 75, 83, 92, 105, 118, 130, 135, 137, 138]) # You modify here

# -----------------------------
#  2. Choose the polynomial degree
# -----------------------------
poly = PolynomialFeatures(degree=2)  # You modify here (try degree=3 or 4 if needed)
x_poly = poly.fit_transform(x)

# -----------------------------
#  3. Train the model
# -----------------------------
model = LinearRegression()
model.fit(x_poly, y)

# -----------------------------
#  4. Predict for a new x value
# -----------------------------
x_value = np.array([[6.5]])  # You modify here (change 6.5 to any x value)
x_value_poly = poly.transform(x_value)
y_pred = model.predict(x_value_poly)

print(f"Predicted y at x = {x_value[0][0]}: {y_pred[0]:.2f}")

# -----------------------------
#  5. Plotting
# -----------------------------
x_range = np.linspace(min(x), max(x), 100).reshape(-1, 1)
x_range_poly = poly.transform(x_range)
y_range_pred = model.predict(x_range_poly)

plt.scatter(x, y, color='red', label='Actual Data')
plt.plot(x_range, y_range_pred, color='blue', label='Polynomial Fit')
plt.xlabel('x')  # You modify here (e.g., 'Time (min)')
plt.ylabel('y')  # You modify here (e.g., 'Heart Rate (bpm)')
plt.title('Polynomial Regression')  # You modify here
plt.legend()
plt.grid(True)
plt.show()
