

"""Given an integer array arr[], find the sum of any two elements whose sum is closest to zero.
Note: In case if we have two ways to form sum closest to zero, return the maximum sum among them.
"""

def closest_to_zero(n):
    
    empty_arr = []
    # sort the array
    n.sort()
    
    left,right = 0 , len(n) - 1
    
    best_sum = n[left] + n[right]
    
    while left < right:
        current_sum = n[left] + n[right]
        
        if current_sum == 0:
            empty_arr.append(n[left])
            empty_arr.append(n[right])
            return empty_arr
        
        elif current_sum > 0:
            right -= 1
        elif current_sum < 0:
            left += 1
        
        if abs(current_sum) < abs(best_sum):
            best_sum = current_sum
        
        elif abs(current_sum) == abs(best_sum):
            best_sum =  max(current_sum,best_sum)
    return best_sum

arr = [0, -8, -6, 3]
print(closest_to_zero(arr))
         
            
    