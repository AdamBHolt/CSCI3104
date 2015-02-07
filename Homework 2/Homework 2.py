import random
import time
import math

def RSAEncrypt():
    start = time.time()
    
    #Original message to encrypt
    x = 3104
    
    #Number of bits for random numbers
    n = 12
    
    #Set p and q as large random numbers
    p = GetPrime(n)
    q = GetPrime(n)

    #N = p * q
    N = p * q
    #Set e to a relative prime number of p and q
    e = RelativePrime(p, q)
    #Find x using Euclid's Extended algorithm to find d 
    d1 = EuclidExtended(e, (p-1) * (q-1))
    d = d1[0]%((p-1)*(q-1))

    print "Public key (N,e): (", N, ",", e, ")"
    print "Private key (N,d): (", N, ",", d, ")"

    print "\nOriginal message: ", x
    
    encrypted = Encrypt(x, e, N)
    print "Encoded message: ", encrypted
        
    decrypted = Decrypt(encrypted, d, N)

    print "Decoded message: ", decrypted
    
    print "\nn=",n
    print "Run time: ", time.time()-start, " seconds"

def GetPrime(x):
    isPrime = False
    while isPrime == False:
        n = random.getrandbits(x)
        if n%2 != 0:
            for i in range(3, int(math.sqrt(n)), 2):
                if n%i == 0:
                    isPrime = False
                else:
                    isPrime = True               
    return n

def RelativePrime(x, y):
    for i in range(2, 100):
        if Euclid(i,(x-1) * (y-1)) == 1:
            return i
        
def Euclid(a, b):
    if b == 0:
        return a
    else:
        return Euclid(b, a%b)

def EuclidExtended(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x, y, d = EuclidExtended(b, a%b)
        return (y, x-(a//b) * y, d)

def Encrypt(x, e, N):
    return pow(x, e)%N

def Decrypt(y, d, N):
    return pow(y, d)%N
    
if __name__ == '__main__':
    RSAEncrypt()