#include <iostream>
#include <vector>
#include <string>
#include <iterator>
#include <stack>
#include <cmath>
#include <queue>
#include <array>

#define ll long long
#define repeat(idx, start, end) for (int idx = start; idx != end; ++idx)
#define ipair pair<int, int>
#define F first
#define S second

using namespace std;

const int INF = 1e9 + 7;
const ll LLINF = 1e18;
const double EPS = 1e-9;

template<typename T>
void print_vec(const vector<T>& arr) {
    for (T& x: arr) cout << x << " ";
    cout << "\n";
}

template<typename T1, typename T2>
void print_pair(const pair<T1, T2>& p) {
    cout << p.first << ' ' << p.second << '\n';
}

vector<int> read_int_arr(int n) {
    vector<int> arr(n);
    repeat(i, 0, n) {
        cin >> arr[i];
    }
    return arr;
}

int diff(pair<int, int> x) {
    if (x.second == 0 || x.second == INF) return 0;
    return abs(x.first - x.second);
}

// idea: find the edges that have only one monster. for all edges
// with only one, then we select the monster that has the greatest change if moved in.
void run() {
    int n;
    cin >> n;
    vector<pair<int, int>> monsters {};
    repeat(i, 0, n) {
        int x, y;
        cin >> x >> y;
        monsters.emplace_back(x, y);
    }
    
    pair<int, int> min_x {INF, INF}, min_y {INF, INF};
    pair<int, int> max_x {0, 0}, max_y {0, 0};
    // given one 
    for (auto& [x, y] : monsters) {
        min_x.second = x < min_x.first ? min_x.first : min(x, min_x.second);
        min_x.first = min(min_x.first, x);
        max_x.second = x > max_x.first ? max_x.first : max(x, max_x.second);
        max_x.first = max(max_x.first, x);
        min_y.second = y <= min_y.first ? min_y.first : min(y, min_y.second);
        min_y.first = min(min_y.first, y);
        max_y.second = y > max_y.first ? max_y.first : max(y, max_y.second);
        max_y.first = max(max_y.first, y);
    }

    ll bs = LLINF;
    // check for all monsters, if we remove it then what resulting rect do we get
    for (auto& [x, y] : monsters) {
        int cxmin = x == min_x.F ? (min_x.S < INF ? min_x.S : min_x.F) : min_x.F;
        int cxmax = x == max_x.F ? (max_x.S > 0 ? max_x.S : max_x.F) : max_x.F;
        int cymin = y == min_y.F ? (min_y.S < INF ? min_y.S : min_y.F) : min_y.F;
        int cymax = y == max_y.F ? (max_y.S > 0 ? max_y.S : max_y.F) : max_y.F;
        int bl = cxmax - cxmin + 1;
        int bh = cymax - cymin + 1;
        ll sz = 1LL * bl * bh;
        if (sz < monsters.size()) {
            sz += min(bl, bh);
        }
        bs = min(bs, sz);
    }
    cout << bs << "\n";
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        run();
    }
    return 0;
}