# problem
# https://www.geeksforgeeks.org/dsa/largest-sum-contiguous-subarray/
# Given an integer array arr[], find the subarray (containing at least one element) which has the maximum possible sum, and return that sum.
# Note: A subarray is a continuous part of an array.
#
# Examples:
#
# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.
#
# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray [-2] has the largest sum -2.
#
# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25
# Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.

def max_sub_array_sum(input_arr):
    arr_len = len(input_arr)
    if arr_len == 0:
        return [], -1
    temp_sum = input_arr[0]
    temp_st_index = 0
    temp_end_index = 0
    st_index = 0
    end_index = 0
    sum = input_arr[0]

    index = 1
    while index < arr_len:
        if input_arr[index] + temp_sum > temp_sum:
            temp_sum = input_arr[index] + temp_sum
            temp_end_index = index
            if temp_sum > sum:
                sum = temp_sum
                st_index = temp_st_index
                end_index = temp_end_index
        elif input_arr[index] + temp_sum <= 0:
            temp_sum = 0
            temp_st_index = index + 1
            temp_end_index = index + 1
        else:
            temp_sum = input_arr[index] + temp_sum
            temp_end_index = index
        index += 1

    if temp_sum > sum:
        sum = temp_sum
        st_index = temp_st_index
        end_index = temp_end_index

    print(f"Sum: {sum} start index: {st_index} end_index: {end_index}")

def max_sub_array_sum2(input_arr):
    arr_len = len(input_arr)
    if arr_len == 0:
        return -1
    temp_sum = input_arr[0]
    temp_st_index = 0
    temp_end_index = 0
    st_index = 0
    end_index = 0
    sum = input_arr[0]

    index = 1
    while index < arr_len:
        if input_arr[index] < 0:
            if temp_sum > 0:
                if temp_sum + input_arr[index] < 0:
                    temp_sum = 0
                    temp_st_index = index + 1
                    temp_end_index = index + 1
                else:
                    temp_sum = temp_sum + input_arr[index]
                    temp_end_index = index
            else:
                if temp_sum < input_arr[index]:
                    temp_sum = input_arr[index]
                    temp_st_index = index
                    temp_end_index = index

        else:
            if temp_sum > 0:
                temp_sum = temp_sum + input_arr[index]
                temp_end_index = index
            else:
                temp_sum = input_arr[index]
                temp_st_index = index
                temp_end_index = index

        if sum < temp_sum:
            sum = temp_sum
            st_index = temp_st_index
            end_index = temp_end_index
        #print(f"index: {index} Sum: {sum} start index: {st_index} end_index: {end_index} temp_sum:{temp_sum}, temp_st: {temp_st_index}, temp_end: {temp_end_index}")
        index += 1

    print(f"Sum: {sum} start index: {st_index} end_index: {end_index}")
    return sum



# max_sub_array_sum([2, 3, -8, 7, -1, 2, 3])
# max_sub_array_sum([5, 4, 1, 7, 8])
# max_sub_array_sum([-22, 10, 19, 21, 22, 5, -22, -23, 15, 0, 45, -89, 10])
# max_sub_array_sum([-2, -4])
max_sub_array_sum2([2, 3, -8, 7, -1, 2, 3])
max_sub_array_sum2([5, 4, 1, 7, 8])
max_sub_array_sum2([-22, 10, 19, 21, 22, 5, -22, -23, 15, 0, 45, -89, 10])
max_sub_array_sum2([-2, -4])
max_sub_array_sum2([-3, -2, -6, -1, -7, -4])


