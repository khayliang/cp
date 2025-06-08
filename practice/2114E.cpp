#include <bits/stdc++.h>

#define repeat(idx, start, end) for (int idx = start; idx != end; ++idx)
#define F first
#define S second
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define pb emplace_back
#define mp make_pair

using namespace std;

typedef pair<int, int> ipair;
typedef long long ll;
typedef long double ld;

const double EPS = 1e-9;
const ll INF = 1e18;
const int MOD = 1e9 + 7;
const ld PI = atan2(0, -1);

mt19937 rnd(time(nullptr));

template<typename T>
void print_vec(const vector<T>& arr) {
    for (const T& x: arr) cout << x << " ";
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

void run() {
    int n;
    cin >> n;
    auto a = read_int_arr(n);
    auto edges = vector<vector<int>>(n);
    auto parents = vector<int>(n);
    repeat(i, 0, n - 1) {
        int x, y;
        cin >> x >> y;
        --x, --y;
        edges[x].pb(y), edges[y].pb(x);
    }
    auto mins = vector<ll>(n);
    auto maxs = vector<ll>(n);

    auto dfs = [&](auto&& self, int curr) -> void {
        if (curr == 0) {
            parents[0] == -1;
            mins[0] = a[0];
            maxs[0] = a[0];
        } else {
            int parent = parents[curr];
            mins[curr] = min({1LL * a[curr] - mins[parent], 1LL * a[curr] - maxs[parent], 1LL * a[curr]});
            maxs[curr] = max({1LL * a[curr] - mins[parent], 1LL * a[curr] - maxs[parent], 1LL * a[curr]});
        }
        for (int v : edges[curr]) {
            if (v == parents[curr]) continue;
            parents[v] = curr;
            self(self, v);
        }
    };
    dfs(dfs, 0);
    print_vec(maxs);
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        run();
    }
    return 0;
}