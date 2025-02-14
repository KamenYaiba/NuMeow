from src.interpolation import nevilles_method

n_tests = 1
tests = []

test = nevilles_method([8.1, 8.3, 8.6], [16.94410, 17.56492, 18.50515], 8.4) == 17.87713
tests.append(test)

for i in range(n_tests):
    if tests[i]:
        print(f'Test {i+1}: Passed ✔')
    else:
        print(f'Test {i+1}: Failed ❌')