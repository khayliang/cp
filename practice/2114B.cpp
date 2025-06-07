#include <iostream>
#include <vector>
#include <string>
#include <iterator>
#include <stack>
#include <cmath>
#include <queue>

#define ll long long
#define EPS 1e-9

using namespace std;

void run() {
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;
    int counts[2] {};
    for (char c: s) {
        ++counts[c - '0'];
    }
    int diff = min(counts[0], counts[1]);
    int req_diff = (n / 2) - k;

    if (req_diff > diff) {
        cout << "NO\n";
        return;
    }

    if (abs(diff - req_diff) % 2 != 0) {
        cout << "NO\n";
        return;
    }

    int same = (counts[0] - req_diff) / 2 + (counts[1] - req_diff) / 2;
    if (same < k) {
        cout << "NO\n";
        return;
    }

    cout << "YES\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        run();
    }
    return 0;
}