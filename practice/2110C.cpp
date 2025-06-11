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
    
void fail() {
    cout << -1 << "\n";
}
    
void run() {
    int n;
    cin >> n;
    auto d = vector<int>(n);
    repeat(i, 0, n) { cin >> d[i]; }
    auto l = vector<int>(n);
    auto r = vector<int>(n);
    repeat(i, 0, n) {
        cin >> l[i] >> r[i];
    }
    
    auto mins = vector<int>(n + 1);
    auto maxs = vector<int>(n + 1);
    
    repeat(i, 1, n + 1) {
        maxs[i] = min(r[i - 1], maxs[i - 1] + (d[i - 1] == -1 ? 1 : d[i - 1]));
        mins[i] = max(l[i - 1], mins[i - 1] + (d[i - 1] == -1 ? 0 : d[i - 1]));
        if (maxs[i] < mins[i]) {
            return fail(); 
        }
    }
    int h = mins[n];
    repeat_reverse(i, n - 1, -1) {
        if (d[i] != -1) {
            h -= d[i];
        } else {
            if (h == mins[i]) {
                d[i] = 0;
            } else {
                d[i] = 1;
                --h;
            }
        }
    }
    print_vec(d);
}
    
int main() {
    int t;
    cin >> t;
    
    while (t--) {
        run();
    }
    return 0;
}