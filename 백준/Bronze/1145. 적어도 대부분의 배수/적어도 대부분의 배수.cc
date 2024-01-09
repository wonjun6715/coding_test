#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n = 1;
    int arr[5];
    int count = 0;
    for (int i = 0; i < 5; i++) {
        cin >> arr[i];
    }

    while (1) {
        count = 0;
        for (int i = 0; i < 5; i++) {
            if (n % arr[i] == 0) {
                count++;
            }
        }
        if (count >= 3) {
            cout << n;
            break;
        }
        n++;
    }
}