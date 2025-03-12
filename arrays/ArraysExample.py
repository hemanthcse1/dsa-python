from array import *

def print_squares(num_array):
    print("The square roots")
    for i in range(len(num_array)):
        val = arr[i]
        val = val * val
        print(val)

arr = array('i', [2,5,7,9,3,8])
newArr = array(arr.typecode,(a for a in arr))

for i in range(len(arr)):
    print(arr[i])

print_squares(newArr)
