#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

int path[8];
bool visited[8];
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
		path[lev] = i;
		visited[i] = true;
		func(lev + 1);
		path[lev] = 0;
		visited[i] = false;
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N >> M;
	func(1);
	return 0;
}
