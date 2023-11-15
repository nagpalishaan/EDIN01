import math
import subprocess
import numpy as np
from decimal import *
import time

# returns a list of primes less than or equal to b
def bPrimes(b):
    # read primes from file
    primes = []
    filename = "prim_2_24.txt"
    with open(filename, 'r') as file:
        # read each line
        for line in file:
            # read each number in line
            for number in line.split():
                # convert to int
                prime = int(number)
                # if prime is greater than b, stop
                if prime > b:
                    break
                else:
                    primes.append(prime)
    return primes

# Returns true if x is B-smooth, false otherwise
def bSmooth(primes, x):
    # create an array of size len(primes) with all 0s
    exponents = [0] * len(primes)

    # if x is 0, return false
    if x == 0:
        return False, exponents
    
    # iterate through all of the primes
    for i in range(len(primes)):
        prime = primes[i]
        # if x mod prime is equal to 0, then x is divisible by prime
        while x % prime == 0:
            # divide x by prime
            x //= prime
            # increment the exponent of prime
            exponents[i] += 1
    # if x is 1, then x is B-smooth
    if x == 1:
        return True, exponents
    else:
        return False, exponents

# computes the quadratic sieve algorithm
def quadraticSieve(N, L, primes):
    # initialize
    x = []
    y = []
    y_factors = []
    total = 2
    #
    while len(x) < L:
        for k in range(1, total):
            # compute r
            j = total - k
            r = int(math.sqrt(k * N)) + j
            test = r*r % N
            # check if b-smooth
            smooth, exponents = bSmooth(primes, test)
            # if b-smooth and not in x, add to x and y
            if smooth and r not in x:
                x.append(r)
                y.append(test)
                y_factors.append(exponents)
                if len(x) == L:
                    break
        total += 1
                
    return x, y, y_factors

# returns a string with the value of x mod 2
# this is needed for ./GaussBin.out
def mod2String(x):
    return str(x % 2)

def gaussElimination(M):
    # setup formatting for input file
    f = open("input.txt", "w")
    f.write(str(len(M)) + " " + str(len(M[0])) + "\n")
    for row in M:
        f.write(' '.join(list(map(mod2String, row))) + "\n")
    f.close()
    
    # call the c++ GaussBin program
    subprocess.run(["./GaussBin.out", "input.txt", "output.txt"])

    # convert the output file to a matrix
    solutions = [] 
    with open("output.txt", 'r') as file:
        for line in file:
            solutions.append(list(map(int, line.split())))

    return solutions[1:]

# returns gcd of a and b
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

# returns the factors of N
def factorize(N, x, solutions, M, primes):
    # set precision to 10000 bc it gave an annoying overflow error
    getcontext().prec = 10000
    # iterate through matrix
    for solution in solutions:
        #initialize
        X = Decimal(1)
        Y_exponents = np.array([0] * len(primes))
        # compute X
        for i in range(len(solution)):
            if solution[i] == 1:
                X *= Decimal(x[i])
                Y_exponents += np.array(M[i])
        Y = Decimal(1)
        # compute Y
        for i in range(len(primes)):
            Y *= Decimal(math.pow(primes[i], Y_exponents[i] / 2))
        # compute gcd
        p = abs(gcd(Y - X, Decimal(N)))
        if p != Decimal(1):
            return p, Decimal(N) / p
        
    return 0, 0


if __name__ == '__main__':
    # start time to calculate runtime
    start_time = time.time()
    # Number to factorize
    #N = 16061 * 60167
    #N = 11 * 7
    N = 235616869893895625763911
    #N = 511337 * 909451
    #N = 1149361 * 2956493
    #N = 29775497 * 29775989
    #N = 115461013 * 115639127
    #N = 303684763 * 310248241
    #N = 797 * 859

    # Primes in factor base with B = 1000
    primes = bPrimes(1000)
    
    # Use quadratic sieve algorithm to generate x and y lists, as well as M matrix
    x, y, M = quadraticSieve(N, len(primes) + 100, primes)

    # Get solutions to equation x * M = (0)
    sols = gaussElimination(M)

    # Get factors of N
    p, q = factorize(N, x, sols, M, primes)
    # print results
    print(p, "*", q, "=", N)
    # output runtime
    print("Time taken:", time.time() - start_time, "seconds")
    # Exercise 3: 453131078611 * 519975082301 = 235616869893895625763911
