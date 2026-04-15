


"""Given an array arr[] of size n, find the element that appears
more than ⌊n/2⌋ times. If no such element exists, return -1
"""

def majorityElement(arr):
    target = len(arr) / 2
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        
        if d[i] > target:
            return i
        
    return -1

arr1 = [1, 1, 2, 1, 3, 5, 1]
arr2 = [7]
arr3 = [2, 13]

print(majorityElement(arr1))
print(majorityElement(arr2))
print(majorityElement(arr3))