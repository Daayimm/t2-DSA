

# Hollow Diamond Pattern

# Given an integer N, print the pattern shown below.


def hollow_diamond(n):
    
    for i in range (1, n+1):
        if i == 1:
            print(" " * (n-1)+"*")
        
        else:
            print(" " * (n-i)+'*' + " " * (2*i-3) +  '*' )
    
    for j in range (n+1, 2*n):
        if j == (2*n - 1):
            print(" " * (n-1) +"*" )
        else:
            print(" " * (j-n)+'*' + " " * (2*(2*n-j)-3) +  '*' )
        
if __name__ == '__main__':
    hollow_diamond(5)
