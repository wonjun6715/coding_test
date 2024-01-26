#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    int count = 0;

    cin >> n >> m;

    map<string, int> ma1;
    map<string, int> ma2;

    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        ma1[str]++;
    }

    for (int i = 0; i < m; i++) {
        string str;
        cin >> str;
        ma2[str]++;
        if (ma1[str] == 1) {
            count++;
        }
    }

    cout << count;
   
}