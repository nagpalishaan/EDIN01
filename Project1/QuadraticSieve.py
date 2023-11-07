import math

def bPrimes(b):
    primes = []
    filename = "prim_2_24.txt"
    with open(filename, 'r') as file:
        for line in file:
            for number in line.split():
                prime = int(number)
                if prime > b:
                    break
                else:
                    primes.append(prime)
    return primes

def bSmooth(primes, x):
    if x == 0:
        return False
    for prime in primes:
        while x % prime == 0:
            x //= prime
    if x == 1:
        return True
    else:
        return False

def quadraticSieve(N, primes):
    for total in range(2, N):
        for k in range(1, total):
            j = total - k
            r = int(math.sqrt(k * N)) + j
            test = r*r % N
            smooth = bSmooth(primes, test)
            if smooth:
                print("hello")
                return r

if __name__ == '__main__':
    primes = bPrimes(101)
    for prime in primes:
        print(prime)
    x = 21
    y = 25
    z = 31
    w = 26
    print(bSmooth(primes, x))
    print(bSmooth(primes, y))
    print(bSmooth(primes, z))
    print(bSmooth(primes, w))
    quadraticSieve(100, primes)
