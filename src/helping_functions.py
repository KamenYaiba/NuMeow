import itertools
import math
from sympy import sympify, lambdify, E
from config import x


def elementary_symmetric_sum(input_list):
    degree = len(input_list)
    result_list = []
    for i in range(degree+1):
        result_list.append(sum_product_length_n_combinations(input_list, i))
    return result_list


#let array = [1, 2, 3, 4]
#product_length_n_combinations(array, 1) should return 1 + 2 + 3 + 4
#product_length_n_combinations(array, 2) should return 1x2 + 1x3 + 1x4 + 2x3 + 2x4 + 3x4
#product_length_n_combinations(array, 3) should return 1x2x3 + 1x2x4 + 1x3x4 +2x3x4
#product_length_n_combinations(array, 4) should return 1x2x3x4
def sum_product_length_n_combinations(array, n):
    if n == 0:
        return 1
    if n == 1:
        return sum(array)
    if len(array) == n:
        return math.prod(array)

    #no im not using the one-liner "pythonic way"
    combinations = itertools.combinations(array, n)
    res_sum = 0
    for c in combinations:
        res_sum += math.prod(c)

    return res_sum


# use with try
def parse_func(func_str):
    func = sympify(func_str, locals={'e': E})
    return lambdify(x, func)





