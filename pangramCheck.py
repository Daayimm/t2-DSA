

"""Given a string s, check if it is Pangram or not. 
A pangram is a sentence containing all letters of the English Alphabet.
    """





def checkPangram(s):
    
    s = s.lower()
    for l in "abcdefghijklmnopqrstuvwxyz":
        if l in s:
            continue
        else:
            return False
    return True


s = "The quick brown fox jumPs over the Lazy dog"
print(checkPangram(s))       
     