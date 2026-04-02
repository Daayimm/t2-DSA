
from __future__ import print_function
import math


class MinHeap():
    def __init__ (self):
        self.arr = []
    
    def left(self,i) : return 2*i + 1
    def right(self,i) : return 2*i + 2
    
    def parent(self,i) : return (i-1) // 2
    
    def getMin(self):
        return self.arr[0] if self.arr else None
    
    def insert(self,k):
        self.arr.append(k)
        
        i = len(self.arr) -1
        
        while i > 0 and k < self.arr[self.parent(i)]:
            self.arr[self.parent(i)],self.arr[i] = self.arr[i] , self.arr[self.parent(i)]
            i = self.parent(i)
    
    
    def decrease_key(self,i,new_val):
        self.arr[i] = new_val

        while i != 0 and self.arr[i] < self.arr[self.parent(i)]:
            p = self.parent(i)
            self.arr[i] , self.arr[p] = self.arr[p] , self.arr[i]
            
            i = p
    
    def extract_min(self):
        root = self.arr[0]
        
        self.arr[0] = self.arr[-1]
        
        self.arr.pop(-1)
        
        self.min_heapify(0)    
        return root
    
    def min_heapify(self,i):
        
        left = self.left(i)
        right = self.right(i)
        
        smallest = i
        
        if left < len(self.arr) and self.arr[left] < self.arr[smallest]:
            smallest = left
        if right < len(self.arr) and self.arr[right] < self.arr[smallest]:
            smallest = right 
        
        if smallest != i:
            self.arr[i],self.arr[smallest] = self.arr[smallest] , self.arr[i]
            self.min_heapify(smallest)
    
    def delete_key(self,i):
        
        self.decrease_key(i,float('-inf'))
        
        self.extract_min()
            
            
            
        
        
# --- Execution ---
h = MinHeap()
h.insert(3)
h.insert(2)
h.delete_key(1)
h.insert(15)
h.insert(5)
h.insert(4)
h.insert(45)

# Prints values on the same line separated by spaces
print(h.extract_min(), end=" ") 
print(h.getMin(), end=" ") 

h.decrease_key(2, 1)
print(h.extract_min())     


