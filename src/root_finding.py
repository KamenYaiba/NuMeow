from config import precision
from helping_functions import parse_func


#TODO: newtons_method()
#TODO: secant_method()
#TODO: newtons_method_steps()
#TODO: secant_method_steps()
#TODO: fixed_point_iteration_steps()


def bisection_method(func, a, b, pr = precision, iterations = 10000):
    if iterations > 10000 or iterations < 0:
        iterations = 10000

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
    if iterations > 10000 or iterations < 0:
        iterations = 10000

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
        


def fixed_point_iteration(func, point, pr = precision, iterations = 10000):
    if iterations > 10000 or iterations < 0:
        iterations = 10000

    i = 0
    points_history = []
    while i < iterations and abs(func(point) - point) > pr:
        points_history.append(point)
        if i > 9:
            points_history.pop(0)
            avg = sum(points_history) / 10
            if min(avg, point) / max(avg, point) < 0.25:
                return False

        point = func(point)
        i += 1

    return point




def fixed_point_iteration_steps(func, point, pr = precision, iterations = 10000):
    if iterations > 10000 or iterations < 0:
        iterations = 10000

    i = 0
    points_history = []
    steps = []
    while i < iterations and abs(func(point) - point) > pr:
        points_history.append(point)
        steps.append(point)
        if i > 9:
            points_history.pop(0)
            avg = sum(points_history) / 10
            if min(avg, point) / max(avg, point) < 0.25:
                return False

        point = func(point)
        i += 1

    return point, steps






 