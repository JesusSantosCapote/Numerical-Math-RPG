import math
from scipy import misc
import numpy as np

def bisection(fun, eps, steps): #Para el warrior
    x_a = float(input("Enter the first extreme of the interval\n"))
    x_b = float(input("Enter the second extreme of the interval\n"))
    if fun(x_a) * fun(x_b) >= 0:
        print("The bisection method cannot be applied")
        return "Zero not found", steps
    
    steps_calculated = math.ceil(math.log((x_b - x_a) / eps) / math.log(2))
    if steps_calculated >= steps:
        return "Zero not founded" , steps
    # The bisection method
    for n in range(steps + 1):
        x_m = (x_a + x_b) / 2
        
        if fun(x_m) == 0:
            return x_m, n
        
        if fun(x_a) * fun(x_m) < 0:
            x_b = x_m
        else:
            x_a = x_m
    
    return (x_a + x_b) / 2 , steps


def newton(fun, eps, steps):   #Este esta bueno para el Rogue porque es rapido
    x_n = float(input("Enter the starting point\n"))
    for i in range(steps + 1):
        # Evaluación de la función para ver si el resultado es válido
        f_x = fun(x_n)
        if abs(f_x) < eps:
            return x_n, i
        
        d_f = misc.derivative(fun,x_n)
        if d_f == 0:
            return "Zero not Found, some derivative was equal to zero", steps
        
        # Estimación del siguiente punto
        x_n = x_n - f_x / d_f
    
    return "Zero not Found", steps


def secant(fun, eps, steps):
    x_a = float(input("Enter the first extreme of the interval\n"))
    x_b = float(input("Enter the second extreme of the interval\n"))

    # El método de la secante no se puede aplicar
    if fun(x_a) * fun(x_b) >= 0:
        print("The secant method cannot be applied.")
        return "Zero not Found", steps

    # El método de la secante
    for n in range(steps + 1):
        # Cálculo de la secante
        x_n = x_a - fun(x_a) * (x_b - x_a) / (fun(x_b) - fun(x_a))

        if fun(x_n) < eps:
            return x_n, n

        if fun(x_a) * fun(x_n) < 0:
            x_b = x_n
        else:
            x_a = x_n

    return "Zero not Found", steps


def regulaFalsi( fun, eps, steps):

    x_a = float(input("Enter the first extreme of the interval\n"))
    x_b = float(input("Enter the second extreme of the interval\n"))
    if fun(x_a) * fun(x_b) >= 0:
        print("The regula-falsi method cannot be applied")
        return "Zero not found", steps
     
     
    for i in range(steps + 1):
         
        # Find the point that touches x axis
        x_c = (x_a * fun(x_b) - x_b * fun(x_a))/ (fun(x_b) - fun(x_a))
         
        # Check if the above found point is root
        if fun(x_c) <= eps:
            return x_c, i
         
        # Decide the side to repeat the steps
        elif fun(x_c) * fun(x_a) < 0:
            x_b = x_c
        else:
            x_a = x_c
    return "Zero not found", steps

def regulaFalsiHamming (fun, eps, steps):
    x_a = float(input("Enter the first extreme of the interval\n"))
    x_b = float(input("Enter the second extreme of the interval\n"))
    if fun(x_a) * fun(x_b) >= 0:
        print("The regula falsi hamming method cannot be applied")
        return "Zero not found", steps

     
    for i in range(steps + 1):
        
        x_m = (x_a +x_b)/2
        if fun(x_m) < (fun(x_a) + fun(x_b)) / 2:
            x_c = (x_a * fun(x_b)/2 - x_b * fun(x_a))/ fun(x_b)/2 - fun(x_a)
        else:
            x_c = (x_a * fun(x_b) - x_b * fun(x_a)/2)/ fun(x_b) - fun(x_a)/2

        # Check if the above found point is root
        if fun(x_c) <= eps:
            return x_c, i
         
        # Decide the side to repeat the steps
        elif fun(x_c) * fun(x_a) < 0:
            x_b = x_c
        else:
            x_a = x_c
    return "Zero not found", steps


def steffensen_algorithm(f, eps, steps):
    while True:
        x_n = float(input("Enter the starting point\n"))
        if x_n == 0.0:
            print("Initial value cannot be zero")
        else:
            break
    
    if abs(f(x_n)) < eps:
        # found!
        return x_n, 0

    for i in range(steps + 1):
        g = (f(x_n + f(x_n))) / f(x_n) - 1
        try:
            x_n -= (f(x_n)) / (g * x_n)
        except ZeroDivisionError:
            return "Zero not found. Some division by zero was founded", steps
        if abs(f(x_n)) < eps:
            # found!
            return x_n, i
    
    return "Zero not found", steps