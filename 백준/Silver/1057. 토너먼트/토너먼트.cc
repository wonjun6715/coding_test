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

    int kim;
    int lim;
    int n;
    int count = 0;

    cin >> n >> kim >> lim;

    while (kim != lim) {
        kim = (kim + 1) / 2;
        lim = (lim + 1) / 2;
        count++;
        if (kim == 0 || lim == 0) {
            cout << -1;
            exit(0);
        }
    }

    cout << count;
    
}