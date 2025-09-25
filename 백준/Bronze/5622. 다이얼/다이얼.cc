#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int time = 0, alpha[26] = { 2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9 };

    string S;

    cin >> S;

    for (int i = 0; i < S.length(); ++i) {
        time += alpha[S[i] - 'A'] + 1;
    }

    cout << time;
    return 0;
}