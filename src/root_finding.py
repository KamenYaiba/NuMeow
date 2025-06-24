from config import precision
from helping_functions import parse_func


#TODO: newtons_method()
#TODO: secant_method()
#TODO: fixed_point_iteration()
#TODO: bisection_method()
#TODO: newtons_method_steps()
#TODO: secant_method_steps()
#TODO: fixed_point_iteration_steps()
#TODO: bisection_method_steps()


def bisection_method(func, a, b, pr = precision, iterations = 10000):
    if iterations > 10000:
        iteratioin = 10000

    if func(a) * func(b) > 0:
        return False
    
    if(a > b):
        a, b = b, a
    
    a_neg = False
    if func(a) < 0:
        a_neg = True

    mp = (b + a) / 2 #mid point
    i = 0
    while i < iterations and abs(func(mp) - 0) > pr:
        i = i+1
        if func(mp) < 0:
            if a_neg:
                a = mp
            else:
                b = mp
        else:
            if a_neg:
                b = mp
            else:
                a = mp
        
        mp = (a + b) / 2

    return mp



def bisection_method_steps(func, a, b, pr = precision, iterations = 10000):
    if iterations > 10000:
        iteratioin = 10000

    if func(a) * func(b) > 0:
        return False
    
    if(a > b):
        a, b = b, a
    
    a_neg = False
    if func(a) < 0:
        a_neg = True

    
    points = []
    mp = (b + a) / 2 #mid point
    i = 0
    while i < iterations and abs(func(mp) - 0) > pr:
        i = i+1
        points.append(mp)

        if func(mp) < 0:
            if a_neg:
                a = mp
            else:
                b = mp
        else:
            if a_neg:
                b = mp
            else:
                a = mp
        
        mp = (a + b) / 2

    return mp, points
        


func = parse_func("x^4 - 2*x^3 - 4*x^2 + 4*x + 4")
ans, ps = bisection_method_steps(func, -2, -1)
print(ps)
print(len(ps))
