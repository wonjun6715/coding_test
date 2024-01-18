#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k;
    int tmp;

    cin >> n >> k;

    cout << "<";

    deque<int> dq;

    for (int i = 0; i < n; i++) {
        dq.push_back(i + 1);
    }

    while (!dq.empty()) {
        for (int i = 0; i < k; i++) {
            tmp = dq.front();
            dq.pop_front();
            if (i < k - 1) {
                dq.push_back(tmp);
            }
        }
        if (dq.empty()) {
            cout << tmp << ">";
        }
        else {
            cout << tmp << ", ";
        }
        
    }

    
}