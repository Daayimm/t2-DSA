
"""Given an array arr[], check if it is sorted in ascending order or not. 
Equal values are allowed in an array and two consecutive equal values are considered sorted
"""




def isSorted(arr):
    
    
    for i in range(len(arr) - 1):
        if (arr[i] <= arr[i+1]):
            continue
        else:
            return False
    return True

arr1 = [90, 80, 100, 70, 40, 30]
arr2 = [10, 20, 30, 40, 50]
print(isSorted(arr1))
print(isSorted(arr2))

