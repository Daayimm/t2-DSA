

"""
Given an integer N, 
print a butterfly star pattern with 2N − 1 rows. 
The number of stars increases from 1 to N in the upper half and then decreases from N − 1 to 1 
in the lower half, forming a symmetric butterfly shape


"""


def printButterfly(n):
    spaces = 2*n-1
    stars = 0
    for i in range(1,spaces+1):
        if i <= n:
            spaces -= 2
            stars += 1
        else:
            spaces += 2
            stars -= 1
    
        for j in range(1,stars+1):
            print('*',end='')
            
        for j in range(1,spaces+1):
            print(" ",end='')
        
        for j in range(1,stars+1):
            if j!= n:
                print("*",end='')
    
        print()
    
printButterfly(5)
            
    