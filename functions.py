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


def secant(fun, x_a, x_b, steps=50):
    # El método de la secante no se puede aplicar
    if fun(x_a) * fun(x_b) >= 0:
        print('El método de la secante no se puede aplicar')
        return None

    # El método de la secante
    for n in range(steps + 1):
        # Cálculo de la secante
        x_n = x_a - fun(x_a) * (x_b - x_a) / (fun(x_b) - fun(x_a))

        if fun(x_n) == 0:
            return x_n

        if fun(x_a) * fun(x_n) < 0:
            x_b = x_n
        else:
            x_a = x_n
    return x_n


def regulaFalsi( a , b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1
     
    c = a # Initialize result
     
    for i in range(MAX_ITER):
         
        # Find the point that touches x axis
        c = (a * func(b) - b * func(a))/ (func(b) - func(a))
         
        # Check if the above found point is root
        if func(c) == 0:
            break
         
        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print("The value of root is : " , '%.4f' %c)


def puntofijo(gx,a,tolera, iteramax = 15):
    i = 1 # iteración
    b = gx(a)
    tramo = abs(b-a)
    while(tramo>=tolera and i<=iteramax ):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i + 1
    respuesta = b
    
    # Validar respuesta
    if (i>=iteramax ):
        respuesta = np.nan
    return(respuesta)
    