


def towerOfHanoi(n,fromRod,helpRod,toRod):
    
    # base case
    if n == 0:
        return
    
    towerOfHanoi(n-1,fromRod,toRod,helpRod )
    print("Disk", n, " moved from ", fromRod, " to ", toRod)
    towerOfHanoi(n-1,helpRod,fromRod,toRod)
    
if __name__ == "__main__":
    n = 3
    
    # A, C, B are the name of rods
    towerOfHanoi(n, 'A', 'C', 'B')



