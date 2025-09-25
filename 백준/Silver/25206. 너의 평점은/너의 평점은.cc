#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    pair<string, pair<double, string>> input;
    double score = 0, avg = 0, hakjum = 0;

    for (int i = 0; i < 20; ++i) {
        cin >> input.first >> input.second.first >> input.second.second;
        if (input.second.second == "A+") {
            score += input.second.first * 4.5;
            hakjum += input.second.first;
        }
        else if (input.second.second == "A0") {
            score += input.second.first * 4.0;
            hakjum += input.second.first;
        }
        else if (input.second.second == "B+") {
            score += input.second.first * 3.5;
            hakjum += input.second.first;
        }
        else if (input.second.second == "B0") {
            score += input.second.first * 3.0;
            hakjum += input.second.first;
        }
        else if (input.second.second == "C+") {
            score += input.second.first * 2.5;
            hakjum += input.second.first;
        }
        else if (input.second.second == "C0") {
            score += input.second.first * 2.0;
            hakjum += input.second.first;
        }
        else if (input.second.second == "D+") {
            score += input.second.first * 1.5;
            hakjum += input.second.first;
        }
        else if (input.second.second == "D0") {
            score += input.second.first * 1.0;
            hakjum += input.second.first;
        }
        else if(input.second.second == "P")
            continue;
        else
            hakjum += input.second.first;
    }

        avg = score / hakjum;

        cout << avg;

    return 0;
}