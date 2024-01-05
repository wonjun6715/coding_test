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
	
	int n;

	cin >> n;

	if (n % 2 == 1) {
		cout << "SK";
	}
	else {
		cout << "CY";
	}
}   