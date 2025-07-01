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

template <typename T>
void print_vec(const vector<T>& arr) {
  for (const T& x : arr) cout << x << " ";
  cout << "\n";
}

template <typename T1, typename T2>
void print_pair(const pair<T1, T2>& p) {
  cout << p.first << ' ' << p.second << '\n';
}

vector<int> read_int_arr(int n) {
  vector<int> arr(n);
  repeat(i, 0, n) { cin >> arr[i]; }
  return arr;
}

vector<ll> read_ll_arr(ll n) {
  vector<ll> arr(n);
  repeat(i, 0, n) { cin >> arr[i]; }
  return arr;
}
void run() {
  ll n, k;
  cin >> n >> k;
  auto a = read_ll_arr(n);
  bool stop = false;
  for (ll i = 0; i != (ll)log2(10e19); ++i) {
    if (stop) break;
    ll x = pow(2, i);
    repeat(j, 0, n) {
      if ((x & a[j]) != 0) { 
        continue;
      }
      if (k < x) {
        stop = true;
        break;
      }
      a[j] += x;
      k -= x;
    }
  }
  int res = 0;
  repeat(i, 0, n) {
    res += __builtin_popcountll(a[i]);
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