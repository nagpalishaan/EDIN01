#include "LongInt_unix.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

vector<LongInt> bPrimes(LongInt b)
{
    vector<LongInt> primes;

    fstream file;
    string word, t, q, filename;

    filename = "prim_2_24.txt";

    file.open(filename.c_str());

    while (file >> word)
    {
        LongInt prime(stoi(word));
        if (prime > b)
        {
            break;
        }
        else
        {
            primes.push_back(prime);
        }
    }

    return primes;
}

bool bSmooth(vector<LongInt> primes, LongInt x)
{
    if (x == 0) return false;

    for (int i = 0; i < primes.size(); i++)
    {
        if (x % primes[i] == 0)
        {
            x /= primes[i];
            i -= 1;
        }
    }

    if (x == 1) return true;
    else return false;
}

void quadraticSieve(LongInt N, vector<LongInt> primes)
{
    LongInt one(1);

    for (LongInt total = 2; total < N; total = total + one)
    {
        for (LongInt k = 1; k < total; k = k + one)
        {
            LongInt j = total - k;
            LongInt r = (k * N).powfn(.5) + j;
            LongInt test = r*r % N;
            bool smooth = bSmooth(primes, test);

            if (smooth)
            {
                r.DecOutput("r");
                cout << "hello" << endl;
                return;
            }
        }
    }
    // (j, k)
    // (1,1) 2
    // (1,2), (2,1) 3
    // (1,3), (2,2), (3,1) 4

}

int main()
{
    vector<LongInt> primes = bPrimes(101);
    for (int i = 0; i < primes.size(); i++)
    {
        primes[i].DecOutput("");
    }

    LongInt x(21);
    LongInt y(25);
    LongInt z(31);
    LongInt w(26);

    cout << bSmooth(primes, x) << endl;
    cout << bSmooth(primes, y) << endl;
    cout << bSmooth(primes, z) << endl;
    cout << bSmooth(primes, w) << endl;

    quadraticSieve(100, primes);
}