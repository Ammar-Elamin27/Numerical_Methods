import math



def f(x):
    # Define your function here. Example:
    return math.sqrt(1+x**2)

def integrate():
    a = float(input("Enter lower limit a: "))
    b = float(input("Enter upper limit b: "))
    h = float(input("Enter step size h: "))
    
    # Compute how many full subintervals fit
    n = int((b - a) / h)
    
    # Left Riemann sum
    left_sum = sum(f(a + i*h) for i in range(n)) * h
    # Right Riemann sum
    right_sum = sum(f(a + i*h) for i in range(1, n+1)) * h
    
    # Determine over- and underestimations
    over = max(left_sum, right_sum)
    under = min(left_sum, right_sum)
    avg = (over + under) / 2  # Trapezoidal approximation

    print(f"Overestimation:   {over}")
    print(f"Underestimation:  {under}")
    print(f"Average (trap.):  {avg}")


#Call this then input the minimum, highest, and gap(IDEALLY) 0.001
integrate()
