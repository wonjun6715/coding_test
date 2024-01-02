#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	string tmp;
	vector <string> str;
	

	cin >> n;
	
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		str.push_back(tmp);
	}

	string result = "";
	result = str[0];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < str[0].length(); j++) {
			if (result[j] != str[i][j]) {
				result[j] = '?';
			}
		}
	}
	cout << result << "\n";
}