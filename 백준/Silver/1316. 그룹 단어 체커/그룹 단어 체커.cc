#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    string S;
    int N, cnt = 0;

    cin >> N;
    cin.ignore();

    for (int i = 0; i < N; ++i) {
        getline(cin, S);
        bool alphabet[26] = {};

        for (int j = 0; j < S.length(); ++j) {
            if (alphabet[S[j] - 'a'] == false) {
                alphabet[S[j] - 'a'] = true;
            }
            else {
                if (j > 0 && S[j -1] != S[j]) {
                    break;
                }
            }
            if (j == S.length() - 1) {
                cnt++;
            }
        }
    }
    cout << cnt;
    return 0;
}
