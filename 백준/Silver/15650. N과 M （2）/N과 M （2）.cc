#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

int path[9];
bool visited[9];
int N, M;

void func(int lev)
{
	if (lev == M + 1)
	{
		for (int i = 1; i <= M; i++) {
			cout << path[i] << " ";
		}
		cout << endl;
		return;
	}

	for (int i = 1; i <= N; i++)
	{
		if (visited[i] || i < path[lev - 1]) continue;

		path[lev] = i;
		visited[i] = true;
		func(lev + 1);
		path[lev] = 0;
		visited[i] = false;
	}
}

int main()
{
	cin >> N >> M;
	func(1);
	return 0;
}
