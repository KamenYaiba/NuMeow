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


print(elementary_symmetric_sum([4, 2, 3]))

