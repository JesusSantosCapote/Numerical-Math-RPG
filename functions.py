import math
from scipy import misc

def bisection(fun, eps, steps): #Para el warrior
    x_a = float(input("Enter the first extreme of the interval"))
    x_b = float(input("Enter the second extreme of the interval"))
    if fun(x_a) * fun(x_b) >= 0:
        print("The bisection method cannot be applied")
        return None
    
    steps_calculated = math.ceil(math.log((x_b - x_a) / eps) / math.log(2))
    if steps_calculated >= steps:
        return "Zero not founded" , steps
    # The bisection method
    for n in range(steps + 1):
        x_m = (x_a + x_b) / 2
        
        if fun(x_m) == 0:
            return x_m
        
        if fun(x_a) * fun(x_m) < 0:
            x_b = x_m
        else:
            x_a = x_m
    
    return (x_a + x_b) / 2 , steps


def newton(fun, eps, steps):   #Este esta bueno para el Rogue porque es rapido
    x_n = float(input("Enter the starting point"))
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