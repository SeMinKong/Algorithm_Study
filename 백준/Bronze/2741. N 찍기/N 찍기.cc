#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
   
    cin >> N;

    for (int i = 0; i < N; ++i) {
        cout << i + 1 << '\n';
    }
    return 0;
}