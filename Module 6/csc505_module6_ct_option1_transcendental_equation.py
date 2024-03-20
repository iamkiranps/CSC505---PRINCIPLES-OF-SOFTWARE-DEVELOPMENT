"""
  Kiran Ponappan Sreekumari 
  CSC505 – Principles of Software Development 
  Colorado State University - Global
  Dr. Pubali Banerjee 
  March 20, 2024
  Module 6: Critical Thinking - Stepwise Refinement Approach
  Apply a “stepwise refinement approach” to iteratively solve for the roots of a transcendental equation.
 """
import math
from matplotlib import pyplot as plt
import numpy as np
import random

def f(x):
    # Define the transcendental equation
    return x - math.sin(x) - 0.5

def df(x):
    # Define the derivative of the equation
    return 1 - math.cos(x)

def newton_raphson(x0, max_iter, tol):
    # Step 1: Initialize variables
    iter_count = 0
    x = x0
    
    # Step 2: Iterate until convergence or maximum iterations reached
    while iter_count < max_iter:
        # Step 3: Compute the function value and its derivative
        fx = f(x)
        dfx = df(x)
        
        # Step 4: Update the root approximation using Newton-Raphson method
        x_new = x - fx / dfx
        
        # Step 5: Check for convergence
        if abs(x_new - x) < tol:
            return x_new, iter_count + 1  # Return the root and number of iterations
        
        # Step 6: Update variables for the next iteration
        x = x_new
        iter_count += 1
    
    # Step 7: Return None if maximum iterations reached without convergence
    return None, iter_count

def bisection(func, a, b, tol=1e-6, max_iter=100):
    # Ensure that the function has opposite signs at the interval endpoints
    assert func(a) * func(b) < 0, "Function must have opposite signs at interval endpoints"

    # Initialize variables
    iteration = 0

    # Perform bisection iterations
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            return c  # c is exactly the root
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    return (a + b) / 2, iteration

# Step 8: Call the Newton-Raphson method with initial guess, tolerance, and maximum iterations
n_root, n_iterations = newton_raphson(1.0, 100, 1e-8)
b_root, b_iterations = bisection(f, 1.0,2.0, tol=1e-6, max_iter=100)

# Step 9: Display the result
if n_root is not None:
    print("Newton-Raphson method - Root found:", n_root)
    print("Newton-Raphson method - Iterations:", n_iterations)
else:
    print("Root not found within maximum iterations")

# Step 9: Display the result
if b_root is not None:
    print("Bisection Method - Root found:", b_root)
    print("Bisection Method - Iterations:", b_iterations)
else:
    print("Root not found within maximum iterations")

#plot
x = np.arange(0,2,0.01)
y = [f(i) for i in x]
plt.title('Transcendental Equation [f(x) = x - sin(x) - 0.5]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x, y, color='green')
plt.scatter(n_root, 0, c='red')
plt.text(n_root,0,f"Newton \n({n_root},0)") 
plt.scatter(b_root, 0, c='blue')
plt.text(b_root,0,f"Bisection \n({b_root},0)", horizontalalignment='right',verticalalignment='top') 
plt.show()