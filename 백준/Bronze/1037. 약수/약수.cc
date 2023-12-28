#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int nums;
	int a, b;
	int max = -1;
	int min = 9999;

	cin >> nums;
	for (int i = 0; i < nums; i++) {
		cin >> a;
		if (a > max) {
			max = a;
		}
		if (a < min) {
			min = a;
		}
	}
	cout << max * min << endl;
}