
from typing import List

# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.




def remove_Dup(arr : List[int]):

    expetced_num = []
    
    slow = 1 
    arr.sort()
    
    for fast in range(1,len(arr)):
        if arr[slow-1] != arr[fast]:
            arr[slow] = arr[fast]
            slow += 1
        
    
        

    return arr[:slow]     

 
nums = [1,1,2,2,2,2,2,3,5,5,5,5]

print(remove_Dup(nums))
                 
test1 = []
test2 = [1]
test3 = [1, 1, 1]
test4 = [1, 2, 3]
test5 = [1, 1, 2, 3, 3]

print(remove_Dup(test1))
print(remove_Dup(test2))
print(remove_Dup(test3))
print(remove_Dup(test4))
print(remove_Dup(test5))

