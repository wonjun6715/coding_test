#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio;
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;

	cin >> n >> m;

	int arr[100] = { 0, };

	for (int i = 1; i <= n; i++) {
		arr[i] = i;
	}

	for (int i = 0; i < m; i++) {
		int a, b;
		int tmp;
		cin >> a >> b;

		tmp = arr[a];
		arr[a] = arr[b];
		arr[b] = tmp;
	}

	for (int i = 1; i <= n; i++) {
		cout << arr[i] << " ";
	}
}