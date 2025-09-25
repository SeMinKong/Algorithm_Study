#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string createNumber(const vector<char>& inequalities, bool descending) {
    vector<int> digits(10);
    for (int i = 0; i < 10; ++i) {
        digits[i] = i;
    }
    if (descending) {
        reverse(digits.begin(), digits.end());
    }

    vector<int> result, stack;
    int k = inequalities.size();

    for (int i = 0; i < k; ++i) {
        stack.push_back(digits.back());
        digits.pop_back();

        if ((descending && inequalities[i] == '<') || (!descending && inequalities[i] == '>')) {
            while (!stack.empty()) {
                result.push_back(stack.back());
                stack.pop_back();
            }
        }
    }

    stack.push_back(digits.back());
    result.insert(result.end(), stack.rbegin(), stack.rend());

    string number;
    for (int digit : result) {
        number += to_string(digit);
    }
    return number;
}

int main() {
    int k;
    cin >> k;
    vector<char> inequalities(k);
    for (int i = 0; i < k; ++i) {
        cin >> inequalities[i];
    }

    string maxNumber = createNumber(inequalities, false);
    string minNumber = createNumber(inequalities, true);

    cout << maxNumber << endl;
    cout << minNumber << endl;

    return 0;
}
