import math
import subprocess
import numpy as np
from decimal import *

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
    exponents = [0] * len(primes)

    if x == 0:
        return False, exponents
    
    for i in range(len(primes)):
        prime = primes[i]
        while x % prime == 0:
            x //= prime
            exponents[i] += 1
    if x == 1:
        return True, exponents
    else:
        return False, exponents

def quadraticSieve(N, L, primes):
    x = []
    y = []
    y_factors = []
    total = 2
    while len(x) < L:
        for k in range(1, total):
            j = total - k
            r = int(math.sqrt(k * N)) + j
            test = r*r % N
            smooth, exponents = bSmooth(primes, test)
            if smooth and r not in x:
                x.append(r)
                y.append(test)
                y_factors.append(exponents)
                if len(x) == L:
                    break
        total += 1
                
    return x, y, y_factors

def mod2String(x):
    return str(x % 2)

def gaussElimination(M):
    f = open("input.txt", "w")
    f.write(str(len(M)) + " " + str(len(M[0])) + "\n")
    for row in M:
        f.write(' '.join(list(map(mod2String, row))) + "\n")
    f.close()
    
    subprocess.run(["./GaussBin.out", "input.txt", "output.txt"])

    solutions = [] 
    with open("output.txt", 'r') as file:
        for line in file:
            solutions.append(list(map(int, line.split())))

    return solutions[1:]

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def factorize(N, x, solutions, M, primes):
    getcontext().prec = 10000
    for solution in solutions:
        X = Decimal(1)
        Y_exponents = np.array([0] * len(primes))
        for i in range(len(solution)):
            if solution[i] == 1:
                X *= Decimal(x[i])
                Y_exponents += np.array(M[i])
        Y = Decimal(1)
        for i in range(len(primes)):
            Y *= Decimal(math.pow(primes[i], Y_exponents[i] / 2))

        p = abs(gcd(Y - X, Decimal(N)))
        if p != Decimal(1):
            return p, Decimal(N) / p
        
    return 0, 0


if __name__ == '__main__':
    # Number to factorize
    #N = 16061 * 60167
    #N = 11 * 7
    N = 235616869893895625763911
    #N = 511337 * 909451
    #N = 1149361 * 2956493
    #N = 29775497 * 29775989
    #N = 115461013 * 115639127
    #N = 303684763 * 310248241

    # Primes in factor base with B = 1000
    primes = bPrimes(1000)
    
    # Use quadratic sieve algorithm to generate x and y lists, as well as M matrix
    x, y, M = quadraticSieve(N, len(primes) + 100, primes)

    # Get solutions to equation x * M = (0)
    sols = gaussElimination(M)

    # Get factors of N
    p, q = factorize(N, x, sols, M, primes)
    print(p, "*", q, "=", N)

    # Exercise 3: 453131078611 * 519975082301 = 235616869893895625763911
