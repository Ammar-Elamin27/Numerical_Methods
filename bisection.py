# BISECTION METHOD FOR ROOT FINDING


def f(x):
    return x**3 - x - 2 #Chnage this line to make it to your intened equation to solve

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
root = bisection_method(1, 2, 0.001) # Change this to make it to the interval you plan to code in
print("Root found at:", root)
