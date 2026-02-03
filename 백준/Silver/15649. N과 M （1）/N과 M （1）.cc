#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

int path[9];
bool visited[9];
int N, M;

void func(int lev)
{
	if (lev == M)
	{
		for (int i = 0; i < M; i++)
		{
			cout << path[i] <<" ";
		}
		cout << endl;

		return;
	}
	for (int i = 0; i < N; i++)
	{
		if (visited[i + 1])continue;
		path[lev] = i + 1;
		visited[i + 1] = true;
		func(lev + 1);
		visited[i + 1] = false;
	}
}

int main()
{
	cin >> N >> M;
	func(0);
	return 0;
}
