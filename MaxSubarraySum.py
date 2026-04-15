




"""Given an integer array arr[], find the subarray 
    (containing at least one element) 
    which has the maximum possible sum, and return that sum.
    """
    
    
    # Kadane's Algorithm
def maxSubarray(arr):
    maxSum = float('-inf')
    currentSum = 0
    
    for i in arr:
        currentSum += i
        if(currentSum > maxSum):
            maxSum = currentSum
        
        if currentSum < 0:
            currentSum = 0
    return maxSum       
        
a1 = [-3, -1, -2] 
a2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a3 = [2, 3, -8, 7, -1, 2, 3]
a4 = [-2, -4]
a5 = [5, 4, 1, 7, 8]
print(maxSubarray(a1))
print(maxSubarray(a2))
print(maxSubarray(a3))
print(maxSubarray(a4))
print(maxSubarray(a5))