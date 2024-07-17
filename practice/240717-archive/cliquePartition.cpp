#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
       int N, K;
        cin >> N >> K;
        vector<int> a(N), c(N);
        for (int i = 0; i != N; ++i) {
            a[i] = i + 1;
            c[i] = i / K + 1;
        }
        int q = (N - 1)/K + 1;
        for (int i = 1; i <= q; ++i) {
            int l = find(c.begin(), c.end(), i) - c.begin();
            int r = c.rend() - find(c.rend(), c.rbegin(), i);
            int m = (r + l) / 2;
            reverse(a.begin() + l, a.begin() + m);
            reverse(a.begin() + m, a.begin() + r);
        }
        for(int i = 0; i < N; i++)
        cout << a[i] << " \n"[i == N - 1];
    cout << q << "\n";
    for(int i = 0; i < N; i++)
        cout << c[i] << " \n"[i == N - 1];

    }
    return 0;
}