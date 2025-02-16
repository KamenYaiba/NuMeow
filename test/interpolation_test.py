from src.interpolation import nevilles_method, nevilles_method_steps

tests = []

test = nevilles_method([8.1, 8.3, 8.6], [16.94410, 17.56492, 18.50515], 8.4) == 17.87713
tests.append(test)
test = nevilles_method([8.1, 8.3], [16.94410, 17.56492, 18.50515], 8.4) is False
tests.append(test)
test = nevilles_method([8.1, 8.3, 8.6], [], 8.4) is False
tests.append(test)
test = nevilles_method([0, 0.25, 0.5, 0.75], [1, 1.64872, 2.71828, 4.48169], 0.43) == 2.36060473408
tests.append(test)

test = nevilles_method_steps([0, 0.25, 0.5, 0.75], [1, 1.64872, 2.71828, 4.48169], 0.43) == [1, 1.64872, 2.71828, 4.48169, 2.1157984, 2.4188032, 2.2245251999999995, 2.3763825279999997, 2.34886312, 2.36060473408]
tests.append(test)
test = nevilles_method_steps([], [1, 1.64872, 2.71828, 4.48169], 0.43) is False
tests.append(test)
test = nevilles_method_steps([0, 0.25, 0.5, 0.75], [1, 1.64872, 2.71828], 0.43) is False
tests.append(test)
test = nevilles_method_steps([8.1, 8.3, 8.6], [16.94410, 17.56492, 18.50515], 8.4) == [16.9441, 17.56492, 18.50515, 17.875329999999998, 17.878330000000002, 17.87713]
tests.append(test)


for i in range(len(tests)):
    if tests[i]:
        print(f'Test {i+1}: Passed ✔')
    else:
        print(f'Test {i+1}: Failed ❌')