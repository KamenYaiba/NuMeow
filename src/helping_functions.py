import itertools
import math


#NOT DONE
def elementary_symmetric_sum(input_list):
    degree = len(input_list)
    result_list = [1, sum(input_list)]

    temp_sum = 0
    iterations = degree - 2 #a list of length n prodeces n+1 constants, and 3 of these constants do not
                            #need iterations to calculate, therfore: n+1 - 3 = n-1
    for itr in range(iterations):
        for i in range(degree):
            for j in range(i+1, degree):
                temp_sum = temp_sum + (input_list[i] * input_list[j])

        result_list.append(temp_sum)

    result_list.append(math.prod(input_list))
    return result_list


#let array = [1, 2, 3, 4]
#product_length_n_groups(array, 1) should return 1 + 2 + 3 + 4
#product_length_n_groups(array, 2) should return 1x2 + 1x3 + 1x4 + 2x3 + 2x4 + 3x4
#product_length_n_groups(array, 3) should return 1x2x3 + 1x2x4 + 1x3x4 +2x3x4
#product_length_n_groups(array, 4) should return 1x2x3x4
def sum_product_length_n_combinations(array, n):
    if n == 1:
        return sum(array)
    if len(array) == n:
        return math.prod(array)

    combinations = itertools.combinations(array, n)
    res_sum = 0
    for c in combinations:
        res_sum += math.prod(c)

    return res_sum


print(sum_product_length_n_combinations([1,2,3], 2))
