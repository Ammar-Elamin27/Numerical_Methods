def integrate_points(x, y):
    if len(x) != len(y):
        print("Error: x and y must have the same length.")
        return None
    
    if len(x) < 2:
        print("Error: At least two points are required.")
        return None
    
    total_area = 0.0
    for i in range(len(x) - 1):
        dx = x[i+1] - x[i]
        avg_height = (y[i] + y[i+1]) / 2
        slice_area = avg_height * dx
        total_area += slice_area
    
    return total_area

# Add the following

x = [0, 1, 2, 3, 4]       # x values given
y = [0, 2, 4, 6, 8]       # Y values given


area = integrate_points(x, y)   # Call the function


print(f"Estimated area under the curve: {area}")
