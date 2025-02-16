def nevilles_method(x, y, xS):
    if len(x) != len(y):
        return False

    columns = len(x) -1
    diff = 1

    for i in range(columns):
        for j in range(columns - i):
            y[j] = (y[j+1] * (xS - x[j]) - y[j] * (xS - x[j+diff])) / (x[j+diff] - x[j])
        diff += 1

    return y[0]


#TODO: lagrange_polynomial()
#TODO: divided_differences()
#TODO: hermites_method()
#TODO: nevilles_method_steps()
#TODO: lagrange_polynomial_steps()
#TODO: divided_differences_steps()
#TODO: hermites_method_steps()

