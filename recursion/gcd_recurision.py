

""" Given two positive integers a and b, the task is to find the GCD of the two numbers.
Note: The GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers 
is the largest number that divides both of t
"""


def gcd(a,b):
    if a == 0 :
        return b
    elif b == 0:
        return a     
    
    
    remainder = a % b
    
    return gcd(b, remainder)
    
    
    
if __name__ == '__main__':
    
    print(gcd(100,500))
    print(20%28)



