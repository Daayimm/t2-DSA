"""Given an array, arr[] of n integers, and an integer element x, find whether element x 
is present in the array. Return the index of the first occurrence
of x in the array, or -1 if it doesn't exist."""



def array_search(arr,x):
    
    for i in range(0,len(arr)):
        if arr[i] == x:
            return i
            break
      
    return -1
        

arr = [1,2,4,5,3]
print(array_search(arr,5))