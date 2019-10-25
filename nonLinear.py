#Ahmed Eamd
#section 1 
import sys
from sympy import *
import math
x = symbols('x')             
f_expr = x**3 + 4*x**2 - 10
dfdx_expr = diff(f_expr, x)  
f = lambdify([x],     
             f_expr)  
dfdx = lambdify([x], dfdx_expr)
print(dfdx(x))         

method = int(input('which method do you want to use? \n 1. newoten-raphson \n 2. bisection \n 3. secant \n'))

if method == 1:
    def Newton(f, dfdx, x, acc):
        f_value = f(x)
        iteration_counter = 0
        while abs(f_value) > acc and iteration_counter < 1000:
            try:
                x = x - float(f_value)/dfdx(x)
            except ZeroDivisionError:
                print("Error! - derivative zero for x = ", x)
                sys.exit(1)     

            f_value = f(x)
            iteration_counter += 1

    
        if abs(f_value) > acc:
            iteration_counter = -1
        return x, iteration_counter

    solution, no_iterations = Newton(f, dfdx, x=1000, acc=1.0e-6)

    if no_iterations > 0:    
        print("Number of function calls: %d" % (1 + 2*no_iterations))
        print("A solution is: %f" % (solution))
    else:
        print("Solution not found!")
elif method == 2:
    def bisection(f, x_L, x_R, acc, return_x_list=False):
        f_L = f(x_L)
        if f_L*f(x_R) > 0:
            print("root does not exist")
            sys.exit(1)
        x_M = float(x_L + x_R)/2.0
        f_M = f(x_M)
        iteration_counter = 1
        if return_x_list:
            x_list = []

        while abs(f_M) > acc:
            if f_L*f_M > 0:   
                x_L = x_M
                f_L = f_M
            else:
                x_R = x_M
            x_M = float(x_L + x_R)/2
            f_M = f(x_M)
            iteration_counter += 1
            if return_x_list:
                x_list.append(x_M)
        if return_x_list:
            return x_list, iteration_counter
        else:
            return x_M, iteration_counter
    a = 1
    b = 2
    solution, no_iterations = bisection(f, a, b, acc=1.0e-6)

    print("Number of function calls: %d" % (1 + 2*no_iterations))
    print("A solution is: %f" % (solution))
elif method == 3:
    def secant(f, x0, x1, acc):
        f_x0 = f(x0)
        f_x1 = f(x1)
        iteration_counter = 0
        while abs(f_x1) > acc and iteration_counter < 100:
            try:
                denominator = float(f_x1 - f_x0)/(x1 - x0)
                x = x1 - float(f_x1)/denominator
            except ZeroDivisionError:
                print("Error! - denominator zero for x = ", x)
                sys.exit(1)     
            x0 = x1
            x1 = x
            f_x0 = f_x1
            f_x1 = f(x1)
            iteration_counter += 1
        if abs(f_x1) > acc:
            iteration_counter = -1
        return x, iteration_counter
    x0 = 1000   
    x1 = x0 - 1
    solution, no_iterations = secant(f, x0, x1, acc=1.0e-6)
    if no_iterations > 0:    
        print("Number of function calls: %d" % (2 + no_iterations))
        print("A solution is: %f" % (solution))
    else:
        print("Solution not found!")
else:
    print('enter 1 , 2 or 3')
