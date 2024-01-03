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

	map<string, int> result;
	result["black"] = 0;
	result["brown"] = 1;
	result["red"] = 2;
	result["orange"] = 3;
	result["yellow"] = 4;
	result["green"] = 5;
	result["blue"] = 6;
	result["violet"] = 7;
	result["grey"] = 8;
	result["white"] = 9;

	string color1, color2, color3;

	cin >> color1 >> color2 >> color3;
	long long tmp;
	tmp = pow(10, result[color3]);
	cout << stoi(to_string(result[color1]) + to_string(result[color2])) * tmp;



	
}