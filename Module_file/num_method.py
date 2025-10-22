import sympy as sp
import numpy as np
import math

class numerical_methods():
    def bisection(f,a, b, maxiter=100, tol=1e-6):
       for i in range(maxiter):
        mid = (a + b) / 2
        fa, fb, fmid = f(a), f(b), f(mid)
             
        if abs(fmid) < tol:
            return mid
        if fa * fmid < 0:
             b = mid
        else:
            a = mid
        return mid

    def false_position(f,a, b, maxiter=100, tol=1e-6):
        for i in range(maxiter):
            fa, fb = f(a), f(b)
            c = (a * fb - b * fa) / (fb - fa)
            fc = f(c)
           
            if abs(fc) < tol:
              return c
            if fa * fc < 0:
              b = c
            else:
              a = c
        return c



    def newton_raphson(f, x0, maxiter=100, tol=1e-6):
       for _ in range(maxiter):
          f_val = f(x0)
          f_prime = (f(x0 + 1e-6) - f(x0 - 1e-6)) / (2 * 1e-6)  # numerical derivative
          if abs(f_prime) < 1e-12:
             raise ZeroDivisionError("Derivative too small")
          x1 = x0 - f_val / f_prime
          if abs(x1 - x0) < tol:
            return x1
          x0 = x1
       raise ValueError("Did not converge")

  

    def trapezoidal_rule(f,a, b, n=100):
        h = (b - a) / n
        result = 0.5 * (f(a) + f(b))
       
        running_sum = result
        for i in range(1, n):
            xi = a + i * h
            fx = f(xi)
            running_sum += fx
            
        integral = running_sum * h
        return integral

    def simpsons_rule(f,a, b, n):
        if n % 2 != 0:
            raise ValueError("Simpson's Rule requires even number of intervals.")
        h = (b - a) / n
        result = f(a) + f(b)
        
        for i in range(1, n):
            xi = a + i * h
            fx = f(xi)
            coeff = 4 if i % 2 == 1 else 2
            result += coeff * fx
        
       
        integral = result * h / 3
        return integral

    
