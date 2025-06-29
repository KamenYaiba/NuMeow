from config import precision, max_itr
from helping_functions import parse_func


#TODO: newtons_method()
#TODO: secant_method()
#TODO: newtons_method_steps()
#TODO: secant_method_steps()


def bisection_method(func, a, b, pr = precision, iterations = max_itr):
    if iterations > max_itr or iterations < 0:
        iterations = max_itr

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



def bisection_method_steps(func, a, b, pr = precision, iterations = max_itr):
    if iterations > max_itr or iterations < 0:
        iterations = max_itr

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
        


def fixed_point_iteration(func, p, pr = precision, iterations = max_itr):
    if iterations > 10000 or iterations < 0:
        iterations = 10000

    i = 0
    points_history = []
    while i < iterations and abs(func(p) - p) > pr:
        points_history.append(p)
        if i > 9:
            points_history.pop(0)
            avg = sum(points_history) / 10
            if min(avg, p) / max(avg, p) < 0.25:
                return False

        p = func(p)
        i += 1

    return p




def fixed_point_iteration_steps(func, p, pr = precision, iterations = max_itr):
    if iterations > max_itr or iterations < 0:
        iterations = max_itr

    i = 0
    points_history = []
    steps = []
    while i < iterations and abs(func(p) - p) > pr:
        points_history.append(p)
        steps.append(p)
        if i > 9:
            points_history.pop(0)
            avg = sum(points_history) / 10
            if min(avg, p) / max(avg, p) < 0.25:
                return False

        p = func(p)
        i += 1

    return p, steps



