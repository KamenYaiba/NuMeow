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


