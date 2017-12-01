import math
import random
import sys
from fractions import gcd

def giveMePrimes():
    primeList = list()
    for num in range(1000,10001):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            primeList.append(num)
    return primeList


def pickRandomPrime(primes):
    secure_random = random.SystemRandom()
    return secure_random.choice(primes)

def main():
    ###pick random prime
    pl = giveMePrimes()
    P = pickRandomPrime(pl)
    print("Modulus Number: %s" % P)
    #### static base number
    secure_random = random.SystemRandom()
    N = secure_random.choice(range(1,10001))
    print("Base Number: %s" % N)
    ###Secret Exponent
    A = secure_random.choice(range(1,10001))
    B = secure_random.choice(range(1,10001))
    if gcd(N,A) != 1:
        print("N(%s) and A(%s) can't be relative primes" % (N,A))
        sys.exit(1)
    if gcd(N,B) != 1:
        print("N(%s) and B(%s) can't be relative primes" % (N,B))
        sys.exit(1)
    print("A is %s" % A)
    print("B is %s" % B)

    ###Computation numbers
    J = N ** A % P
    K = N ** B % P
    print("A computational numbers: %s" % J)
    print("B computational numbers: %s" % K)

    print("this %s should be the same than this %s" % (K ** A % P , J ** B % P))

if __name__ == "__main__": 
    main()
