

# Given a positive integer n, print a pyramid pattern consisting of stars (*) such that the number of rows equals n. 
# The pyramid should be center-aligned as shown in the example below


def printPyr(n):
    
    if n == 0:
        return 
    
    for i in range (1,n+1):
        print(" " * (n-i), end = ' ')
        print("*" * (2*i-1) )
        
        
    


if __name__ == '__main__':
    printPyr(5)