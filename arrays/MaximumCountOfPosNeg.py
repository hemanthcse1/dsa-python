

def max_count(num_arr):
    minCount = maxCount = 0

    for i in range(len(num_arr)):
        if num_arr[i] < 0:
            minCount +=1
        elif num_arr[i] > 0:
            maxCount +=1
    return max(minCount, maxCount)

arr = [-2,-3,-4,-5,-6,-7,-8,-9]
print(max_count(arr))

arr2 = [-2,-2,1,4,5,6]
print(max_count(arr2))