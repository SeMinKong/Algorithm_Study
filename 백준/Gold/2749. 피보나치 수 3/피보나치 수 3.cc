#include <iostream>

using namespace std;

const int MOD = 1000000;
const int PISANO = 1500000;

int fib[PISANO] = { 0, 1 };

int main() {
    long long n;
    cin >> n;

    for (int i = 2; i < PISANO; i++) {
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD;
    }

    cout << fib[n % PISANO];

    return 0;
}
