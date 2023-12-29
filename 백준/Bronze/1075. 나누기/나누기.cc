#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int N;
	int F;

	int count = 0;
	int mod;
	cin >> N;
	cin >> F;

	while (N % 100 != 0) {
		mod = N % 100;
		N = N - mod;
	}
	
	while (N % F != 0) {
		N++;
		count++;
	}
	
	if (count >= 10) {
		cout << count << "\n";
	}
	else {
		string result = to_string(count);
		cout << '0' << result << "\n";
	}
	


}