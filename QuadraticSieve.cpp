#include "LongInt_unix.h"
#include <vector>
#include <iostream>
#include <fstream>
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

void quadraticSieve()
{
    for (int total = 2; total < 10; total += 1)
    {
        for (int k = 1; k < total; k += 1)
        {
            int j = total - k;
            
        }
    }
    // (1,1)
    // (1,2), (2,1)

}

int main()
{
    vector<LongInt> primes = bPrimes(10);
    for (int i = 0; i < primes.size(); i++)
    {
        primes[i].DecOutput("");
    }

    LongInt x(100);
    LongInt y(25);
    LongInt z(31);
    LongInt w(26);

    cout << bSmooth(primes, x) << endl;
    cout << bSmooth(primes, y) << endl;
    cout << bSmooth(primes, z) << endl;
    cout << bSmooth(primes, w) << endl;
}