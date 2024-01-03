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

	long N;
	int B;
	int na;
	string tmp;
	char result;
	int count = 0;

	cin >> N >> B;

	while (N > 0) {
		na = N % B;
		N = N / B;
		if (na >= 10) {
			na = na + 55;
			result = na;
			tmp += (char)result;
			//cout << (char)result;
		}
		else {
			tmp += to_string(na);
			//cout << to_string(na);
		}
	}

	for (int i = tmp.length() - 1; i >= 0; i--) {
		cout << tmp[i];
	}
}