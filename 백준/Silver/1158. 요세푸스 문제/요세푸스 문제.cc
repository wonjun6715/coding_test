#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, K;

	cin >> N >> K;

	queue<int> qu;

	for (int i = 0; i < N; i++) {
		qu.push(i + 1);
	}
	cout << "<";
	while (!qu.empty()) {
		for (int i = 0; i < K - 1; i++) {
			qu.push(qu.front());
			qu.pop();
		}

		if (qu.size() != 1) {
			cout << qu.front() << ", ";
		}
		else {
			cout << qu.front() << ">";
		}
		qu.pop();
	}

}