#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>

using namespace std;

int path[9], input[9];
bool visited[10001];
int N, M;

void func(int lev)
{
	if (lev == M + 1)
	{
		for (int i = 1; i <= M; i++) {
			cout << path[i] << " ";
		}
		cout << "\n";
		return;
	}

	for (int i = 1; i <= N; i++)
	{
		path[lev] = input[i - 1];
		visited[input[i - 1]] = true;
		func(lev + 1);
		path[lev] = 0;
		visited[input[i - 1]] = false;
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> input[i];
	}

	sort(input, input + N);

	func(1);
	return 0;
}
