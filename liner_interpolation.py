def linear_interpolate(x, y, x0):
    
    # Basic input checks
    if len(x) != len(y):
        print("Error: x and y must have the same number of points.")
        return None
    
    if len(x) < 2:
        print("Error: At least two points are required for interpolation.")
        return None
    
    # Check bounds
    if x0 < x[0] or x0 > x[-1]:
        print("Error: x0 is outside the range of x.")
        return None

    # Find the interval [x[i], x[i+1]] that contains x0
    for i in range(len(x) - 1):
        x_left = x[i]
        x_right = x[i+1]
        if x0 >= x_left and x0 <= x_right:
            y_left = y[i]
            y_right = y[i+1]
            
            # Compute fraction along the interval
            t = (x0 - x_left) / (x_right - x_left)
            
            # Linear interpolation formula
            y0 = y_left + t * (y_right - y_left)
            
            return y0

    # Should never reach here if x0 is in bounds
    return None

# --------------------------------------
#  YOU MODIFY THESE LINES BELOW 

#Your known x and y values:
x = [1, 2, 3, 4]        #  Change these if you have different x-values
y = [2, 4, 6, 8]        #  Change these to match your y-values

#The x0 value where you want to interpolate:
x0 = 2.5                # Change this to any value in the x-range

# Call the function:
y0 = linear_interpolate(x, y, x0)

#Show the result:
print("Interpolated y0 =", y0)
