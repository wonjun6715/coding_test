#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main() {
	ios::sync_with_stdio;
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	int x;
	int result = 0;

	cin >> n;

	vector<int> A(n, 0);

	int st = 0;
	int en = n - 1;
	for (int i = 0; i < n; i++) {
		cin >> A[i];
	}

	cin >> x;

	sort(A.begin(), A.end());

	while (st < en) {
		if (A[st] + A[en] == x) {
			result++;
			st++;
		}
		else if (A[st] + A[en] < x) {
			st++;
		}
		else if (A[st] + A[en] > x) {
			en--;
		}
	}
	cout << result;
}