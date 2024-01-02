#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int count = 0;
	int tmp = 0;
	string A;
	string B;
	int position = 0;
	int position1 = 0;
	int min = 9999;
	cin >> A >> B;

	if (A.length() == B.length()) {
		for (int i = 0; i < A.length(); i++) {
			if (A[i] != B[i]) {
				count++;
			}
		}
		cout << count << "\n";
	}
	else if (A.length() != B.length()) {
		for (int i = 0; i < B.length() - A.length() + 1; i++) {
			position = i;
			tmp = 0;
			for (int j = 0; j < A.length(); j++) {
				if (A[j] != B[position]) {
					position++;
					tmp++;
				}
				else {
					position++;
				}
			}
			if (min > tmp) {
				min = tmp;
				
			}
		}
		cout << min << "\n";
	}
}