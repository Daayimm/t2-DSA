
"""     Given an array arr[] of size n consisting of non-negative integers, 
        where each element represents the height of a bar in an elevation map 
        and the width of each bar is 1, determine the total amount of water 
        that can be trapped between the bars after it rain
    """
def maxWater(arr):
    
    
    # one condition has to be that 1st and last element are non zero
    left, right = 0,len(arr)-1
    left_max,right_max = 0,0
    water = 0
    while left<right:
        if arr[left] < arr[right]:
            left_max = max(left_max,arr[left])
            water += left_max - arr[left]
            left += 1
        else:
            right_max = max(right_max,arr[right])
            water += right_max - arr[right]
            right -= 1
            
  
    return water

arr = [2, 1, 5, 3, 1,0,0, 4]
print(maxWater(arr))
