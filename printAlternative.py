
# You are given an array arr[], the task is to 
# return a list elements of arr in alternate order (starting from index 0)





def print_alt(n):
    
    return n[::2]
    # for i in range(0,len(n),2):
    #     print (n[i])


arr = [1,2,3,4,5,6]

print(print_alt(arr))