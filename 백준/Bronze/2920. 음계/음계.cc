#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N[8], adm = 0, k = 0;

    for (int i = 0; i < 8; ++i) {
        cin >> N[i];
    }

    while (k < 7) {
        if (N[k] + 1 == N[k + 1]) {
            adm = 1;
        }
        else if (N[k] - 1 == N[k + 1]) {
            adm = 2;
        }
        else {
            adm = 0;
            break;
        }
        k++;
    }

    if (adm == 1) {
        cout << "ascending";
    }
    else if (adm == 2) {
        cout << "descending";
    }
    else {
        cout << "mixed";
    }

    return 0;
}
