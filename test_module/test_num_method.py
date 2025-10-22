import math
from num_method import numerical_methods
def test_bisection():
   f= lambda x: x**2 -4
   root = numerical_methods.bisection(f,1,3)
   assert abs(root-2)<1e-6


   
def test_false_position():
   f= lambda x: x**2 -4
   root = numerical_methods.false_position(f,1,3)
   assert abs(root-2)<1e-6   
   
   
   
def test_newton_raphson():
   f= lambda x: x**2 -4
   root = numerical_methods.newton_raphson(f,x0=1,maxiter=100)
   assert abs(root-2)<1e-6    
   
   
      
def test_trapezoidal_rule():
   f= lambda x: math.sin(x)
   root = numerical_methods.trapezoidal_rule(f,a=0,b=math.pi,n=1000)
   assert abs(root-2)<1e-4
   
   
   
         
def test_simpsons_rule():
   f= lambda x:math.sin(x)
   root = numerical_methods.simpsons_rule(f,a=0,b=math.pi,n=1000)
   assert abs(root-2)<1e-6  
