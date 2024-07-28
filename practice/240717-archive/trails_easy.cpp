#include <iostream>
#include <vector>
using namespace std;

int inp() {
    int x;
    cin >> x;
    return x;
}

vector<int> inlt() {
    vector<int> v;
    int x;
    while (cin >> x) {
        v.push_back(x);
        if (cin.get() == '\n') break;
    }
    return v;
}

vector<char> insr() {
    string s;
    cin >> s;
    vector<char> v(s.begin(), s.end() - 1);
    return v;
}

vector<int> invr() {
    vector<int> v;
    int x;
    while (cin >> x) {
        v.push_back(x);
        if (cin.get() == '\n') break;
    }
    return v;
}

int main() {
    const int MOD = 1e9 + 7;

    vector<int> mn = inlt();
    int m = mn[0], n = mn[1];
    vector<int> s = inlt();
    vector<int> l = inlt();

    vector<long long> dp(m, 0);
    dp[0] = 1;

    for (int t = 0; t < n; ++t) {
        vector<long long> ndp(m, 0);
        for (int i = 0; i < m; ++i) {
            long long sm = 0;
            for (int j = 0; j < m; ++j) {
                sm = (sm + dp[j] * s[j] * l[i] % MOD) % MOD;
                sm = (sm + dp[j] * s[j] * s[i] % MOD) % MOD;
                sm = (sm + dp[j] * l[j] * s[i] % MOD) % MOD;
            }
            ndp[i] = sm;
        }
        dp = ndp;
    }

    long long result = 0;
    for (int i = 0; i < m; ++i) {
        result = (result + dp[i]) % MOD;
    }

    cout << result << endl;
    return 0;
}
