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


def nevilles_method_steps(x, y, xS):  # uses more space/might be slower?
    if len(x) != len(y):
        return False

    columns = len(x) -1
    diff = 1
    result = y[:]
    result_pointer = columns

    for i in range(columns):
        k = columns - i
        for j in range(k):
            result.append((result[result_pointer - k + 1] * (xS - x[j]) - result[result_pointer - k] * (xS - x[j+diff])) / (x[j+diff] - x[j]))
            result_pointer += 1
        diff += 1

    return result


#TODO: lagrange_polynomial()
#TODO: divided_differences()
#TODO: hermites_method()
#TODO: lagrange_polynomial_steps()
#TODO: divided_differences_steps()
#TODO: hermites_method_steps()

