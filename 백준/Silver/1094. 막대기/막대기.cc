#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int X;
	int len = 64;
	int count = 0;

	cin >> X;

	while (1) {
		if (len > X) {
			len = len / 2;
		}
		else {
			X = X - len;
			count++;
			len = len / 2;
		}
		if (X == 0) {
			break;
		}
	}
	cout << count << "\n";

}