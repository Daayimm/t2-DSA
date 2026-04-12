


# Given an integer n. Print numbers from 1 to n using recursion.


def printNum(n):

    if n == 0:  
        return 
    
    printNum(n-1)
    
    print(n,end=' ')
    
if __name__ == '__main_':
    
    printNum(10)
    





