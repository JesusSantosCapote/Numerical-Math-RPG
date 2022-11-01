import math


def bisection(fun, x_a, x_b, eps=None, steps=10):
    if fun(x_a) * fun(x_b) >= 0:
        print("The bisection method cannot be applied")
        return None
    
    # Calculate number of stepds base on eps
    if eps is not None:
        steps = math.ceil(math.log((x_b - x_a) / eps) / math.log(2))
    
    # The bisection method
    for n in range(steps + 1):
        x_m = (x_a + x_b) / 2
        
        if f(x_m) == 0:
            return x_m
        
        if f(x_a) * f(x_m) < 0:
            x_b = x_m
        else:
            x_a = x_m
    
    return (x_a + x_b) / 2