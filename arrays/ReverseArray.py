
def reverse_array(arr):
    start = 0
    end = len(arr)-1

    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        start += 1
        end -= 1


arr_nums = [1,2,3,4,5]

reverse_array(arr_nums)
print(arr_nums)