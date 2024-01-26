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
    
    cin >> n >> m;
    
    map<string, int> ma;
    vector<string> v;

    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        ma[str]++;
    }

    for (int i = 0; i < m; i++) {
        string str;
        cin >> str;
        ma[str]++;
        if (ma[str] == 2) {
            v.push_back(str);
        }
    }
    sort(v.begin(), v.end());
    cout << v.size() << "\n";
    for (auto& e : v) {
        cout << e << "\n";
    }
   
}