#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio;
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;
	int count = 0;

	cin >> n;
	cin >> m;

	int arr[15000];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			if (arr[i] + arr[j] == m) {
				count++;
			}
		}
	}

	cout << count;
}