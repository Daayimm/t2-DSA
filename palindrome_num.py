
# Check if a number is Palindrome

def palindrome_num(n):
    
    empty_str = ''
    if n < 0:
        n = abs(n)
    
    n_str = str(n)
    
    for i in range(len(n_str)-1,-1,-1):
        empty_str += n_str[i]
    if empty_str == n_str:
        return True
    else:
        return False

if __name__ == '__main__':
      n = 12321
      print(palindrome_num(n))
      b = -121
      print(palindrome_num(b))
      x = 7
      print(palindrome_num(x))
      c = 12345
      print(palindrome_num(c))
    


