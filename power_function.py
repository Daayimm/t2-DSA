



# Given two numbers b(base) and e(exponent), calculate the value of be.




def power(b,e):
    pow = 1    
    for i in range(abs(e)):
        pow = pow * b
        
    if e < 0:
        return 1 / pow
    
    return pow
if __name__ == '__main__':
    print(power(3,5))
    print(power(-2,-2))

