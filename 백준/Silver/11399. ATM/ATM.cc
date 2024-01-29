#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n;

	int sum = 0;
	int tmp = 0;

	cin >> n;

	vector<int> v(n);

	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}

	sort(v.begin(), v.end());

	for (int i = 0; i < n; i++) {
		sum = sum + tmp + v[i];
		tmp += v[i];
	}

	cout << sum;


}