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

int main() {
    int t;
    cin >> t;
    while (t--) {
        int x;
        cin >> x;
        double sx = sqrt(x);
        if (sx - floor(sx) < EPS) {
            cout << int(sx) << " " << 0 << endl;
        } else cout << -1 << endl;
    }
    return 0;
}