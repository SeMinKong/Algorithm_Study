#include <iostream>
#include <cmath>

using namespace std;

int findIndex(int N) {
    if (N == 1) 
        return 1;

    int index = 1;
    while (true) {
        int lowerBound = pow(index, 3) - pow(index - 1, 3);
        int upperBound = pow(index + 1, 3) - pow(index, 3);
        if (N > lowerBound && N <= upperBound) {
            return index + 1;
        }
        index++;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;

    cin >> N;

    cout << findIndex(N);
    return 0;
}
