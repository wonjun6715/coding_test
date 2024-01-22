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

    int n;
    int x;
    int tmp;
    deque<int> dq;

    cin >> n;

    for (int i = 0; i < n; i++) {
        int cmd;
        cin >> cmd;
        switch (cmd) {
        case 1:
            
            cin >> x;
            dq.push_front(x);
            break;
        case 2:
            cin >> x;
            dq.push_back(x);
            break;
        case 3:
            if (!dq.empty()) {
                tmp = dq.front();
                dq.pop_front();
                cout << tmp << "\n";
                break;
            }
            else {
                cout << -1 << "\n";
                break;
            }
        case 4:
            if (!dq.empty()) {
                tmp = dq.back();
                dq.pop_back();
                cout << tmp << "\n";
                break;
            }
            else {
                cout << -1 << "\n";
                break;
            }
        case 5:
            cout << dq.size() << "\n";
            break;
        case 6:
            if (!dq.empty()) {
                cout << 0 << "\n";
                break;
            }
            else {
                cout << 1 << "\n";
                break;
            }
        case 7:
            if (!dq.empty()) {
                tmp = dq.front();
                cout << tmp << "\n";
                break;
            }
            else {
                cout << -1 << "\n";
                break;
            }
        case 8:
            if (!dq.empty()) {
                tmp = dq.back();
                cout << tmp << "\n";
                break;
            }
            else {
                cout << -1 << "\n";
                break;
            }
        }
        

    }

    
}