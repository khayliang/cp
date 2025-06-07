#include <iostream>
#include <vector>
#include <string>
#include <iterator>
#include <stack>
#include <cmath>
#include <queue>

#define ll long long
#define EPS 1e-9
#define repeat(idx, start, end) for (int idx = start; idx != end; ++idx)

using namespace std;

template<typename T>
void print_vec(const vector<T>& arr) {
    for (T& x: arr) cout << x << " ";
    cout << "\n";
}

vector<int> read_int_arr(int n) {
    vector<int> arr(n);
    repeat(i, 0, n) {
        cin >> arr[i];
    }
    return arr;
}

void run() {
    int n;
    cin >> n;
    vector<int> a_raw = read_int_arr(n);
    vector<int> a {};
    for (int x : a_raw) {
        if (a.size() != 0 && a.back() == x) continue;
        a.push_back(x);
    }

    int res = 1;
    int prev = a[0];
    repeat(i, 1, a.size()) {
        if (prev + 1 != a[i]) {
            ++res;
            prev = a[i];
        }
    }
    cout << res << "\n";
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        run();
    }
    return 0;
}