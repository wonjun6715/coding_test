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

    int n;

    cin >> n;
    int count = 0;
    vector<int> A(n);
    priority_queue<int, vector<int>> pq;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
        
    }
    int da = A[0];

    for (int i = 1; i < n; i++) {
        pq.push(A[i]);
    }
    
    while (!pq.empty()) {
        if (pq.top() >= da) {
            int tmp = pq.top();
            tmp--;
            da++;
            count++;
            pq.pop();
            pq.push(tmp);
        }
        else {
            pq.pop();
        }
        
    }
    cout << count;
}