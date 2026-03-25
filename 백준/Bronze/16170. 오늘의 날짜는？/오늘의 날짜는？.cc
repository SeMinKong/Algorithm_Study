#include <iostream>
#include <ctime>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    time_t now = time(nullptr);
    struct tm* t = gmtime(&now);

    cout << t->tm_year + 1900 << "\n";
    cout.width(2);
    cout.fill('0');
    cout << t->tm_mon + 1 << "\n";
    cout.width(2);
    cout.fill('0');
    cout << t->tm_mday << "\n";

    return 0;
}