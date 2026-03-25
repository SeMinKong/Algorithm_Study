#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    double score = 0.0;

    if (s == "A+") score = 4.3;
    else if (s == "A0") score = 4.0;
    else if (s == "A-") score = 3.7;
    else if (s == "B+") score = 3.3;
    else if (s == "B0") score = 3.0;
    else if (s == "B-") score = 2.7;
    else if (s == "C+") score = 2.3;
    else if (s == "C0") score = 2.0;
    else if (s == "C-") score = 1.7;
    else if (s == "D+") score = 1.3;
    else if (s == "D0") score = 1.0;
    else if (s == "D-") score = 0.7;
    else score = 0.0;

    cout << fixed;
    cout.precision(1);
    cout << score;

    return 0;
}