from src.interpolation import nevilles_method

tests = []

test = nevilles_method([8.1, 8.3, 8.6], [16.94410, 17.56492, 18.50515], 8.4) == 17.87713
tests.append(test)
test = nevilles_method([8.1, 8.3], [16.94410, 17.56492, 18.50515], 8.4) is False
tests.append(test)
test = nevilles_method([8.1, 8.3, 8.6], [], 8.4) is False
tests.append(test)

for i in range(len(tests)):
    if tests[i]:
        print(f'Test {i+1}: Passed ✔')
    else:
        print(f'Test {i+1}: Failed ❌')