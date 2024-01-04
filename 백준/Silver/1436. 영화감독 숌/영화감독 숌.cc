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

	int N;
	int count = 0;
	string str;
	
	cin >> N;
	int i = 666;
	while(1) {
		str = to_string(i);
		if (str.find("666") != string::npos) {
			count += 1;
		}
		if (count == N) {
			cout << str;
			break;
		}
		i++;
	}

}   