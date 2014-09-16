import random

def RSAEncrypt():
    print GetPrime()


def GetPrime():
    isPrime = False
    while isPrime == False:
        n = random.randint(0, 0xffffffff)
        if n%2 != 0:
            for i in range(3, int(n**.5), 2):
                if n%i == 0:
                    isPrime = False
                else:
                    isPrime = True               
    return n

if __name__ == '__main__':
    RSAEncrypt()
    