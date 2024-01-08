#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main() {
	ios::sync_with_stdio;
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;

	cin >> n >> m;

	vector<int> A(n + 1, 0);

	for (int i = 1; i <= n; i++) {
		A[i] = i;
	}

	for (int i = 0; i < m; i++) {
		int a, b;

		cin >> a >> b;

		while (a < b) {
			int tmp;
			tmp = A[a];
			A[a] = A[b];
			A[b] = tmp;
			a++;
			b--;
		}
	}

	for (int i = 1; i <= n; i++) {
		cout << A[i] << " ";
	}
}