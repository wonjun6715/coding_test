#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    char arr[8][8];
    int count = 0;

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 'F') {
                if (i % 2 == 0) {
                    if (j % 2 == 0) {
                        count++;
                    }
                }
                else if (i % 2 == 1) {
                    if (j % 2 == 1) {
                        count++;
                    }
                }
            }
            
        }
    }
    cout << count;
}