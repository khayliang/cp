#include <iostream>
#include <vector>
#include <string>
#include <iterator>
#include <stack>
#include <cmath>
#include <queue>

using ll = long long;

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        // if mod 4 == 0  then just cows
        // else value - 2 cows and 1 chicken
        int n;
        cin >> n;
        if (n % 4 == 0) {
            cout << n / 4 << "\n";
        } else {
            cout << n / 4 + 1 << "\n";
        }
    }
    return 0;
}