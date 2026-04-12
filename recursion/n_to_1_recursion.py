


def printNos(n):
    if n == 0 :
        return

    
    print(n,end=' ')
    printNos(n-1)
    
    
if __name__ == '__main__':
    printNos(10)