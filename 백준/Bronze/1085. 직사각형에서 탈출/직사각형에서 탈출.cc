#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int x, y, w, h;

	cin >> x >> y >> w >> h;
	int tmp1, tmp2, tmp3, tmp4;

	// 0과의 거리
	tmp1 = abs(x - 0);
	tmp2 = abs(y - 0);
	
	// w, h와의 거리
	tmp3 = abs(x - w);
	tmp4 = abs(y - h);

	int result1 = min(tmp1, tmp2);
	int result2 = min(tmp3, tmp4);

	int result = min(result1, result2);

	cout << result << "\n";


}