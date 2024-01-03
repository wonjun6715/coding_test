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

	string arr[5];
	
	for (int i = 0; i < 5; i++) {
		string tmp;
		cin >> tmp;
		if (tmp.length() < 15) {
			tmp.append(15 - tmp.length(), ' ');
		}
		arr[i] = tmp;
	}
	for (int i = 0; i < 15; i++) {
		for (int j = 0; j < 5; j++) {
			if (arr[j][i] == ' ') {
				continue;
			}
			cout << arr[j][i];
		}
	}
}