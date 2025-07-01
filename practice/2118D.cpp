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

struct v {
  bool success;
  bool visited = false;
};

void run() {
  int n, k;
  cin >> n >> k;
  auto pa = read_ll_arr(n);
  auto da = read_int_arr(n);

  auto lefts = vector<v>(n);
  auto rights = vector<v>(n);

  auto find = [&](bool ri, ll pos, int tm) {
    if (ri) {
      repeat(i, 0, pa.size()) {
        ll p = pa[i];
        if (p < pos) continue;
        ll diff = p - pos;
        if (((diff + tm) % k) == da[i]) return i;
      }
    } else {
      repeat_reverse(i, pa.size() - 1, -1) {
        ll p = pa[i];
        if (p > pos) continue;
        ll diff = pos - p;
        if (((diff + tm) % k) == da[i]) return i;
      }
    }
    return -1;
  };

  // lefts
  repeat(i, 0, n) {
    if (lefts[i].visited) continue;

    set<pair<int, bool>> visited;
    visited.insert({i, false});

    bool ri = false;
    ll pos = pa[i];
    int tm = 0;

    bool succ = false;

    while (true) {
      int next_idx = find(ri, pos, tm);
      if (next_idx == -1) {
        succ = true;
        break;
      }
      pos = pa[next_idx];
      tm = da[next_idx];
      ri = !ri;
      pair<int, bool> nxt = {next_idx, ri};
      if (visited.find(nxt) != visited.end()) {
        succ = false;
        break;
      }

      visited.insert(nxt);
    }
    for (auto q_pv : visited) {
      if (q_pv.second) {
        rights[q_pv.first].success = succ;
        rights[q_pv.first].visited = true;
      } else {
        lefts[q_pv.first].success = succ;
        lefts[q_pv.first].visited = true;
      }
    }
  }
  cout << "lefts: ";
  repeat(i, 0, n) {
     cout << lefts[i].success << " ";
  }
  cout << "\n";
  cout << "rights: ";
  repeat(i, 0, n) {
     cout << rights[i].success << " ";
  }
  cout << "\n";
  int q;
  cin >> q;
  auto aa = read_ll_arr(q);
  repeat(i, 0, q) {
    ll a = aa[i];
    int nxt_i = find(true, a, 0);
    if (nxt_i == -1 || lefts[nxt_i].success)
      cout << "YES\n";
    else
      cout << "NO\n";
  }
}

int main() {
  int t;
  cin >> t;

  while (t--) {
    run();
  }
  return 0;
}