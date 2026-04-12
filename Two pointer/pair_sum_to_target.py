from typing import List

# Given a sorted array arr (sorted in ascending order) and a target, find if there exists any pair of elements (arr[i], arr[j]) 
# such that their sum is equal to the target.


def twoSum(arr: List[int],target:int):
    left,right = 0, len(arr) -1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left + 1, right+1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1,1]
        
        



if __name__ == '__main__':
    arr = [2, 7, 11, 15]
    target = 9
    result = twoSum(arr, target)
    for num in result:
        print(num, end=' ')
    print()
            
    

