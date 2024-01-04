#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <cmath>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	int arr[100];
	int total;
	int result = 0;

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		arr[i] = tmp;
	}

	sort(arr, arr + N);

	for (int i = 0; i < N - 2; i++) {
		for (int j = i + 1; j < N - 1; j++) {
			for (int k = i + 2; k < N; k++) {
				total = arr[i] + arr[j] + arr[k];
				if (total <= M && total > result) {
					result = total;
				}
			}
		}
	}
	cout << result;
}