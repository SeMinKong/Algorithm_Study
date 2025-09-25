#include <iostream>

using namespace std;

int subject[1000];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, max = 0;
    double sum = 0, avg;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        cin >> subject[i];
        if (subject[i] > max)
            max = subject[i];
    }

    for (int i = 0; i < N; ++i) {
        sum += (subject[i] / (double)max) * 100;
        avg = sum / N;
    }

    cout << avg;

    return 0;
}