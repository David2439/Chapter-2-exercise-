from math import sqrt as sq

def isprime(n):

    if n <= 1:
        return False
    
    else:
        for x in range(2,int(sq(n) + 1)):
            if n%x ==0:
                return False
            
        return True