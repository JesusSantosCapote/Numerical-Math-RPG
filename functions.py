import math
from scipy import misc

def bisection(fun, eps): #Para el warrior
    x_a = input("Enter the first extreme of the interval")
    x_b = input("Enter the second extreme of the interval")
    if fun(x_a) * fun(x_b) >= 0:
        print("The bisection method cannot be applied")
        return None

    # Calculate number of stepds base on eps
    if eps is not None:
        steps = math.ceil(math.log((x_b - x_a) / eps) / math.log(2))
    
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


def newton(fun, der, x_n, epsilon=1e-6, steps=50):   #Este esta bueno para el Rogue porque es rapido
    for n in range(steps + 1):
        # Evaluación de la función para ver si el resultado es válido
        f_x = fun(x_n)
        if abs(f_x) < epsilon:
            return x_n
        
        # Evaluación de la derivada
        d_f = der(x_n)
        if d_f == 0:
            print('Error la derivada es cero')
            return None
        
        # Estimación del siguiente punto
        x_n = x_n - f_x / d_f
    
    print('Se ha alcanzado el límite de iteraciones')
    return None