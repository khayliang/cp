#include <bits/stdc++.h>
    
#define repeat(idx, start, end) for (int idx = start; idx != end; ++idx)
#define repeat_reverse(idx, start, end) for (int idx = start; idx != end; --idx)
    
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
const ll INFLL = 1e18;
const ll INF = 1e9 + 7;

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

struct Edge {
    int from;
    int to;
    int weight;

};

struct CompareEdge {
    bool operator()(const Edge& a, const Edge& b) { return a.weight > b.weight; };
};

void run() {
    int n, m;
    cin >> n >> m;
    auto b = read_int_arr(n);

    vector<vector<Edge>> adj(n);

    repeat(i, 0, m) {
        int s, t, w;
        cin >> s >> t >> w;
        --s, --t;
        adj[s].pb(Edge {s, t, w});
    }

    int l = 0, r = 1e9;

    auto test = [&](int batt) {
        vector<int> best(n);
        repeat(i, 0, n) {
            if (i > 0 && best[i] == 0) continue;
            best[i] = min(best[i] + b[i], batt);
            for (Edge& e : adj[i]) {
                if (e.weight > best[i]) continue;
                best[e.to] = min(max(best[e.to], best[i]), batt);
            }
        }
        return best.back() > 0;
    };
    while (l < r) {
        int m = (l + r) / 2;
        if (test(m)) { 
            r = m; 
        } 
        else { l = m + 1; }
    }
    if (r == l && test(r)) {
        cout << r << "\n";
        return;
    }
    cout << "-1" << "\n";    
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        run();
    }
    return 0;
}