#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

bool binary_search(vector<int>& arr, int len, int target);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int m, n;
    int count = 0;
    cin >> m;

    vector<int> A(m, 0);

    for (int i = 0; i < m; i++) {
        cin >> A[i];
    }
    sort(A.begin(), A.end());
    cin >> n;

    vector<int> B(n, 0);

    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }

    for (int j = 0; j < n; j++) {
        if (binary_search(A, A.size(), B[j])) {
            cout << "1 ";
        }
        else {
            cout << "0 ";
        }
    }

    return 0;
}

bool binary_search(vector<int>& arr, int len, int target) {
    int low = 0;
    int high = len - 1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (arr[mid] == target) {
            return true;
        }
        else if (arr[mid] < target) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    return false;
}