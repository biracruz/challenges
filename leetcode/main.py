import sys

def _sum(subarray):
    s = 0
    for i in subarray:
        i += s
    return s
    
    
def left_subarrays(input):
    #TODO: NOT STARTING ONLY FROM 0
    subarray_size = 1
    _max = -1
    
    while subarray_size < len(input) -1:
        subarray_left = input[:subarray_size]
        subarray_right = input[:-subarray_size]
        actual_sum_right = _sum(subarray_right)
        actual_sum_left = _sum(subarray_left)
        actual_sum = max(actual_sum_right, actual_sum_left)
        subarray_size += 1
        if  actual_sum> _max:
            _max = actual_sum
    
    return actual_sum

print(left_subarrays([-2,7,6,4,-1,2]))