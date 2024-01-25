#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int k;
    int n, m;

    cin >> k;
    
    for (int i = 0; i < k; i++) {
        int count = 0;
        cin >> n >> m;

        queue<pair<int, int>> qu;
        priority_queue<int> pq;
        for (int j = 0; j < n; j++) {
            int tmp;
            cin >> tmp;
            qu.push(make_pair(j, tmp));
            pq.push(tmp);
        }
        while (!qu.empty()) {
            int index = qu.front().first;
            int value = qu.front().second;
            qu.pop();
            if (value == pq.top()) {
                count++;
                pq.pop();
                if (m == index) {
                    cout << count << "\n";
                    break;
                }
            }
            else {
                qu.push(make_pair(index, value));
               
            }
        }
    }

   
}