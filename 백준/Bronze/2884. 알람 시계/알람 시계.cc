#include <iostream>

using namespace std;

int main() {
    int H, M;

    cin >> H >> M;

    if (0 < H) {
        if (M - 45 < 0) {
            M += 15;
            H -= 1;
        }
        else {
            M -= 45;
        }
    }
    else {
        if (M - 45 < 0) {
            M += 15;
            H = 23;
        }
        else {
            M -= 45;
        }
    }
    cout << H << ' ' << M;
        
    return 0;
}