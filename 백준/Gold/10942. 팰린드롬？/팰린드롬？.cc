#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<int> arr(n + 1);
    vector<vector<bool>> dp(n + 1, vector<bool>(n + 1, false));

    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
        dp[i][i] = true;
    }

    for (int i = 1; i < n; i++) {
        if (arr[i] == arr[i + 1]) {
            dp[i][i + 1] = true;
        }
    }

    for (int length = 3; length <= n; length++) {
        for (int start = 1; start <= n - length + 1; start++) {
            int end = start + length - 1;
            if (arr[start] == arr[end] && dp[start + 1][end - 1]) {
                dp[start][end] = true;
            }
        }
    }

    int m;
    cin >> m;
    while (m--) {
        int s, e;
        cin >> s >> e;
        cout << dp[s][e] << '\n';
    }

    return 0;
}
