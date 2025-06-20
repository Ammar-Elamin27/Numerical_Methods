ef f(x):
    return 100/(x**2 +1)-5 #change

def bisection_method(a, b, tolerance):
    
    if f(a) * f(b) >= 0:
        print("Invalid interval: No sign change")
        return None

    while (b - a) / 2 > tolerance:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

# Example use:
root = bisection_method(0, 3.5, 0.001) #CHanged to adapt the code to the given function
print("Root found at:", root)
